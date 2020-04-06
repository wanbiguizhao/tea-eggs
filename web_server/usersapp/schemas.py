# -*- coding: utf-8 -*-
'''
    desc: 数据库操作。
    author: liukun
    date: 2020-04-05
'''

from typing import List

from pydantic import BaseModel
from enum import Enum


class TaskStatusEnum(str, Enum):
    init = "init" #
    processing = "processing" # 
    sucess = "sucess" # 成功
    failure = 'failure' #


class LockUserTaskBase(BaseModel):
    host: str
    username: str 

class LockUserTaskCreate(LockUserTaskBase):
    pass

class LockUserTask(LockUserTaskBase):
    id: int
    uuid: str
    class Config:
        orm_mode = True

class ItemBase(BaseModel):
    title: str
    description: str = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True