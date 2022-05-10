from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from routers.schemas import UserDisplay, UserBase
from db.database import get_db
from db import db_user
from db.db_user import get_all

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

@router.get('/all')
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all(db)