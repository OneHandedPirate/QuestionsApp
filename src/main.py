from typing import Union

from fastapi import Depends, FastAPI

from src.schemas.question import QuestionRequest, QuestionSchema
from src.services.question import QuestionService

app = FastAPI(
    title='Questions App',
    summary='Question App with the only one endpoint',
)


@app.post('/', response_model=Union[QuestionSchema, dict], tags=['Questions'])
async def post_questions(
    questions: QuestionRequest,
    question_service: QuestionService = Depends(),
):
    """Endpoint to get questions from open API and pass them to DB"""

    return await question_service.post_questions(questions)
