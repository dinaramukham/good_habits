# good habit

Этот проект представляет собой пример приложения, использующего Docker для контейнеризации, Django REST Framework для создания API, Celery для асинхронной обработки задач и Crontab для периодических задач.

## Установка

Для запуска проекта вам понадобится установленный Docker и Docker Compose.

1. Склонируйте репозиторий:

git clone https://github.com/dinaramukham/good_habits
cd your_project

2. Запустите контейнеры с помощью Docker Compose:
 docker-compose up --build

3. Примените миграции Django:
docker-compose exec web python manage.py migrate
