# Модуль 4: LangChain ⛓️

> **Время:** ~5 часов | **Уровень:** средний

## Чему вы научитесь

- Что такое LangChain и зачем он нужен
- Создавать цепочки (Chains)
- Добавлять память (Memory)
- Работать с шаблонами промптов

---

## 🧩 Что такое LangChain?

LangChain — это **набор блоков**, из которых собираются приложения с LLM.

```
Без LangChain:                   С LangChain:

Написать API-клиент    →   from langchain_openai import ChatOpenAI
Написать память          →   + ChatMessageHistory()
Написать обработку tools →   + @tool + AgentExecutor
Написать парсинг       →   + StrOutputParser()
```

---

## 🔗 Цепочки (Chains)

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Три блока связаны в цепочку (оператор |)
промпт = ChatPromptTemplate.from_messages([
    ("system", "Ты — инспектор. Отвечай кратко."),
    ("user", "{question}"),
])
модель = ChatOpenAI(model="gpt-4o-mini")
парсер = StrOutputParser()

# Строим цепочку:
цепочка = промпт | модель | парсер

# Запускаем:
рез = цепочка.invoke({"question": "Проверь заявку: название: тест"})
print(рез)  # строка с ответом
```

```
Цепочка визуально:

вопрос → [Промпт] → [Модель] → [Парсер] → результат
  str        мессажи     LLM        str
```

---

## 🧠 Память (Memory)

Без памяти LLM не помнит предыдущие сообщения. В `dzo-tz-agents` используется `ConversationBufferWindowMemory(k=20)`.

```python
from langchain.memory import ConversationBufferWindowMemory

память = ConversationBufferWindowMemory(
    k=5,           # храним последние 5 обменов
    return_messages=True,
)

память.save_context(
    {"input": "Проверь заявку название: тест"},
    {"output": "Полная!"},
)
print(память.load_memory_variables({}))
```

---

## 📝 Практика

См. папку [`practice/`](practice/)

## ✅ Чек-лист

- [ ] Собрал цепочку из prompt | model | parser
- [ ] Добавил память к цепочке
- [ ] Создал агент с инструментами через LangChain

---

**Следующий:** [Модуль 5 — LangGraph →](../module-05/README.md)
