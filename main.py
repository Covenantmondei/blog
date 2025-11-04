from fastapi import FastAPI
from router import blog_get, blog_post

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get("/")
def index():
    return {"message": "Covenant Monday on Fastapi"}

# @app.get("/blog/all")
# def get_all_blogs(page, page_size):
#     return {"message": f"All {page_size} blogs in blog {page}"}

# @app.get("/blog/all")
# def get_all_blogs(page = 2, page_size = 8):
#     return {"message": f"All {page_size} blogs in blog {page}"}

# @app.get("/blog/{id}/comment/{comment_id}")
# def blog_with_comments(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
#     return {"message": f"Blog_id {id}, comment {comment_id}, valid {valid} of username {username}"}

