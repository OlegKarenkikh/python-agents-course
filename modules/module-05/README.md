# Модуль 5: LangGraph 🔀

> **Время:** ~5 часов | **Уровень:** средний

## Чему вы научитесь

- Что такое граф и узлы
- Как работает состояние (State)
- Как строить циклы в графе
- Почему `dzo-tz-agents` использует LangGraph

---

## 🔷 Что такое граф?

![Граф решений с состоянием](https://user-gen-media-assets.s3.amazonaws.com/gemini_images/d6a674bb-3b35-4215-81f2-4c457c5c6fc1.png)

Граф — схема, где есть **узлы** (действия) и **рёбра** (переходы между ними).

```
START → [Проверка] → развилка:
  Полная? → [Регистрация] → END
  Неполная? → [Запрос] → END
```

---

## 📦 Состояние (State)

```python
from typing import TypedDict

class AgentState(TypedDict):
    messages: list   # история сообщений
    status: str      # текущий статус
    errors: list     # ошибки
```

---

## 🛠️ create_react_agent

```python
from langgraph.prebuilt import create_react_agent

agent = create_react_agent(
    model=llm,
    tools=[check_tool, register_tool],
    prompt="Ты — инспектор.",
)
result = agent.invoke({"messages": [{"role": "user", "content": "заявка..."}]})
```

---

## 📝 Практика

[`practice/`](practice/)

## ✅ Чек-лист

- [ ] Понимаю разницу узла и рёбра
- [ ] Понимаю, что такое State
- [ ] Разобрался в `agent1_dzo_inspector/agent.py`

**Следующий:** [Модуль 6 →](../module-06/README.md)
