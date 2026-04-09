# Модуль 2: ИИ и Языковые Модели (LLM) 🧠

> **Время:** ~3 часа | **Уровень:** начальный

## Чему вы научитесь

- Что такое LLM и токены
- Как общаться с GPT через API
- Как писать хорошие промпты
- GitHub Models — бесплатный доступ к GPT-4o

---

## 🧠 Часть 1: Что такое LLM?

![Как работает LLM — от текста к ответу](https://user-gen-media-assets.s3.amazonaws.com/gemini_images/fe8e6f1d-0d3d-400a-8f98-b4265af0c3b8.png)

```
Как обучалась модель GPT:

Trillionы слов → Анализ → Модель знает:
📚 📚 📚       → 🔍🔍🔍  → «после ‘заявка’
                           часто идёт ‘название’»
```

---

## 🔢 Часть 2: Токены

Токен — минимальная единица текста. Стоимость API считается в токенах.

```
"Заявка на сервер"
   ↓
["Заявка"] ["на"] ["сер"] ["вер"] = 4 токена

GitHub Models: БЕСПЛАТНО! 🎉
```

---

## 🔑 Часть 3: GitHub Models — бесплатно

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["GITHUB_TOKEN"],
    base_url="https://models.inference.ai.azure.com",
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Ты — инспектор заявок."},
        {"role": "user", "content": "Проверь: название=закупка"},
    ],
)
print(response.choices[0].message.content)
```

---

## 💬 Часть 4: Структура промпта

![Структура промпта: system, user, assistant](https://user-gen-media-assets.s3.amazonaws.com/gemini_images/8daf6ca7-bf0f-4620-ac25-8f832b1918a7.png)

```
Структура диалога:

system   → правила игры (не виден пользователю)
user     → запрос пользователя
assistant→ ответ модели
```

---

## 📝 Практика

[`practice/`](practice/)

## ✅ Чек-лист

- [ ] Понимаю что такое LLM и токены
- [ ] Знаю отличие system/user/assistant
- [ ] Отправил первый запрос к GitHub Models

**Следующий:** [Модуль 3 →](../module-03/README.md)
