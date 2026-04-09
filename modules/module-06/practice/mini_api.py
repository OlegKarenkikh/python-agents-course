# Практика: Мини-API с агентом
# Задача: создайте FastAPI-сервер с эндпоинтами:
# GET /health → {status: ok}
# POST /check → проверяет заявку (без LLM)
# POST /process → проверяет + регистрирует
#
# Запуск:
#   pip install fastapi uvicorn
#   uvicorn practice.mini_api:app --reload
# Откройте http://localhost:8000/docs

from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI(title="Мини-Инспектор")


class AppRequest(BaseModel):
    text: str


@app.get("/health")
def health():
    return {"status": "ok", "version": "1.0"}


# TODO: добавьте POST /check и POST /process
# /check: проверьте наличие "название" и "количество" в text
# /process: /check + если ok → регистрирует с случайным номером
