# Модуль 6: Проект — Агент ДЗО 🏗️

> **Время:** ~6 часов | **Уровень:** средний+

## Чему вы научитесь

- Что такое FastAPI и как создать API
- Интегрировать агента в API
- Что такое Docker
- Как читать код реального проекта

---

## 🌐 FastAPI: API за 5 минут

**API** (веб-версия) — это программа, которая получает запросы из интернета и возвращает данные.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ApplicationRequest(BaseModel):
    text: str
    subject: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/api/v1/process/dzo")
async def process_dzo(req: ApplicationRequest):
    # Вот здесь будет стоять вызов агента:
    result = agent.invoke({"input": req.text})
    return {"result": result["output"]}
```

```
Визуально:

  Пользователь/сайт → POST /api/v1/process/dzo
           (запрос с JSON)
                   ↓
           [Наш FastAPI]
                   ↓
           [Агент LangGraph]
                   ↓
           [Генерирует ответ]
                   ↓
  Пользователь ← JSON с результатом
```

---

## 🐳 Docker: упаковка для приложения

Docker — это коробка (контейнер) для вашей программы. Идёт везде одинаково.

```
Без Docker:       С Docker:

"У меня не    →  Всё в контейнере:
работает!"       Python 3.11
                   все зависимости
                   наш код
                   → работает везде!
```

---

## 🔍 Анализ реального проекта

Откройте файлы в исходном репозитории [dzo-tz-agents](https://github.com/OlegKarenkikh/dzo-tz-agents):

```
dzo-tz-agents/
├── agent1_dzo_inspector/
│   ├── agent.py        ← здесь create_react_agent
│   ├── tools.py        ← здесь @tool функции
│   └── runner.py       ← здесь IMAP-поллинг
├── api/
│   └── app.py          ← FastAPI эндпоинты
├── shared/
│   ├── llm.py          ← build_llm()
│   └── logger.py       ← setup_logger()
└── main.py             ← точка входа
```

---

## 📝 Практика

См. папку [`practice/`](practice/)

## ✅ Чек-лист

- [ ] Запустил FastAPI с одним эндпоинтом
- [ ] Добавил эндпоинт с агентом
- [ ] Прочитал `agent1_dzo_inspector/agent.py` и понял каждую строку

---

**Следующий:** [Модуль 7 — Продвинутый →](../module-07/README.md)
