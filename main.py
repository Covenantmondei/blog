from fastapi import FastAPI
from router import article, blog_get, blog_post, user
from db import models
from db.database import engine

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)

@app.get("/")
def index():
    return {"message": "Covenant Monday on Fastapi"}


models.Base.metadata.create_all(engine)