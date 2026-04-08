# 📄 Шпаргалка: Python для новичков

## Переменные
```python
name = "Olga"          # строка
age = 25               # число
is_student = True      # булевое значение
```

## Функции
```python
def greet(name: str) -> str:
    return f"Привет, {name}!"

result = greet("Anna")  # Привет, Anna!
```

## Списки и словари
```python
tools = ["search", "read", "write"]  # список
config = {"model": "gpt-4o", "temp": 0.2}  # словарь
```

## Классы
```python
class Agent:
    def __init__(self, name: str):
        self.name = name
    
    def think(self, task: str) -> str:
        return f"{self.name} думает над: {task}"
```

## f-строки
```python
model = "gpt-4o"
print(f"Используется модель: {model}")
```

## Ошибки
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Нельзя делить на 0!")
```
