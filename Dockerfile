FROM python:3.11-slim

WORKDIR ./code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFRERED 1

COPY pyproject.toml .

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --only main

COPY . .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0"]
