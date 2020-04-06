# -*- coding: utf-8 -*-
'''
    desc: 数据库常用操作
    author: liukun
    date: 2020-04-05
'''

import pathlib
import sys
import yaml
_project_root = str(pathlib.Path(__file__).resolve().parents[2])
sys.path.append(_project_root)
from web_server.usersapp import crud, models, schemas
from web_server.usersapp.database import SessionLocal, engine
from sqlalchemy import or_ , and_
from datetime import timedelta , datetime
from fastapi.params import Depends
from sqlalchemy.orm import Session


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def get_undo_lock_user_tasks():
    query_result_list=[]
    try:
        db = SessionLocal()
        obj=db.query(models.LockUserTask).filter(
        or_(
            models.LockUserTask.status == schemas.TaskStatusEnum.init,
            and_(models.LockUserTask.status == schemas.TaskStatusEnum.processing , models.LockUserTask.last_updatime + timedelta(seconds=120) < datetime.now() )
            )
        ).first()
        if obj is not None:
            query_result_list=[obj]
    except Exception as e:
        print(e)
    finally :
        db.close()
    return query_result_list

if __name__ == "__main__":
    x=get_undo_lock_user_tasks()
    print(x)