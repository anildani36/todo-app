from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class TodoCreateSchema(BaseModel):
    title: str = Field(min_length=1)
    description: Optional[str] = None
    priority: int = Field(ge=1, le=5, default=3)
    due_date: Optional[date] = None
