
# -*- coding: utf-8 -*-
'''
    desc: 数据库操作。
    author: liukun
    date: 2020-04-05
'''
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import Sequence


import pathlib
import sys
import yaml
_project_root = str(pathlib.Path(__file__).resolve().parents[2])
sys.path.append(_project_root)
from web_server.usersapp.database import Base


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
    task_status = Column(String)
    #create_datetime=
    #last_updatime=
    #status=[init,process,failture,sucess,]
    #error_count=0
    # 


