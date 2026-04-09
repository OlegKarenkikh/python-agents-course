# Решение: Агент через LangChain + LangGraph

import os
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent


@tool
def check_application_tool(text: str) -> str:
    """Проверяет заявку на полноту.
    Используй, когда нужно проверить полноту заявки.
    """
    errors = []
    for field in ["название", "количество", "дата"]:
        if field not in text.lower():
            errors.append(f"отсутствует '{field}'")
    if errors:
        return f"Неполная: {'; '.join(errors)}"
    return "Заявка полная!"


@tool
def register_application_tool(text: str) -> str:
    """Регистрирует заявку.
    Используй только после успешной проверки.
    """
    import random
    return f"Заявка зарегистрирована под номером №{random.randint(1000, 9999)}."


SYSTEM_PROMPT = """\
Ты — инспектор заявок. Проверяй заявку и регистрируй если она полная.
ШАГ 1: вызови check_application_tool
ШАГ 2: если полная — вызови register_application_tool
ШАГ 3: ответь пользователю
"""


def create_agent():
    github_token = os.environ.get("GITHUB_TOKEN", "")
    
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=github_token or "sk-placeholder",
        base_url="https://models.inference.ai.azure.com" if github_token else None,
    )
    
    agent = create_react_agent(
        model=llm,
        tools=[check_application_tool, register_application_tool],
        prompt=SYSTEM_PROMPT,
    )
    return agent


if __name__ == "__main__":
    agent = create_agent()
    result = agent.invoke({
        "messages": [{
            "role": "user",
            "content": "Проверь: название=закупка, количество=5, дата=2024-01-15"
        }]
    })
    print(result["messages"][-1].content)
