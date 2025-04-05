from uuid import UUID
from pydantic import BaseModel
from typing import List
from datetime import datetime

class Question(BaseModel):
    id: UUID
    title: str
    content: str
    tags: List[str] =[]
    created_by: str
    created_at: datetime
    is_answerd: bool
    views: int
    answer_ids: List[UUID] =[]


