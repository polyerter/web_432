# Вируальное окружение

python -m venv .venv

переключаемся на него

# Настройка Django

скачиваем
```bash
pip install django
```

## начинаем новый проект

```bash
django-admin startproject app
```

```bash
cd app
```
## Запуск сервера
```bash
python manage.py runserver
```

## Применение миграций

```bash
python manage.py migrate
```

## Создание пользователя admin

```bash
python manage.py createsuperuser
```
## Создание приложения

```bash
python manage.py startapp hello
```