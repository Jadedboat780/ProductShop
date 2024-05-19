# Бэкенд для магазина продуктов (находится в разработке)
Стек: fastapi, pydantic, sqlalchemy(psycopg2), alembic, fastapi-cache2(redis), poetry

## Структура проекта
* app - корневая папка бекенда
  * auth - реализацию аунтификации
  * db - содержит описание таблиц и производит подключение к базе данных
  * products - реализация эндпоинтов для товаров
  * tasks - фоновые задачи
  * users - реализация эндпоинтов для пользователя
  * config.py - конфигурационные переменные проекта
  * file.py - функции для работы с файлами
* files - папка для хранения файлов (в основном фотографий)
* migrations - папка с описанием миграций
* tests - папка с тестами
* .env - файл с переменными окружения
* main.py - сборка эндпоинтов и запуск бекенда
* pyproject.toml - файл с описанем зависимостей проекта

## Что ещё необходимо реализовать
1. [x] Работу с jwt access токеном
2. [ ] Работу jwt refresh токеном
3. [ ] Api rate limiting
4. [ ] Работу с Elasticsearch
5. [ ] Добавить тесты