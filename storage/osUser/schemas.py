# -*- coding: utf-8 -*-
'''
    desc: 数据库操作。
    author: liukun
    date: 2020-04-05
'''

from typing import List
from pydantic import BaseModel
from enum import Enum
from pydantic.schema import datetime
from storage.basicModel import TaskStatusEnum





class LockUserTaskBase(BaseModel):
    host: str
    username: str 


class LockUserTaskCreate(LockUserTaskBase):
    pass

class LockUserTask(LockUserTaskBase):
    id: int
    uuid: str
    status : TaskStatusEnum
    create_datetime : datetime 
    last_updatime : datetime
    class Config:
        orm_mode = True

class UNLockUserTask(LockUserTask):

    class Config:
        orm_mode = True

#添加sudo权限

class AddSudoTaskBase(BaseModel):
    host: str
    username: str

class AddSudoTaskCreate(AddSudoTaskBase):
    pass

class AddSudoTask(AddSudoTaskBase):
    id: int
    uuid: str
    status : TaskStatusEnum
    create_datetime : datetime
    last_updatime : datetime
    class Config:
        orm_mode = True

#增加用户

class AddUserTaskBase(BaseModel):
    host: str
    username: str
    password: str
    publickey: str

class AddUserTaskCreate(AddUserTaskBase):
    pass

class AddUserTask(AddUserTaskBase):
    id: int
    uuid: str
    status : TaskStatusEnum
    create_datetime : datetime
    last_updatime : datetime
    class Config:
        orm_mode = True

#修改用户密码

class ChangePasswordTaskBase(BaseModel):
    host: str
    username: str
    password: str

class ChangePasswordTaskCreate(ChangePasswordTaskBase):
    pass

class ChangePasswordTask(ChangePasswordTaskBase):
    id: int
    uuid: str
    status : TaskStatusEnum
    create_datetime : datetime
    last_updatime : datetime
    class Config:
        orm_mode = True

#增加公钥

class AddPublickeyTaskBase(BaseModel):
    host: str
    username: str
    publickey: str

class AddPublickeyTaskCreate(AddPublickeyTaskBase):
    pass

class AddPublickeyTask(AddPublickeyTaskBase):
    id: int
    uuid: str
    status : TaskStatusEnum
    create_datetime : datetime
    last_updatime : datetime
    class Config:
        orm_mode = True

#添加用户组

class AddGroupTaskBase(BaseModel):
    host: str
    username: str
    groupname: str

class AddGroupTaskCreate(AddGroupTaskBase):
    pass

class AddGroupTask(AddGroupTaskBase):
    id: int
    uuid: str
    status : TaskStatusEnum
    create_datetime : datetime
    last_updatime : datetime
    class Config:
        orm_mode = True


 

