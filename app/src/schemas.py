from pydantic import BaseModel, Field
from typing import Optional


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    due_date: Optional[str] = Field(None, example="2025-12-31")


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    due_date: Optional[str] = None
    status: Optional[str] = Field(None, example="completed")


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    due_date: Optional[str]
    status: str
