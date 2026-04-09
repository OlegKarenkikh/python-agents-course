# FastAPI-сервер с Агентом ДЗО
# Запуск: uvicorn agent_app:app --reload
# Swagger UI: http://localhost:8000/docs

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import DZOAgent

app = FastAPI(
    title="Инспектор ДЗО",
    description="Агент проверки заявок ДЗО",
    version="1.0.0",
)

# Создаём агента при запуске
agent = None


@app.on_event("startup")
async def startup():
    global agent
    try:
        agent = DZOAgent()
        print("Агент ДЗО запущен успешно")
    except Exception as e:
        print(f"Предупреждение: агент не запущен ({e}). API работает в режиме mock.")


class ApplicationRequest(BaseModel):
    text: str

    class Config:
        json_schema_extra = {
            "example": {
                "text": "Название: покупка офисной техники, количество: 10 шт, дата: 2024-03-15, инициатор: Иванов А.П."
            }
        }


@app.get("/health")
def health():
    """Проверка состояния сервиса."""
    return {"status": "ok", "agent": "ready" if agent else "mock"}


@app.post("/check")
async def check_application(req: ApplicationRequest):
    """Проверить заявку через агента."""
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Текст заявки пустой")

    if agent:
        result = agent.process(req.text)
    else:
        # Mock-режим без LLM
        errors = []
        for f in ["название", "количество", "дата", "инициатор"]:
            if f not in req.text.lower():
                errors.append(f)
        result = "Заявка полная!" if not errors else f"Неполная, отсутствует: {errors}"

    return {"result": result, "input_length": len(req.text)}
