# Шпаргалка: FastAPI

## Минимальный сервер

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str

@app.get("/health")
def health(): return {"status": "ok"}

@app.post("/process")
def process(item: Item): return {"result": item.text.upper()}
```

## Запуск

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
# Swagger: http://localhost:8000/docs
```

## Ответы

```python
from fastapi import HTTPException

@app.get("/item/{id}")
def get_item(id: int):
    if id < 0:
        raise HTTPException(status_code=404, detail="Не найдено")
    return {"id": id}
```

## HTTP-методы

| Метод | Назначение |
|---|---|
| `GET` | Получить данные |
| `POST` | Отправить данные |
| `PUT` | Обновить |
| `DELETE` | Удалить |
