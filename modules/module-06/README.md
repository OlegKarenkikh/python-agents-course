# Модуль 6: Проект — Агент ДЗО 🏗️

> **Время:** ~6 часов | **Уровень:** средний+

## Чему вы научитесь

- Что такое FastAPI и как создать API
- Интегрировать агента в API
- Что такое Docker
- Как читать код реального проекта

---

## 🌐 FastAPI: API за 5 минут

![Запрос идёт к агенту и возвращает ответ](https://user-gen-media-assets.s3.amazonaws.com/gemini_images/fd0b9ae7-b4aa-4976-a371-c2f9fa7a5ba6.png)

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AppRequest(BaseModel):
    text: str

@app.get("/health")
def health(): return {"status": "ok"}

@app.post("/check")
async def check(req: AppRequest):
    result = agent.process(req.text)
    return {"result": result}
```

```bash
uvicorn agent_app:app --reload
# Swagger UI: http://localhost:8000/docs
```

---

## 🐳 Docker: упаковка для приложения

```
Без Docker:       С Docker:
"У меня не    →  Python 3.11 + все зависимости
работает!"       + наш код → работает везде!
```

---

## 🔍 Анализ реального проекта

[dzo-tz-agents](https://github.com/OlegKarenkikh/dzo-tz-agents):

```
agent1_dzo_inspector/
  agent.py   ← create_react_agent
  tools.py   ← @tool функции
api/app.py   ← FastAPI эндпоинты
shared/llm.py ← build_llm()
```

---

## 📝 Практика

[`practice/`](practice/)

## ✅ Чек-лист

- [ ] Запустил FastAPI
- [ ] Добавил эндпоинт с агентом
- [ ] Прочитал `agent1_dzo_inspector/agent.py`

**Следующий:** [Модуль 7 →](../module-07/README.md)
