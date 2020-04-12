
# -*- coding: utf-8 -*-
'''
    desc: 数据库操作。
    author: liukun
    date: 2020-04-05
'''
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String , DateTime ,Enum
from sqlalchemy.orm import relationship
from sqlalchemy import Sequence


from datetime import datetime
import pathlib
import sys
import yaml
_project_root = str(pathlib.Path(__file__).resolve().parents[2])
sys.path.append(_project_root)
from storage.database import Base
from storage.database import SessionLocal
from storage.osUser.schemas import TaskStatusEnum
from storage.basicModel import AbstractTask

class LockUserTask(AbstractTask):

    __tablename__ = "lockUserTask"
    id = Column(Integer, Sequence('lock_user_task_id_seq'),primary_key=True, index=True)

    host = Column(String)
    username = Column(String)



class UNLockUserTask(AbstractTask):
    
    __tablename__ = "unLockUserTask"
    id = Column(Integer, Sequence('unlock_user_task_id_seq'),primary_key=True, index=True)
    host = Column(String)
    username = Column(String)
