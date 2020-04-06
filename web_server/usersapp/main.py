
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

from web_server.usersapp import crud, models, schemas
from web_server.usersapp.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.post("/users/task/lock", response_model= schemas.LockUserTask)
def lock_user(task: schemas.LockUserTaskCreate , db: Session = Depends(get_db) ):
    return crud.create_lock_user_task( db=db,task=task)

@app.get("/users/task/lock", response_model= schemas.LockUserTask)
def read_lock_user_task(task_id: int, db: Session = Depends(get_db)):
    db_task= crud.get_lock_user_task(db,task_id)
    return db_task


@app.post("/users/task/unlock", response_model= schemas.LockUserTask)
def unlock_user(task: schemas.LockUserTaskCreate , db: Session = Depends(get_db) ):
    return crud.create_unlock_user_task( db=db,task=task)

@app.get("/users/task/unlock", response_model= schemas.LockUserTask)
def read_unlock_user_task(task_id: int, db: Session = Depends(get_db)):
    db_task= crud.get_unlock_user_task(db,task_id)
    return db_task

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items