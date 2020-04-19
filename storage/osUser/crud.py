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
from storage.osUser import models,schemas




def get_undo_lock_user_tasks(db: Session ):
    query_result_obj=db.query(models.LockUserTask).filter(
        or_(models.LockUserTask.status == models.TaskStatusEnum.init,
            and_(models.LockUserTask.status == models.TaskStatusEnum.processing , models.LockUserTask.last_updatime + timedelta(seconds=120) > datetime.now() )
            )
        ).first()
    return query_result_obj
    

def create_lock_user_task(db: Session, task:schemas.LockUserTaskCreate ):
    db_task = models.LockUserTask( uuid=uuid.uuid4().hex , host= task.host , username= task.username )
    db_task.save()
    return db_task

def get_lock_user_task(db: Session, task_id:int ):
    return db.query(models.LockUserTask).filter(models.LockUserTask.id == task_id ).first()

def create_unlock_user_task(db: Session, task:schemas.UNLockUserTask ):
    db_task = models.UNLockUserTask( uuid=uuid.uuid4().hex , host= task.host , username= task.username )
    db_task.save()
    return db_task

def get_unlock_user_task(db: Session, task_id:int ):
    return db.query(models.UNLockUserTask).filter(models.UNLockUserTask.id == task_id ).first()

def get_locks_task(db: Session,skip: int = 0, limit: int = 100):
    return db.query(models.LockUserTask).offset(skip).limit(limit).all()

def get_unlocks_task(db: Session,skip: int = 0, limit: int = 100):
    return db.query(models.UNLockUserTask).offset(skip).limit(limit).all()

###添加sudo权限###

def create_add_sudo_task(db: Session, task:schemas.AddSudoTaskCreate ):
    db_task = models.AddSudoTask( uuid=uuid.uuid4().hex , host= task.host , username= task.username )
    db_task.save()
    return db_task

def get_add_sudo_task(db: Session,skip: int = 0, limit: int = 100):
    return db.query(models.AddSudoTask).offset(skip).limit(limit).all()

###添加用户###

def create_add_user_task(db: Session, task:schemas.AddUserTaskCreate ):
    db_task = models.AddUserTask( uuid=uuid.uuid4().hex , host= task.host , username= task.username , password= task.password , publickey= task.publickey)
    db_task.save()
    return db_task


###修改用户密码###

def create_change_password_task(db: Session, task:schemas.ChangePasswordTaskCreate ):
    db_task = models.ChangePasswordTask( uuid=uuid.uuid4().hex , host= task.host , username= task.username , password= task.password)
    db_task.save()
    return db_task

###增加用户公钥###
def create_add_publickey_task(db: Session, task:schemas.AddPublickeyTaskCreate ):
    db_task = models.AddPublickeyTask( uuid=uuid.uuid4().hex , host= task.host , username= task.username ,  publickey= task.publickey)
    db_task.save()
    return db_task

###增加用户组###
def create_add_group_task(db: Session, task:schemas.AddGroupTaskCreate ):
    db_task = models.AddGroupTask( uuid=uuid.uuid4().hex , host= task.host , username= task.username ,  groupname= task.groupname)
    db_task.save()
    return db_task
