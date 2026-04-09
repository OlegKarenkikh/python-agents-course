# Тесты без LLM — проверяет инструменты напрямую
# Запуск: python test_agent.py

from tools import (
    check_application_completeness,
    register_in_system,
    request_additional_info,
)


def test_full_application():
    """\u041f\u043e\u043b\u043d\u0430\u044f \u0437\u0430\u044f\u0432\u043a\u0430 \u0434\u043e\u043b\u0436\u043d\u0430 пройти."""
    text = "Название: покупка ноутбуков, количество: 5 шт, дата: 2024-03-15, инициатор: Петров И."
    result = check_application_completeness.invoke(text)
    assert "ПОЛНАЯ" in result, f"Ожидался УСПЕХ, получил: {result}"
    print("✅ test_full_application: прошёл")


def test_incomplete_application():
    """\u041dе\u043f\u043e\u043b\u043d\u0430\u044f \u0437\u0430\u044f\u0432\u043a\u0430 \u0434\u043e\u043b\u0436\u043d\u0430 \u0431\u044b\u0442\u044c \u043e\u0442\u0432\u0435\u0440\u0433\u043d\u0443\u0442\u0430."""
    text = "Пожалуйста, нужны деньги"
    result = check_application_completeness.invoke(text)
    assert "НЕПОЛНАЯ" in result, f"Ожидался ОШИБКА, получил: {result}"
    print("✅ test_incomplete_application: прошёл")


def test_register():
    """\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f \u0434\u043e\u043b\u0436\u043d\u0430 \u0432\u0435\u0440\u043d\u0443\u0442\u044c \u043d\u043e\u043c\u0435\u0440."""
    result = register_in_system.invoke("любой текст")
    assert "№" in result, f"Ожидался номер, получил: {result}"
    print("✅ test_register: прошёл")


def test_request_info():
    """\u0417\u0430\u043f\u0440\u043e\u0441 \u0434\u043e\u043b\u0436\u0435\u043d \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0442\u044c \u043f\u043e\u043b\u044f."""
    result = request_additional_info.invoke("название, количество")
    assert "указать" in result.lower(), f"Ожидался запрос, получил: {result}"
    print("✅ test_request_info: прошёл")


if __name__ == "__main__":
    print("\n=== Тесты инструментов (без LLM) ===")
    test_full_application()
    test_incomplete_application()
    test_register()
    test_request_info()
    print("\nВсе тесты прошли! 🎉")
