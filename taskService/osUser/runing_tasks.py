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
import storage.osUser.models
from taskService.basicTask import RunningTask
import  click
from datetime import datetime
import time
import fire
from config import BECOME_PASS,ANSIBLE_SSH_USER,ANSIBLE_SSH_PORT,ANSIBLE_SSH_PRIVATE_KEY_FILE


class LockUserRunningTask(RunningTask):
    task_name:str="lock_user_task"
    db_task_type_name  = storage.osUser.models.LockUserTask
    ansible_task_type_name =os_user_tasks.ansibleLockUserTask

class UnLockUserRunningTask(RunningTask):
    task_name:str="unlock_user_task"
    db_task_type_name  = storage.osUser.models.UNLockUserTask
    ansible_task_type_name =os_user_tasks.ansibleUnLockUserTask

class AddUserRunningTask(RunningTask):
    task_name:str="add_user_task"
    db_task_type_name  = storage.osUser.models.AddUserTask
    ansible_task_type_name =os_user_tasks.ansibleAddUserTask

class AddSudoRunningTask(RunningTask):
    task_name:str="add_sudo_task"
    db_task_type_name  = storage.osUser.models.AddSudoTask
    ansible_task_type_name =os_user_tasks.ansibleAddSudoTask

class ChangePasswordRunningTask(RunningTask):
    task_name:str="change_password_task"
    db_task_type_name  = storage.osUser.models.ChangePasswordTask
    ansible_task_type_name =os_user_tasks.ansibleChangePasswordTask

class AddPublickeyRunningTask(RunningTask):
    task_name:str="add_publickey_task"
    db_task_type_name  = storage.osUser.models.AddPublickeyTask
    ansible_task_type_name =os_user_tasks.ansibleAddPublickeyTask

class AddGroupRunningTask(RunningTask):
    task_name:str="add_group_task"
    db_task_type_name  = storage.osUser.models.AddGroupTask
    ansible_task_type_name =os_user_tasks.ansibleAddGroupTask


def run_all_osuser_tasks(sleep_time_seconds):
    task_class_list=[LockUserRunningTask,UnLockUserRunningTask,AddUserRunningTask,AddSudoRunningTask,ChangePasswordRunningTask,AddPublickeyRunningTask,AddGroupRunningTask]
    ansibile_vars={
    'ansible_ssh_user' : ANSIBLE_SSH_USER,
    'ansible_ssh_port' : ANSIBLE_SSH_PORT,
    'ansible_ssh_private_key_file' : ANSIBLE_SSH_PRIVATE_KEY_FILE
    }
    task_obj_list=[]
    for task_class in task_class_list:
        task_obj_list.append(
            task_class(
        ansibile_vars=ansibile_vars ,
        ansible_become_pass=BECOME_PASS)
        )
    while True:
        for task_obj in task_obj_list:
            task_obj.run()
        time.sleep(sleep_time_seconds)

if __name__ == "__main__":
    fire.Fire(
        {
            "run_all_osuser":run_all_osuser_tasks
        }
    )









