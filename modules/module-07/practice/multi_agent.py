# Практика: система двух агентов
# Задача:
# 1. Создайте двух агентов - dzo_agent и tz_agent
# 2. dzo_agent: проверяет наличие "дзо" или "заявка"
# 3. tz_agent: проверяет наличие "тз" или "техническое"
# 4. router(текст) → определяет кому передать

def dzo_agent(text: str) -> str:
    if "дзо" in text.lower() or "заявка" in text.lower():
        return f"[АГЕНТ ДЗО] Обрабатываю: {text[:50]}..."
    return f"[АГЕНТ ДЗО] Не моя область."


def tz_agent(text: str) -> str:
    if "тз" in text.lower() or "техническое" in text.lower():
        return f"[АГЕНТ ТЗ] Обрабатываю: {text[:50]}..."
    return f"[АГЕНТ ТЗ] Не моя область."


# TODO: реализуйте router(text) — определяет кому передать
def router(text: str) -> str:
    pass


if __name__ == "__main__":
    tests = [
        "ДЗО: заявка на покупку серверов",
        "ТЗ: техническое задание на разработку СРМ",
        "Информационный запрос",
    ]
    for test in tests:
        print(f"\nВход: {test}")
        print(f"Выход: {router(test)}")
