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
import storage.osUser.util 
from storage.osUser.schemas import TaskStatusEnum
from taskService.osUser import os_user_tasks
from datetime import datetime
import time
from config import YAML_PATH,BECOME_PASS


def run_lock_user_tasks():
    try:
        task_list=storage.osUser.util.get_undo_lock_user_tasks()
        print(datetime.now(),'->',len(task_list),'lock_user_tasks')
        for task in task_list:
            if task.status == TaskStatusEnum.init:
                task.set_status(TaskStatusEnum.processing)
                task.save()
            yaml_save_path=YAML_PATH+datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')+'_lock_user.yaml'
            task.host,
            runtime_task=os_user_tasks.ansibleLockUserTask(BECOME_PASS,yaml_save_path)
            result=runtime_task.run(task)
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
        task_list=storage.osUser.util.get_undo_unlock_user_tasks()
        print(datetime.now(),'->',len(task_list),'unlock_user_tasks')
        for task in task_list:
            if task.status == TaskStatusEnum.init:
                task.set_status(TaskStatusEnum.processing)
                task.save()
            yaml_save_path=YAML_PATH+datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')+'_unlock_user.yaml'
            task.host,
            runtime_task=os_user_tasks.ansibleUnLockUserTask(BECOME_PASS,yaml_save_path)
            result=runtime_task.run(task)
            if result:
                task.set_status(TaskStatusEnum.sucess)
            else:
                task.error_count=task.error_count+1
                if task.error_count>=5:
                    task.set_status(TaskStatusEnum.failure)
            task.save()
    except Exception as identifier:
        print(identifier)

def run_add_user_tasks():
    try:
        task_list=storage.osUser.util.get_undo_add_user_tasks()
        print(datetime.now(),'->',len(task_list),'add_user_tasks')
        for task in task_list:
            if task.status == TaskStatusEnum.init:
                task.set_status(TaskStatusEnum.processing)
                task.save()
            yaml_save_path=YAML_PATH+datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')+'_add_user.yaml'
            task.host,
            runtime_task=os_user_tasks.ansibleAddUserTask(BECOME_PASS,yaml_save_path)
            result=runtime_task.run(task)
            if result:
                task.set_status(TaskStatusEnum.sucess)
            else:
                task.error_count=task.error_count+1
                if task.error_count>=5:
                    task.set_status(TaskStatusEnum.failure)
            task.save()
    except Exception as identifier:
        print(identifier)

def run_add_sudo_tasks():
    try:
        task_list=storage.osUser.util.get_undo_add_sudo_tasks()
        print(datetime.now(),'->',len(task_list),'add_sudo_tasks')
        for task in task_list:
            if task.status == TaskStatusEnum.init:
                task.set_status(TaskStatusEnum.processing)
                task.save()
            yaml_save_path=YAML_PATH+datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')+'_add_sudo.yaml'
            task.host,
            runtime_task=os_user_tasks.ansibleAddSudoTask(BECOME_PASS,yaml_save_path)
            result=runtime_task.run(task)
            if result:
                task.set_status(TaskStatusEnum.sucess)
            else:
                task.error_count=task.error_count+1
                if task.error_count>=5:
                    task.set_status(TaskStatusEnum.failure)
            task.save()
    except Exception as identifier:
        print(identifier)

def run_change_password_tasks():
    try:
        task_list=storage.osUser.util.get_undo_change_password_tasks()
        print(datetime.now(),'->',len(task_list),'change_password_tasks')
        for task in task_list:
            if task.status == TaskStatusEnum.init:
                task.set_status(TaskStatusEnum.processing)
                task.save()
            yaml_save_path=YAML_PATH+datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')+'_change_password.yaml'
            task.host,
            runtime_task=os_user_tasks.ansibleChangePasswordTask(BECOME_PASS,yaml_save_path)
            result=runtime_task.run(task)
            if result:
                task.set_status(TaskStatusEnum.sucess)
            else:
                task.error_count=task.error_count+1
                if task.error_count>=5:
                    task.set_status(TaskStatusEnum.failure)
            task.save()
    except Exception as identifier:
        print(identifier)

def run_add_publickey_tasks():
    try:
        task_list=storage.osUser.util.get_undo_add_publickey_tasks()
        print(datetime.now(),'->',len(task_list),'add_publickey_tasks')
        for task in task_list:
            if task.status == TaskStatusEnum.init:
                task.set_status(TaskStatusEnum.processing)
                task.save()
            yaml_save_path=YAML_PATH+datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')+'_add_publickey.yaml'
            task.host,
            runtime_task=os_user_tasks.ansibleAddPublickeyTask(BECOME_PASS,yaml_save_path)
            result=runtime_task.run(task)
            if result:
                task.set_status(TaskStatusEnum.sucess)
            else:
                task.error_count=task.error_count+1
                if task.error_count>=5:
                    task.set_status(TaskStatusEnum.failure)
            task.save()
    except Exception as identifier:
        print(identifier)

def run_add_group_tasks():
    try:
        task_list=storage.osUser.util.get_undo_add_group_tasks()
        print(datetime.now(),'->',len(task_list),'add_group_tasks')
        for task in task_list:
            if task.status == TaskStatusEnum.init:
                task.set_status(TaskStatusEnum.processing)
                task.save()
            yaml_save_path=YAML_PATH+datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')+'_add_group.yaml'
            task.host,
            runtime_task=os_user_tasks.ansibleAddGroupTask(BECOME_PASS,yaml_save_path)
            result=runtime_task.run(task)
            if result:
                task.set_status(TaskStatusEnum.sucess)
            else:
                task.error_count=task.error_count+1
                if task.error_count>=5:
                    task.set_status(TaskStatusEnum.failure)
            task.save()
    except Exception as identifier:
        print(identifier)

task_list=[run_lock_user_tasks,run_unlock_user_tasks,run_add_user_tasks,run_add_sudo_tasks,run_change_password_tasks,run_add_publickey_tasks,run_add_group_tasks]
def run_all_task():
    while True:
        for func in task_list:
            func()
        time.sleep(10)


if __name__ == "__main__":
    run_all_task()









