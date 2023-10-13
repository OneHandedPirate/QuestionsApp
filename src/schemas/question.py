from datetime import datetime

from pydantic import BaseModel, Field


class QuestionSchema(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime


class QuestionRequest(BaseModel):
    questions_num: int = Field(description="Number of questions", example=10)
