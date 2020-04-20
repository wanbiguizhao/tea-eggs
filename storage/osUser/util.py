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
from storage.osUser import crud, models, schemas
from storage.database import get_db,SessionLocal
from sqlalchemy import or_ , and_
from datetime import timedelta , datetime
from fastapi.params import Depends
from sqlalchemy.orm import Session





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

def get_undo_unlock_user_tasks():
    query_result_list=[]
    try:
        db = SessionLocal()
        obj=db.query(models.UNLockUserTask).filter(
        or_(
            models.UNLockUserTask.status == schemas.TaskStatusEnum.init,
            and_(models.UNLockUserTask.status == schemas.TaskStatusEnum.processing , models.UNLockUserTask.last_updatime + timedelta(seconds=120) < datetime.now() )
            )
        ).first()
        if obj is not None:
            query_result_list=[obj]
    except Exception as e:
        print(e)
    finally :
        db.close()
    return query_result_list

def get_undo_add_sudo_tasks():
    query_result_list=[]
    try:
        db = SessionLocal()
        obj=db.query(models.AddSudoTask).filter(
        or_(
            models.AddSudoTask.status == schemas.TaskStatusEnum.init,
            and_(models.AddSudoTask.status == schemas.TaskStatusEnum.processing , models.AddSudoTask.last_updatime + timedelta(seconds=120) < datetime.now() )
            )
        ).first()
        if obj is not None:
            query_result_list=[obj]
    except Exception as e:
        print(e)
    finally :
        db.close()
    return query_result_list

def get_undo_add_user_tasks():
    query_result_list=[]
    try:
        db = SessionLocal()
        obj=db.query(models.AddUserTask).filter(
        or_(
            models.AddUserTask.status == schemas.TaskStatusEnum.init,
            and_(models.AddUserTask.status == schemas.TaskStatusEnum.processing , models.AddUserTask.last_updatime + timedelta(seconds=120) < datetime.now() )
            )
        ).first()
        if obj is not None:
            query_result_list=[obj]
    except Exception as e:
        print(e)
    finally :
        db.close()
    return query_result_list

def get_undo_change_password_tasks():
    query_result_list=[]
    try:
        db = SessionLocal()
        obj=db.query(models.ChangePasswordTask).filter(
        or_(
            models.ChangePasswordTask.status == schemas.TaskStatusEnum.init,
            and_(models.ChangePasswordTask.status == schemas.TaskStatusEnum.processing , models.ChangePasswordTask.last_updatime + timedelta(seconds=120) < datetime.now() )
            )
        ).first()
        if obj is not None:
            query_result_list=[obj]
    except Exception as e:
        print(e)
    finally :
        db.close()
    return query_result_list

def get_undo_add_publickey_tasks():
    query_result_list=[]
    try:
        db = SessionLocal()
        obj=db.query(models.AddPublickeyTask).filter(
        or_(
            models.AddPublickeyTask.status == schemas.TaskStatusEnum.init,
            and_(models.AddPublickeyTask.status == schemas.TaskStatusEnum.processing , models.AddPublickeyTask.last_updatime + timedelta(seconds=120) < datetime.now() )
            )
        ).first()
        if obj is not None:
            query_result_list=[obj]
    except Exception as e:
        print(e)
    finally :
        db.close()
    return query_result_list

def get_undo_add_group_tasks():
    query_result_list=[]
    try:
        db = SessionLocal()
        obj=db.query(models.AddGroupTask).filter(
        or_(
            models.AddGroupTask.status == schemas.TaskStatusEnum.init,
            and_(models.AddGroupTask.status == schemas.TaskStatusEnum.processing , models.AddGroupTask.last_updatime + timedelta(seconds=120) < datetime.now() )
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
