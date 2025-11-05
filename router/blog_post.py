from fastapi import APIRouter, Query, Body
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class Image(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title: str
    content: str
    no_comment: int
    published: Optional[bool] = None
    images: Optional[Image] = None

@router.post("/new/{id}")
def add_blog(blog: BlogModel, id: int, version: int = 1):
    return "ok"


@router.post("/new/{id}/comment")
def new_comment(blog: BlogModel, id: int, 
        comment_id: int = Query(
            None,
            title="A new comment for a blog",
            description="This is a description for the blog",
            alias="commentId"
        ),
        # content = Body('Hello, can we connect?'), #Ooptional
        # content = Body(...) # Makes it required
        content = Body(Ellipsis), # Makes it required
        v: Optional[List[str]] = Query(None)


    ):
    return {
        'blog': blog,
        'id': id,
        'comment_id': comment_id,
        'content': content,
        'version': v
    }


def required_functionality():
    return {"message": "Learning FastAPI is very important  "}