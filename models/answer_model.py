from uuid import UUID
from pydantic import BaseModel
from typing import List
from datetime import datetime

class Answer(BaseModel):
    id: UUID
    quiestion_id: UUID
    content: str
    created_by: datetime
    is_answerd: bool
    upvotes: int =0
    is_accepted: bool = False