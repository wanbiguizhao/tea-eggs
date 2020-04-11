
# -*- coding: utf-8 -*-
'''
    desc: 数据库操作。
    author: liukun
    date: 2020-04-08
'''
import sys
import pathlib
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
_project_root = str(pathlib.Path(__file__).resolve().parents[1])
sys.path.append(_project_root)
from config import config
db_name = config['sqlite']['db_name']

SQLALCHEMY_DATABASE_URL = "sqlite:///"+_project_root+'/'+db_name
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
