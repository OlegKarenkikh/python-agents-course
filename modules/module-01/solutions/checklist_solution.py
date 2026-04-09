# ============================================
# Решение: Чек-лист проверки заявки
# ============================================

def check_application(text: str) -> dict:
    """Проверяет заявку по чек-листу."""
    errors = []
    text_lower = text.lower()
    
    required_fields = [
        ("название", "Отсутствует название закупки"),
        ("количество", "Отсутствует количество"),
        ("дата", "Отсутствует дата"),
    ]
    
    for field, error_msg in required_fields:
        if field not in text_lower:
            errors.append(error_msg)
    
    return {
        "errors": errors,
        "passed": len(errors) == 0,
    }


if __name__ == "__main__":
    полная = "Название: закупка оборудования, количество: 10 шт, дата: 2024-03-15"
    неполная = "Пожалуйста, дайте денег"
    
    print("Полная заявка:", check_application(полная))
    # Вывод: {'errors': [], 'passed': True}
    
    print("Неполная заявка:", check_application(неполная))
    # Вывод: {'errors': ['Отсутствует название закупки', 'Отсутствует количество', 'Отсутствует дата'], 'passed': False}
