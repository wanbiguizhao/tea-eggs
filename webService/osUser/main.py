
# -*- coding: utf-8 -*-
'''
    desc: 数据库操作。
    author: liukun
    date: 2020-04-05
'''

from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import pathlib
import sys
import yaml
_project_root = str(pathlib.Path(__file__).resolve().parents[2])
sys.path.append(_project_root)

from storage.database import engine ,get_db
from storage.osUser import crud, models, schemas

models.Base.metadata.create_all(bind=engine)

osUserApp = FastAPI(openapi_prefix="/osuser")

@osUserApp.get("/")
def read_root():
    return {"Hello": "World"}

@osUserApp.post("/task/lock", response_model= schemas.LockUserTask)
def lock_user(task: schemas.LockUserTaskCreate , db: Session = Depends(get_db) ):
    return crud.create_lock_user_task( db=db,task=task)

@osUserApp.get("/task/lock", response_model= schemas.LockUserTask)
def read_lock_user_task(task_id: int, db: Session = Depends(get_db)):
    db_task= crud.get_lock_user_task(db,task_id)
    return db_task

@osUserApp.get("/tast/get_lock_users",response_model= List[schemas.LockUserTask])
def read_locks_task(skip: int=0,limit: int=100,db: Session = Depends(get_db)):
    locks= crud.get_locks_task(db,skip=skip,limit=limit)
    return locks

@osUserApp.post("/task/unlock", response_model= schemas.UNLockUserTask)
def unlock_user(task: schemas.LockUserTaskCreate , db: Session = Depends(get_db) ):
    return crud.create_unlock_user_task( db=db,task=task)

@osUserApp.get("/task/unlock", response_model= schemas.UNLockUserTask)
def read_unlock_user_task(task_id: int, db: Session = Depends(get_db)):
    db_task= crud.get_unlock_user_task(db,task_id)
    print(db_task)
    return db_task

@osUserApp.get("/tast/get_unlocks_users",response_model= List[schemas.UNLockUserTask])
def read_unlocks_task(skip: int=0,limit: int=100,db: Session = Depends(get_db)):
    unlocks= crud.get_unlocks_task(db,skip=skip,limit=limit)
    return unlocks

@osUserApp.post("/tast/add_sudo_user",response_model= schemas.AddSudoTask)
def add_sudo(task: schemas.AddSudoTaskCreate , db: Session = Depends(get_db) ):
    return crud.create_add_sudo_task( db=db,task=task)

@osUserApp.get("/tast/get_sudo_users",response_model= List[schemas.AddSudoTask])
def read_sudo_users_task(skip: int=0,limit: int=100,db: Session = Depends(get_db)):
    sudo_users= crud.get_add_sudo_task(db,skip=skip,limit=limit)
    return sudo_users

@osUserApp.post("/tast/add_user",response_model= schemas.AddUserTask)
def add_user(task: schemas.AddUserTaskCreate , db: Session =  Depends(get_db)):
    return crud.create_add_user_task( db=db,task=task)

@osUserApp.post("/tast/change_user_password",response_model= schemas.ChangePasswordTask)
def change_password(task: schemas.ChangePasswordTaskCreate , db: Session =  Depends(get_db)):
    return crud.create_change_password_task( db=db,task=task)

@osUserApp.post("/tast/add_publickey",response_model= schemas.AddPublickeyTask)
def add_publickey(task: schemas.AddPublickeyTaskCreate , db: Session =  Depends(get_db)):
    return crud.create_add_publickey_task( db=db,task=task)

@osUserApp.post("/tast/add_group",response_model= schemas.AddGroupTask)
def add_group(task: schemas.AddGroupTaskCreate , db: Session =  Depends(get_db)):
    return crud.create_add_group_task( db=db,task=task)
