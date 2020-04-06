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
    status : TaskStatusEnum
    create_datetime : datetime 
    last_updatime : datetime
    class Config:
        orm_mode = True

class UNLockUserTask(LockUserTask):

    class Config:
        orm_mode = True
