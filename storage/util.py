
# -*- coding: utf-8 -*-
'''
    desc: 数据库常用操作
    author: liukun
    date: 2020-04-19
'''

import pathlib
import sys
import yaml
_project_root = str(pathlib.Path(__file__).resolve().parents[2])
sys.path.append(_project_root)
from storage.database import get_db,SessionLocal
from storage.basicModel import  AbstractTask ,TaskStatusEnum
from sqlalchemy import or_ , and_
from datetime import timedelta , datetime
from fastapi.params import Depends
from sqlalchemy.orm import Session

def get_undo_task(self, task_type_name : type)->list :
    """
    [
        task_type_name 是storage.models定义的数据库模型
        主要逻辑,根据task_type_name 从数据库中获得要执行的任务,任务队列
    ]

    Arguments:
        task_type_name {type} -- [description]

    Returns:
        list -- [description]
    """
    if not issubclass(AbstractTask,task_type_name):
        # todo 报告一次异常.
        return []
    query_result_list=[]
    try:
        db = SessionLocal()
        obj=db.query(task_type_name).filter(
        or_(
            task_type_name.status == TaskStatusEnum.init,
            and_(task_type_name.status == TaskStatusEnum.processing , task_type_name.last_updatime + timedelta(seconds=120) < datetime.now() )
            )
        ).first()
        if obj is not None:
            query_result_list=[obj]
    except Exception as e:
        print(e)
    finally :
        db.close()
    return query_result_list
