# Question App
Simple FastAPI app with only one endpoint

### Требования:
- установленный docker/docker-compose


### Установка

- стянуть репозиторий:<br>
    `git clone https://github.com/OneHandedPirate/QuestionsApp.git`
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

### Запуск:
- выполнить команду `make up`, которая поднимет `docker-compose-dev.yaml` c FastAPI-приложением и базой данных в detached-режиме.

### Описание эндпоинтов:
- `/questions` метод: `POST`<br>Основной и единственный эндпоинт. Принимает объект вида `{"questions_num": int}`, где `int` - целое число вопросов, которые будут записаны в БД.<br>Ответ:<br>`{}` - в случае, если база данных пуста перед запросом;<br> `{"id": int, "question": string, "answer": string, "created_at": datetime}` - объект последнего вопроса, записанного в БД перед запросом;


### Пример запроса и ответа:
- При пустой БД:

![empty_bd.png](images%2Fempty_bd.png)

- При не пустой БД:

![not_empty_db.png](images%2Fnot_empty_db.png)
