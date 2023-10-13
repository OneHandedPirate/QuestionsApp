from functools import wraps

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from src.db.models import Question
from src.db.session import get_async_session


class QuestionDBRepository:
    def __init__(self, session: AsyncSession = Depends(get_async_session)) -> None:
        self.session = session

    @staticmethod
    def handle_exceptions(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except SQLAlchemyError as e:
                print(e)

        return wrapper

    @handle_exceptions
    async def get_last_question(self):
        """get the last question from database"""

        stmt = select(Question).order_by(Question.question_id.desc()).limit(1)
        last_question = await self.session.scalar(stmt)

        return last_question if last_question else {}

    @handle_exceptions
    async def filter_duplicated_questions(self, questions: list):
        """filter questions from API"""

        stmt = select(Question).where(Question.id.in_(question.id for question in questions))
        existing_question_ids = [question.id for question in (await self.session.execute(stmt)).scalars().fetchall()]
        new_questions = list(filter(lambda question: question.id not in existing_question_ids, questions))

        return new_questions

    @handle_exceptions
    async def dump_questions(self, questions: list):
        """save a list of questions to the database"""

        self.session.add_all(questions)
        await self.session.commit()
