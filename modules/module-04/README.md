# Модуль 4: LangChain ⛓️

> **Время:** ~5 часов | **Уровень:** средний

## Чему вы научитесь

- Что такое LangChain и зачем он нужен
- Создавать цепочки (Chains)
- Добавлять память (Memory)
- Работать с шаблонами промптов

---

## 🧩 Что такое LangChain?

![Конструктор блоков для агента](https://user-gen-media-assets.s3.amazonaws.com/gemini_images/9340adb2-6d81-4c6f-a645-12e0737c685e.png)

LangChain — **набор блоков**, из которых собираются приложения с LLM.

---

## 🔗 Цепочки (Chains)

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

промпт = ChatPromptTemplate.from_messages([
    ("system", "Ты — инспектор. Отвечай кратко."),
    ("user", "{question}"),
])
цепочка = промпт | ChatOpenAI(model="gpt-4o-mini") | StrOutputParser()
рез = цепочка.invoke({"вопрос": "Проверь заявку: название: тест"})
```

```
цепочка: вопрос → [Промпт] → [Модель] → [Парсер] → str
```

---

## 🧠 Память (Memory)

Без памяти LLM не помнит предыдущие сообщения.

```python
from langchain.memory import ConversationBufferWindowMemory
память = ConversationBufferWindowMemory(k=5, return_messages=True)
память.save_context({"input": "заявка"}, {"output": "полная"})
```

---

## 📝 Практика

[`practice/`](practice/)

## ✅ Чек-лист

- [ ] Собрал цепочку prompt | model | parser
- [ ] Добавил память
- [ ] Создал агент с инструментами

**Следующий:** [Модуль 5 →](../module-05/README.md)
