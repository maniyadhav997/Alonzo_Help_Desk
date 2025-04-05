from pydantic import BaseModel, EmailStr
from typing import List
from uuid import UUID

class User(BaseModel):
    email: EmailStr
    favorite_questions: List[UUID] = []
    favorite_answers: List[UUID] = []
