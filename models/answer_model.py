from uuid import UUID
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Answer(BaseModel):
    id: UUID
    question_id: UUID
    content: str
    created_by: str  
    created_at: datetime
    upvotes: int = 0
    is_accepted: bool = False
