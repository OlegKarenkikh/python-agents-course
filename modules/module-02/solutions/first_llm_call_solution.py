# ============================================
# Решение: Первый запрос к LLM
# ============================================

import os
from openai import OpenAI

SYSTEM_PROMPT = """Ты — инспектор заявок. Проверяй текст заявки
и отвечай: полная ли она? Если нет, что отсутствует?"""


def check_with_llm(text: str) -> str:
    """' Отправляет текст заявки в LLM и возвращает ответ."""
    github_token = os.environ.get("GITHUB_TOKEN", "")
    if not github_token:
        return "Ошибка: GITHUB_TOKEN не установлен."
    
    client = OpenAI(
        api_key=github_token,
        base_url="https://models.inference.ai.azure.com",
    )
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # дешевле для учёбы
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text},
        ],
        max_tokens=500,
    )
    
    return response.choices[0].message.content


if __name__ == "__main__":
    print("Пример 1 — полная заявка:")
    полная = "Название: закупка серверов Dell, количество: 5 шт, дата: 2024-03-15, инициатор: Иванов А."
    print(check_with_llm(полная))
    
    print("\nПример 2 — неполная заявка:")
    неполная = "Пожалуйста, дайте денег на офис"
    print(check_with_llm(неполная))
