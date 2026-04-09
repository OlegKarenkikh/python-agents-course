# Практика: создайте 3й инструмент request_info_tool

from langchain_core.tools import tool

@tool
def check_application_tool(text: str) -> str:
    """Проверяет заявку. Используй для проверки полноты."""
    errors = []
    if "название" not in text.lower():
        errors.append("отсутствует название")
    if "количество" not in text.lower():
        errors.append("отсутствует количество")
    if errors:
        return f"Неполная: {', '.join(errors)}"
    return "Полная!"

@tool
def register_application_tool(text: str) -> str:
    """Регистрирует заявку. Используй после успешной проверки."""
    import random
    return f"Зарегистрирована №{random.randint(1000,9999)}."

# TODO: добавьте request_info_tool(отсутствующие_поля)
# возвращает формальный запрос на дополнение

if __name__ == "__main__":
    print(check_application_tool.invoke("название: тест, количество: 5"))
    print(check_application_tool.invoke("пожалуйста дайте денег"))
