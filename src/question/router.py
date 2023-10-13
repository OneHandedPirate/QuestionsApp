from typing import Union

from fastapi import APIRouter, Depends, status

from src.question.schemas import QuestionRequest, QuestionSchema
from src.question.services import QuestionService

router = APIRouter(
    prefix='/questions',
    tags=['Question']
)


@router.post(
    '',
    response_model=Union[QuestionSchema, dict],
    status_code=status.HTTP_201_CREATED
)
async def post_questions(
    questions: QuestionRequest,
    question_service: QuestionService = Depends(),
):
    """Endpoint to get questions from open API and pass them to DB"""

    return await question_service.post_questions(questions)
