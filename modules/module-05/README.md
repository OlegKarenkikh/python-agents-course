# Модуль 5: LangGraph 🔀

> **Время:** ~5 часов | **Уровень:** средний

## Чему вы научитесь

- Что такое граф и узлы
- Как работает состояние (State)
- Как строить цикли в графе
- Почему `dzo-tz-agents` использует LangGraph, а не LangChain

---

## 🔷 Что такое граф?

Граф — это схема, где есть **узлы** (действия) и **рёбра** (переходы между ними).

```
Граф агента Инспектора ДЗО:

  [START]
     ↓
  [Получить письмо]
     ↓
  [Проверить заявку]
     ↓
  ◄──[Решение]
  │        ││
  │     [Требует дополнения]
  │                ↓
  │     [Отправить запрос]──▶ожидаем ответа...
  │                                  ↓
  │           [Получить ответ]
  │                                  ↓
  │───────────────────────────────────────▶[Проверить снова]
  [Полная] → [Зарегистрировать] → [Ответить]
                                  ↓
                                [END]
```

---

## 📦 Состояние (State)

Состояние — это общий ящик, который передаётся между узлами.

```python
from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage
import operator

# Состояние нашего агента
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]  # история сообщений
    статус: str      # текущий статус заявки
    ошибки: list   # список ошибок
```

---

## 🛠️ create_react_agent

В реальном проекте `dzo-tz-agents` используется `langgraph.prebuilt.create_react_agent` — готовый граф с ReAct:

```python
from langgraph.prebuilt import create_react_agent

# Создаём готовый агент-граф:
grapher = create_react_agent(
    model=llm,
    tools=[check_tool, register_tool],
    prompt="Ты — инспектор заявок.",
)

# Запуск графа:
result = grapher.invoke({
    "messages": [{"role": "user", "content": "Проверь заявку..."}]
})
```

Именно так написан реальный `create_dzo_agent()` в `agent1_dzo_inspector/agent.py`.

## ✅ Чек-лист

- [ ] Понимаю разницу узла и рёбра
- [ ] Понимаю, что такое State
- [ ] Разобрался в `agent1_dzo_inspector/agent.py`

---

**Следующий:** [Модуль 6 — Проект →](../module-06/README.md)
