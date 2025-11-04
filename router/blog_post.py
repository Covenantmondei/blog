from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class BlogModel(BaseModel):
    title: str
    content: str
    no_comment: int
    published: Optional[bool] = None

@router.post("/new/{id}")
def add_blog(blog: BlogModel, id: int, version: int = 1):
    return "ok"