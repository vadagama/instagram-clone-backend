import random
import shutil
import string
from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Depends, status, UploadFile, File
from typing import List
from sqlalchemy.orm.session import Session
from auth.oauth2 import get_current_user
from routers.schemas import PostDisplay, CommentBase, UserAuth
from db.database import get_db
from db import db_comment

router = APIRouter(
    prefix='/comment',
    tags=['comment']
)

@router.post('')
def create_comment(request: CommentBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_comment.create_comment(db, request)


@router.get('/all/{post_id}')
def get_comments(post_id: int, db: Session = Depends(get_db)):
    return db_comment.get_all(db, post_id)

# Delete post
@router.delete("/{id}")
def delete_comment():
    pass
# def delete_post(
#     id: int,
#     db: Session = Depends(get_db),
#     current_user: UserAuth = Depends(get_current_user),
# ):
#     return db_post.delete_post(db, id, current_user.id)
    