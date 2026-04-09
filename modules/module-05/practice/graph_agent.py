# Практика: собственный граф-агент
# Задача: постройте граф вручную через StateGraph с узлами:
# - check_node: проверяет заявку
# - register_node: регистрирует (если полная)
# - reject_node: запрашивает дополнение (если неполная)

from typing import TypedDict
from langgraph.graph import StateGraph, END


class ApplicationState(TypedDict):
    text: str
    status: str
    result: str


def check_node(state: ApplicationState) -> ApplicationState:
    """Узел: проверка заявки."""
    text = state["text"]
    errors = []
    for field in ["название", "количество"]:
        if field not in text.lower():
            errors.append(field)
    if errors:
        return {**state, "status": "неполная", "result": f"Отсутствует: {errors}"}
    return {**state, "status": "полная", "result": "Проверка пройдена"}


def register_node(state: ApplicationState) -> ApplicationState:
    """Узел: регистрация."""
    import random
    num = random.randint(1000, 9999)
    return {**state, "result": f"Зарегистрирована №{num}"}


def reject_node(state: ApplicationState) -> ApplicationState:
    """Узел: запрос на дополнение."""
    return {**state, "result": f"\u0417апрос на дополнение: {state['result']}"}


def route(state: ApplicationState) -> str:
    """Маршрутизация: куда идти дальше."""
    if state["status"] == "полная":
        return "регистрация"
    return "запрос"


# Строим граф
graph = StateGraph(ApplicationState)
graph.add_node("проверка", check_node)
graph.add_node("регистрация", register_node)
graph.add_node("запрос", reject_node)
graph.set_entry_point("проверка")
graph.add_conditional_edges("проверка", route)
graph.add_edge("регистрация", END)
graph.add_edge("запрос", END)
app = graph.compile()

if __name__ == "__main__":
    r1 = app.invoke({"text": "название: тест, количество: 5", "status": "", "result": ""})
    print("Полная:", r1["result"])
    r2 = app.invoke({"text": "дайте денег", "status": "", "result": ""})
    print("Неполная:", r2["result"])
