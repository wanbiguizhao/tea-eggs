
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
from web_server.usersapp.database import Base
from web_server.usersapp.database import SessionLocal
from web_server.usersapp.schemas import TaskStatusEnum


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")



class LockUserTask(Base):

    __tablename__ = "lockUserTask"
    id = Column(Integer, Sequence('lock_user_task_id_seq'),primary_key=True, index=True)
    uuid = Column(String(32),unique=True ,index=True )
    host = Column(String)
    username = Column(String)

    create_datetime=Column(DateTime, default=datetime.now)
    last_updatime=Column(DateTime, default=datetime.now, onupdate=datetime.now)
    status=Column(Enum(TaskStatusEnum),server_default=TaskStatusEnum.init, nullable=False)
    error_count=Column(Integer,default=0)


    def __repr__(self):
        return "id:{id}-host:{host}-username:{username}-status:{status}-{last_updatime}".format(**self.__dict__)
    
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


