# Лабораторная работа №1. Трехуровневая клиент-серверная архитектура

Проект реализован на `Django` и `Django REST Framework`. Предметная область: футбольные клубы.

## Что уже покрыто

- Django-проект и приложение с моделью предметной области.
- REST API для `CRUD + List`.
- Миграции для модели данных.
- Админка Django.
- Скрипт и management command для генерации `100+` тестовых записей.
- Поддержка `PostgreSQL` через переменные окружения.
- Безопасный fallback на `SQLite` для локального запуска и тестов.
- Примеры REST-запросов в [lab1/api.http](/home/skre4karta/lesson/architecture/lab1/api.http).
- CRUD-тесты API.

## Структура

- `lab1/` - Django-проект.
- `lab1/gor4eret/models.py` - модель `FootballClub`.
- `lab1/gor4eret/serializers.py` - сериализация в JSON.
- `lab1/gor4eret/views.py` - API на `ModelViewSet`.
- `lab1/lab1/urls.py` - маршруты `admin/` и `api/`.
- `lab1/gor4eret/management/commands/seed_football_clubs.py` - генерация тестовых данных.
- `fill_clubs.py` - удобный запуск генерации из корня проекта.

## Быстрый запуск

```bash
cd /home/skre4karta/lesson/architecture
source venv/bin/activate
python lab1/manage.py migrate
python fill_clubs.py --count 150 --reset
python lab1/manage.py runserver 8000
```

Если нужно работать именно с `PostgreSQL`, заполните переменные из [lab1/.env.example](/home/skre4karta/lesson/architecture/lab1/.env.example) в окружении перед запуском.

## Что показать на защите

- Запуск сервера: `python lab1/manage.py runserver 8000`
- Применение миграций: `python lab1/manage.py migrate`
- Генерацию данных: `python fill_clubs.py --count 150 --reset`
- CRUD-запросы из REST-клиента по адресам `/api/football-clubs/` и `/api/football-clubs/<id>/`
- Работу ORM и содержимое БД в pgAdmin или DBeaver

## Что остается сделать вручную

- Разместить проект в публичном `GitHub/GitLab`-репозитории с корректным именем по шаблону преподавателя.
- Убедиться, что локальный `PostgreSQL` поднят и переменные окружения заданы перед демонстрацией.
- При необходимости создать/переcоздать администратора командой `python lab1/manage.py createsuperuser`.
