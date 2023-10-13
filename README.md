# Question App
Simple app with only one endpoint

### Требования:
- установленный docker/docker-compose


### Установка/запуск

- стянуть репозиторий:<br>
    `git clone ссылка будет позже`
- перейти в папку проекта:<br>
    `cd QuestionsApp`
- выполнить команду `make create_env`, которая создаст в папке проекта файл `.env` со следующим набором переменных:<br>
    `POSTGRES_USER=postgres`<br>
    `POSTGRES_PASSWORD=postgres`<br>
    `POSTGRES_DB=postgres`<br>
    `POSTGRES_PORT=5432`<br>
    `POSTGRES_HOST=db`<br>
    `APP_PORT=8000`<br>
    - Можно оставить их так. По умолчанию после поднятия docker-compose приложение будет висеть на `8000` порту. Для изменения порта приложения нужно изменить `APP_PORT` в файле `.env`
- выполнить команду `make up`, которая поднимет `docker-compose-dev.yaml` c FastAPI-приложением и базой данных в detached-режиме.

### Пример запроса:
