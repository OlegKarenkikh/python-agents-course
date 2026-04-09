# Инструменты агента ДЗО
# Инспирировано: agent1_dzo_inspector/tools.py из dzo-tz-agents

import random
import datetime
from langchain_core.tools import tool


@tool
def check_application_completeness(text: str) -> str:
    """Проверяет полноту заявки по чек-листу.
    
    Проверяет наличие обязательных полей заявки.
    Вызывай этот инструмент первым для любой заявки.
    
    Args:
        text: Полный текст заявки для проверки.
    """
    required = {
        "название": "Название закупки",
        "количество": "Количество с единицами",
        "дата": "Дата поставки",
        "инициатор": "Инициатор (ФИО)",
    }
    
    missing = []
    text_lower = text.lower()
    for keyword, field_name in required.items():
        if keyword not in text_lower:
            missing.append(field_name)
    
    if missing:
        return (
            f"✖ Заявка НЕПОЛНАЯ.\n"
            f"Отсутствует:\n"
            + "\n".join(f"  - {f}" for f in missing)
        )
    return "✔ Заявка ПОЛНАЯ. Все обязательные поля указаны."


@tool
def register_in_system(application_text: str) -> str:
    """Регистрирует заявку в системе электронного документооборота.
    
    Вызывай только после успешной проверки полноты.
    Функция создаёт номер заявки.
    
    Args:
        application_text: Текст полной заявки.
    """
    number = random.randint(10000, 99999)
    today = datetime.date.today().isoformat()
    return (
        f"✅ Заявка зарегистрирована\n"
        f"Номер: №{number}\n"
        f"Дата: {today}\n"
        f"Статус: Ожидает обработки"
    )


@tool
def request_additional_info(missing_fields: str) -> str:
    """Формирует письмо с запросом на дополнение заявки.
    
    Используй, когда заявка неполна и нужно запросить недостающие данные.
    
    Args:
        missing_fields: Перечисление отсутствующих полей.
    """
    return (
        f"Добрый день!\n\n"
        f"Для регистрации вашей заявки необходимо указать следующие данные:\n"
        f"{missing_fields}\n\n"
        f"Пожалуйста, дополните заявку и отправьте повторно.\n"
        f"С уважением,\nИнспектор ДЗО"
    )
