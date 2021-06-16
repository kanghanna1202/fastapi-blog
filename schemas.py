from typing import Optional
from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    description: Optional[str] = None


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int

    class Config:
        orm_mode = True
