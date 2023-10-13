from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Question(Base):
    __tablename__ = 'question'

    question_id = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(Integer)
    question = Column(String)
    answer = Column(String)
    created_at = Column(DateTime(timezone=True))
