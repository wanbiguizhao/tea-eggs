# -*- coding: utf-8 -*-
'''
    desc: 用户后台处理模块
    author: liukun
    date: 2020-04-04
'''

import pathlib
import sys
import os
import yaml
_project_root = str(pathlib.Path(__file__).resolve().parents[1])
sys.path.append(_project_root)
from web_server.usersapp.util import get_undo_lock_user_tasks
from web_server.usersapp.schemas import TaskStatusEnum
from usersModel import lock_user
from datetime import datetime
import time


def run_all_task():
    while True:
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
            pass
        time.sleep(10)


if __name__ == "__main__":
    run_all_task()









