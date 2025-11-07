from typing import List
from fastapi import APIRouter, Depends
from db import db_user
from db.database import get_db
from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/user',
    tags=['user']
)

# create
@router.post("/create", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


# read
@router.get("/all", response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)


# read one user
@router.get("/{id}", response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db)):
    return db_user.get_user(db, id)

# update


# delete