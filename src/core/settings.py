import os

POSTGRES_USER: str | None = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD: str | None = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST: str | None = os.getenv('POSTGRES_HOST')
POSTGRES_PORT: str | None = os.getenv('POSTGRES_PORT')
POSTGRES_DB: str | None = os.getenv('POSTGRES_DB')

DATABASE_URL: str = (
    f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}'
    f'@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
)
