# 241-327_Zelyonkin

Лабораторные работы по дисциплине «Архитектура и дизайн ПО».

## Структура репозитория

- `lab1/` — лабораторная работа №1: Django REST API, PostgreSQL, CRUD+List.
- `lab2/` — лабораторная работа №2: Docker Compose, PostgreSQL, Gunicorn, Nginx, HTTP/HTTPS.
- `venv/` — локальное виртуальное окружение, не добавляется в Git.

## Лабораторная работа №1

Запуск локально:

```bash
source venv/bin/activate
python lab1/backend/manage.py migrate
python lab1/backend/fill_clubs.py --count 150 --reset
python lab1/backend/manage.py runserver