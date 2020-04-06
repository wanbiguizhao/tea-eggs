
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
from enum import Enum
_project_root = str(pathlib.Path(__file__).resolve().parents[2])
sys.path.append(_project_root)
from storage.database import Base
from storage.database import SessionLocal
from storage.osUser.schemas import TaskStatusEnum





class AbstractTask(Base):
    __abstract__ = True

    uuid = Column(String(32),unique=True ,index=True )
    create_datetime=Column(DateTime, default=datetime.now)
    last_updatime=Column(DateTime, default=datetime.now, onupdate=datetime.now)
    status=Column(Enum(TaskStatusEnum),server_default=TaskStatusEnum.init, nullable=False)
    error_count=Column(Integer,default=0)

    def save(self):
        try:
            db = SessionLocal()
            db.add(self)
            db.commit()
            db.refresh(self)
        except Exception as e:
            print(e)
        finally:
            db.close()

    def set_status(self, status_value: TaskStatusEnum ):
        self.status=status_value
    def __repr__(self):
        return "type:{__tablename__}-id:{id}-host:{host}-username:{username}-status:{status}-{last_updatime}".format(**self.__dict__)

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
