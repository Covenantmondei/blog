from fastapi import FastAPI
from auth import authentication
from router import article, blog_get, blog_post, user, product
from db import models
from db.database import engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(authentication.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)


@app.get("/")
def index():
    return {"message": "Covenant Monday on Fastapi"}


models.Base.metadata.create_all(engine)

origins = ['localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)