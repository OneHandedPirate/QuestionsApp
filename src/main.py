from fastapi import FastAPI

from src.question.router import router as question_router

app = FastAPI(
    title='Questions App',
    summary='Question App with the only one endpoint',
)

app.include_router(question_router)
