# Агент ДЗО — упрощённая версия для обучения
# Инспирировано: agent1_dzo_inspector/agent.py из dzo-tz-agents

import os
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from tools import (
    check_application_completeness,
    register_in_system,
    request_additional_info,
)

SYSTEM_PROMPT = """\
Ты — Инспектор ДЗО. Проверяешь заявки ДЗО на полноту.

ШАГ 1: Вызови check_application_completeness
ШАГ 2:
  - Если полная → вызови register_in_system
  - Если неполная → вызови request_additional_info
ШАГ 3: Ответь пользователю о результате

Важно:
- Вежливый деловой тон
- Не оценивай качество — только полноту!
"""


class DZOAgent:
    """\u0410\u0434\u0430\u043f\u0442\u0435\u0440 \u0430\u0433\u0435\u043d\u0442\u0430 \u0414\u0417\u041e \u0434\u043b\u044f \u0438\u043d\u0442\u0435\u0433\u0440\u0430\u0446\u0438\u0438 \u0441 FastAPI."""

    def __init__(self):
        github_token = os.environ.get("GITHUB_TOKEN", "")
        openai_key = os.environ.get("OPENAI_API_KEY", "")

        if github_token and not openai_key:
            llm = ChatOpenAI(
                model="gpt-4o-mini",
                api_key=github_token,
                base_url="https://models.inference.ai.azure.com",
                temperature=0.2,
            )
        else:
            llm = ChatOpenAI(
                model="gpt-4o-mini",
                temperature=0.2,
            )

        self._graph = create_react_agent(
            model=llm,
            tools=[
                check_application_completeness,
                register_in_system,
                request_additional_info,
            ],
            prompt=SYSTEM_PROMPT,
        )

    def process(self, text: str) -> str:
        """\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u0442\u0435\u043a\u0441\u0442 \u0437\u0430\u044f\u0432\u043a\u0438."""
        result = self._graph.invoke({
            "messages": [{"role": "user", "content": text}]
        })
        messages = result.get("messages", [])
        if messages:
            last = messages[-1]
            return getattr(last, "content", str(last))
        return "О\u0448\u0438\u0431\u043a\u0430: \u043f\u0443\u0441\u0442\u043e\u0439 \u043e\u0442\u0432\u0435\u0442"
