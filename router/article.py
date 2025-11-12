from fastapi import APIRouter, Depends
from db import db_article
from db.database import get_db
from schemas import ArticleBase, ArticleDisplay
from sqlalchemy.orm import Session
from auth.oauth2 import oauth2_schema

router = APIRouter(
    prefix='/article',
    tags=['article']
)

# create article
@router.post("/create", response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)


# get specific article
@router.get("/{id}", response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_schema)):
    return db_article.get_article(db, id)