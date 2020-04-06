# -*- coding: utf-8 -*-
'''
    desc: 数据库操作。
    author: liukun
    date: 2020-04-05
'''

from datetime import timedelta , datetime

from sqlalchemy.orm import Session
from sqlalchemy import or_ , and_
import uuid
import pathlib
import sys

_project_root = str(pathlib.Path(__file__).resolve().parents[2])
sys.path.append(_project_root)
from storage import models




def get_undo_lock_user_tasks(db: Session ):
    query_result_obj=db.query(models.LockUserTask).filter(
        or_(models.LockUserTask.status == models.TaskStatusEnum.init,
            and_(models.LockUserTask.status == models.TaskStatusEnum.processing , models.LockUserTask.last_updatime + timedelta(seconds=120) > datetime.now() )
            )
        ).first()
    return query_result_obj
    

def create_lock_user_task(db: Session, task:schemas.LockUserTaskCreate ):
    db_task = models.LockUserTask( uuid=uuid.uuid4().hex , host= task.host , username= task.username )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_lock_user_task(db: Session, task_id:int ):
    return db.query(models.LockUserTask).filter(models.LockUserTask.id == task_id ).first()

def create_unlock_user_task(db: Session, task:schemas.UNLockUserTask ):
    db_task = models.UNLockUserTask( uuid=uuid.uuid4().hex , host= task.host , username= task.username )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_unlock_user_task(db: Session, task_id:int ):
    return db.query(models.UNLockUserTask).filter(models.LockUserTask.id == task_id ).first()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
