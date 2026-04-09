# Модуль 7: Продвинутый 🚀

> **Время:** ~6 часов | **Уровень:** продвинутый

## Чему вы научитесь

- Как заставить несколько агентов работать вместе
- Мониторинг агентов
- Обработка ошибок и оптимизация

---

## 👥 Система агентов

![Три агента работают параллельно](https://user-gen-media-assets.s3.amazonaws.com/gemini_images/2ea386be-4ebd-4bb6-9430-9e1ec0e37658.png)

В `dzo-tz-agents` работают **три агента** параллельно:

```
FastAPI
├── /process/dzo    → [Агент ДЗО]
├── /process/tz     → [Агент ТЗ]
└── /process/tender → [Агент Тендер]
```

---

## 🏗️ Полная архитектура

![Архитектура реального проекта dzo-tz-agents](https://user-gen-media-assets.s3.amazonaws.com/gemini_images/2ebe2099-993b-4ab1-8855-9c9f9d06dfeb.png)

---

## 📊 Мониторинг

```python
from prometheus_client import Counter

requests_total = Counter(
    "agent_requests_total", "Тотал запросов",
    ["agent", "status"]
)
requests_total.labels(agent="dzo", status="success").inc()
```

---

## 📝 Практика

[`practice/`](practice/)

## ✅ Чек-лист

- [ ] Создал двух агентов (ДЗО + ТЗ)
- [ ] Организовал роутинг между ними
- [ ] Понял, как работает реальный `dzo-tz-agents`

---

🎉 **Поздравляем! Вы прошли весь курс!**

Теперь вы знаете, как устроен реальный [dzo-tz-agents](https://github.com/OlegKarenkikh/dzo-tz-agents)!
