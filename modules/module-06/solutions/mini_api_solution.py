# Решение: Мини-API с агентом

from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI(title="Мини-Инспектор")


class AppRequest(BaseModel):
    text: str


def _check(text: str) -> dict:
    errors = []
    for f in ["название", "количество"]:
        if f not in text.lower():
            errors.append(f)
    return {"ok": len(errors) == 0, "errors": errors}


@app.get("/health")
def health():
    return {"status": "ok", "version": "1.0"}


@app.post("/check")
def check(req: AppRequest):
    res = _check(req.text)
    return {
        "passed": res["ok"],
        "errors": res["errors"],
        "message": "Полная" if res["ok"] else f"Неполная: {res['errors']}",
    }


@app.post("/process")
def process(req: AppRequest):
    res = _check(req.text)
    if not res["ok"]:
        return {
            "registered": False,
            "errors": res["errors"],
            "message": f"Отказано. Отсутствует: {res['errors']}",
        }
    num = random.randint(1000, 9999)
    return {
        "registered": True,
        "number": num,
        "message": f"Заявка зарегистрирована под номером \u2116{num}",
    }
