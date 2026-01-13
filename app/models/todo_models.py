from datetime import date
from typing import Optional

from pydantic import BaseModel, field_validator


class TodoItem(BaseModel):
    title: str
    description: Optional[str] = None
    priority: int
    due_date: Optional[date] = None
    is_completed: bool = False

    @field_validator('due_date', mode='before')
    @classmethod
    def empty_string_to_none(cls, v):
        # If the browser sends an empty string, convert it to None
        if v == "":
            return None
        return v
