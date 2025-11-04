from fastapi import APIRouter, status, Response
from typing import Optional

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


@router.get("/{id}/comment/{comment_id}", tags = ['blog', 'comment'])
def blog_with_comments(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {"message": f"Blog_id {id}, comment {comment_id}, valid {valid} of username {username}"}


@router.get("/all")
def get_all_blogs(page = 2, page_size: Optional[int] = None):
    return {"message": f"All {page_size} blogs in blog {page}"}


@router.get("/{id}", status_code=200)
def get_blogs(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f"Blog with id {id} not found"}
    
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": f"A blog with id {id}"}