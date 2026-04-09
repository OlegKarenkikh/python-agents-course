# Шпаргалка: LangGraph

## Создание агента (1 строка!)

```python
from langgraph.prebuilt import create_react_agent
agent = create_react_agent(model=llm, tools=[tool1, tool2], prompt="Ты...")
result = agent.invoke({"messages": [{"role": "user", "content": "задача"}]})
```

## Собственный граф

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict

class State(TypedDict):
    text: str
    result: str

def node_a(state): return {**state, "result": "обработано"}

graph = StateGraph(State)
graph.add_node("узел", node_a)
graph.set_entry_point("узел")
graph.add_edge("узел", END)
app = graph.compile()
result = app.invoke({"text": "вход", "result": ""})
```

## Условные переходы

```python
def router(state) -> str:
    return "узел_a" if state["ok"] else "узел_b"

graph.add_conditional_edges("проверка", router)
```

## Инструмент

```python
from langchain_core.tools import tool

@tool
def my_tool(text: str) -> str:
    """Описание — агент читает его! Важно."""
    return "результат"
```

## Памятные значения

| Понятие | Описание |
|---|---|
| `StateGraph` | Граф со состоянием |
| `add_node` | Добавить узел |
| `add_edge` | Прямой переход |
| `add_conditional_edges` | Условный переход |
| `compile()` | Собрать граф |
| `invoke()` | Запустить граф |
