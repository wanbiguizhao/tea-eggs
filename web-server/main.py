# -*- coding: utf-8 -*-
'''
    desc: web接口模块
    author: liukun
    date: 2020-04-05
'''



import pathlib
import sys
import os
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
_project_root = str(pathlib.Path(__file__).resolve().parents[1])
sys.path.append(_project_root)

from usersModel import lock_user

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


app = FastAPI()


class LockUserTask(BaseModel):
    host: str
    username: str

class UnLockUserTask(LockUserTask):
    pass


# Don't do this in production!
@app.post("/task/user/lock", response_model=LockUserTask)
async def lock_user(*, task: LockUserTask):
    lock_user.run_task_yaml()
    return task

@app.post("/task/user/unlock", response_model=UnLockUserTask)
async def unlock(*, task: UnLockUserTask):
    return task