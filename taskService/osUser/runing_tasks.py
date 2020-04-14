# -*- coding: utf-8 -*-
'''
    desc: 用户任务后台处理模块
    author: liukun
    date: 2020-04-04
'''

import pathlib
import sys
import os
import yaml
_project_root = str(pathlib.Path(__file__).resolve().parents[2])
sys.path.append(_project_root)
from storage.osUser.util import get_undo_lock_user_tasks, get_undo_unlock_user_tasks
from storage.osUser.schemas import TaskStatusEnum
from taskService.osUser import lock_user , unlock_user

from datetime import datetime
import time



def run_lock_user_tasks():
    try:
        task_list=get_undo_lock_user_tasks()
        print(datetime.now(),'->',len(task_list),'lock_user_tasks')
        for task in task_list:
            if task.status == TaskStatusEnum.init:
                task.set_status(TaskStatusEnum.processing)
                task.save()
            yaml_save_path=datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')+'lock_user.yaml'
            task.host,
            result=lock_user.run_task_yaml(task,yaml_save_path)
            if result:
                task.set_status(TaskStatusEnum.sucess)
            else:
                task.error_count=task.error_count+1
                if task.error_count>=5:
                    task.set_status(TaskStatusEnum.failure)
            task.save()
    except Exception as identifier:
        print(identifier)

def run_unlock_user_tasks():
    try:
        task_list=get_undo_unlock_user_tasks()
        print(datetime.now(),'->',len(task_list),'unlock_user_tasks')
        for task in task_list:
            if task.status == TaskStatusEnum.init:
                task.set_status(TaskStatusEnum.processing)
                task.save()
            yaml_save_path=datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')+'unlock_user.yaml'
            task.host,
            result=unlock_user.run_task_yaml(task,yaml_save_path)
            if result:
                task.set_status(TaskStatusEnum.sucess)
            else:
                task.error_count=task.error_count+1
                if task.error_count>=5:
                    task.set_status(TaskStatusEnum.failure)
            task.save()
    except Exception as identifier:
        print(identifier)



task_list=[run_lock_user_tasks,run_unlock_user_tasks]
def run_all_task():
    while True:
        for func in task_list:
            func()
        time.sleep(10)


if __name__ == "__main__":
    run_all_task()









