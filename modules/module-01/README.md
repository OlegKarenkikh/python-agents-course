# Модуль 1: Python Основы 🐍

> **Время:** ~4 часа | **Уровень:** начальный

## Чему вы научитесь

- Переменные, типы данных, строки
- Списки и словари
- Условия и циклы
- Функции и классы

---

## 📦 Часть 1: Переменные и данные

![Типы данных Python](https://user-gen-media-assets.s3.amazonaws.com/gemini_images/e93db065-8083-4f0f-bd7d-c12fef76b43d.png)

```python
имя = "Алексей"   # str
возраст = 25         # int
учеба = True          # bool
print(type(возраст))   # <class 'int'>
```

---

## 📊 Часть 2: Списки и Словари

```python
чек = ["Название", "Количество", "Дата"]
заявка = {"название": "Закупка", "количество": 5}
```

---

## 🔀 Часть 3: Условия и циклы

```python
if заявка["количество"] > 0:
    print("Полная!")
for п в чек:
    print(f"  ✓ {п}")
```

---

## 🔧 Часть 4: Функции

```python
def check(text: str) -> dict:
    """Проверяет заявку."""
    errors = []
    if "название" not in text.lower():
        errors.append("Нет названия")
    return {"passed": not errors, "errors": errors}
```

---

## 🏗️ Часть 5: Классы

```python
class Инспектор:
    def __init__(self, name):
        self.name = name
        self.count = 0
    def run(self, text):
        self.count += 1
        return f"[{self.name}] #{self.count}: {check(text)}"
```

---

## 📝 Практика

[`practice/`](practice/)

## ✅ Чек-лист

- [ ] Переменные всех типов
- [ ] Список и словарь
- [ ] Функция с def
- [ ] Простой класс

**Следующий:** [Модуль 2 →](../module-02/README.md)
