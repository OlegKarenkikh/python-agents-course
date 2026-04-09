# 🏆 Финальный проект: Агент ДЗО

> Полностью рабочее приложение — ваше портфолио!

## Что мы строим

```
Структура проекта:

Пользователь
    │ вводит текст заявки
    ↓
[FastAPI]
    │ принимает POST /check
    ↓
[Агент ДЗО (LangGraph)]
    ├─ check_tool   → проверка чек-листа
    ├─ register_tool → регистрация
    └─ notify_tool  → уведомление
    ↓
[Ответ JSON]
    ↓
Пользователь видит результат
```

## 🚀 Быстрый старт

```bash
# 1. Установка
pip install fastapi uvicorn langchain-openai langgraph

# 2. Задайте токен (GitHub Codespaces: авто)
export GITHUB_TOKEN=<ваш_токен>

# 3. Запустите сервер
uvicorn agent_app:app --reload

# 4. Отправьте запрос
curl -X POST http://localhost:8000/check \
  -H "Content-Type: application/json" \
  -d '{"text": "Название: закупка, количество: 5, дата: 2024-01-15"}'
```

## 📌 Что входит в проект

| Файл | Что делает |
|---|---|
| `agent_app.py` | FastAPI-сервер с эндпоинтами |
| `agent.py` | Создание агента через `create_react_agent` |
| `tools.py` | Инструменты: check, register, notify |
| `test_agent.py` | Тесты без LLM |

## ✅ Чек-лист защиты проекта

- [ ] `GET /health` возвращает `{status: ok}`
- [ ] `POST /check` возвращает результат проверки
- [ ] Агент вызывает check_tool перед register_tool
- [ ] Тесты проходят без LLM
- [ ] Код пушет в GitHub
