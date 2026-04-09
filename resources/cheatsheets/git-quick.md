# Шпаргалка: Git

## Начало работы

```bash
git clone https://github.com/user/repo  # скопировать репо
git status                               # что изменилось?
git log --oneline                        # история коммитов
```

## Сохранить изменения

```bash
git add .              # добавить все изменения
git commit -m "описание"  # сохранить с комментарием
git push               # отправить на GitHub
```

## Ветки

```bash
git checkout -b new-feature  # создать ветку
git checkout main            # вернуться на main
git merge new-feature        # слить ветку
```
