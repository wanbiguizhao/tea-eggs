

# -*- coding: utf-8 -*-
'''
    desc: 数据库操作。
    author: liukun
    date: 2020-04-11
'''

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String , DateTime ,Enum
from sqlalchemy.orm import relationship
from sqlalchemy import Sequence
import  enum
import pathlib
import sys
_project_root = str(pathlib.Path(__file__).resolve().parents[1])
sys.path.append(_project_root)
from storage.database import Base
from storage.database import SessionLocal

from datetime import datetime


class TaskStatusEnum(str, enum.Enum):
    init = "init" #
    processing = "processing" # 
    sucess = "sucess" # 成功
    failure = 'failure' #

class AbstractTask(Base):
    __abstract__ = True

    uuid = Column(String(32),unique=True ,index=True )
    create_datetime=Column(DateTime, default=datetime.now)
    last_updatime=Column(DateTime, default=datetime.now, onupdate=datetime.now)
    status=Column( Enum(TaskStatusEnum),server_default=TaskStatusEnum.init, nullable=False)
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
        return "id:{id}-host:{host}-username:{username}-status:{status}-{last_updatime}".format(**self.__dict__)