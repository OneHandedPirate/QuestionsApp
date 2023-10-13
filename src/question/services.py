from fastapi import Depends

from src.question.models import Question
from src.question.schemas import QuestionRequest, QuestionSchema
from src.question.sqlalch import QuestionDBRepository
from src.utils import get_questions


class QuestionService:
    def __init__(self, db_repo: QuestionDBRepository = Depends()):
        self.db_repo = db_repo

    async def post_questions(self, questions: QuestionRequest):
        last_question: QuestionSchema | dict = await self.db_repo.get_last_question()

        questions_list: list = await get_questions(
            questions.model_dump().get('questions_num'),
        )

        questions_to_db: list = []

        while True:
            question_schemas: list = [
                QuestionSchema(**question) for question in questions_list
            ]
            new_questions: list = await self.db_repo.filter_duplicated_questions(
                question_schemas,
            )
            duplicated_count: int = len(question_schemas) - len(new_questions)
            questions_to_db.extend(
                [Question(**question.model_dump()) for question in new_questions],
            )

            if duplicated_count:
                print(f'Duplicated questions: {duplicated_count}')
                questions_list = await get_questions(duplicated_count)
            else:
                break

        await self.db_repo.dump_questions(questions_to_db)

        return last_question
