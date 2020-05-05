
# -*- coding: utf-8 -*-
'''
    desc: 测试user代码
    author: liukun
    date: 2020-04-12
'''
import pathlib
import sys
_project_root = str(pathlib.Path(__file__).resolve().parents[2])
sys.path.append(_project_root)
from traceback import print_exc
import taskService.osUser.os_user_tasks
import storage.osUser.models
import json
from config import TEST_ANSIBLE_VARS

def test_LockUserRunningTask_01():
    """
    测试锁用户操作
    前置条件: cd PROJECTS_PATH/tea-eggs/taskService/osUser/test
    docker-compose up 
    ping  172.20.16.2 能通过时再执行测试
    """
    yaml_save_path=_project_root+"/TEST/lock_user.yml"
    running_task=taskService.osUser.os_user_tasks.ansibleLockUserTask(
        ansibile_vars=TEST_ANSIBLE_VARS,yaml_save_path=yaml_save_path,become_pass='tea-eggs'
    )
    task_model=storage.osUser.models.LockUserTask()
    task_model.host="127.0.0.1"
    task_model.username="osuser"
    ret=running_task.run(task_info_obj=task_model)
    assert running_task.check_pass==True
    assert ret !=None
    assert ret["sucess_flag"] == True

def test_UnLockUserRunningTask_01():
    """
    测试解锁用户操作
    前置条件: cd PROJECTS_PATH/tea-eggs/taskService/osUser/test
    docker-compose up
    ping  172.20.16.2 能通过时再执行测试
    """
    yaml_save_path=_project_root+"/TEST/unlock_user.yml"
    running_task=taskService.osUser.os_user_tasks.ansibleUnLockUserTask(
        ansibile_vars=TEST_ANSIBLE_VARS,yaml_save_path=yaml_save_path,become_pass='tea-eggs'
    )
    task_model=storage.osUser.models.UNLockUserTask()
    task_model.host="127.0.0.1"
    task_model.username="osuser"
    ret=running_task.run(task_info_obj=task_model)
    assert running_task.check_pass==True
    assert ret !=None
    assert ret["sucess_flag"] == True

def test_AddUserRunningTask_01():
    """
    测试添加用户操作
    前置条件: cd PROJECTS_PATH/tea-eggs/taskService/osUser/test
    docker-compose up
    ping  172.20.16.2 能通过时再执行测试
    """
    yaml_save_path=_project_root+"/TEST/add_user.yml"
    running_task=taskService.osUser.os_user_tasks.ansibleAddUserTask(
        ansibile_vars=TEST_ANSIBLE_VARS,yaml_save_path=yaml_save_path,become_pass='tea-eggs'
    )
    task_model=storage.osUser.models.AddUserTask()
    task_model.host="127.0.0.1"
    task_model.username="MMM"
    task_model.password="123456"
    task_model.publickey="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCV0SMm8r9tycALVtCEKWlebDpcRQRq0iunZsu3sFoQaTjG8me9d603c5dnXbEMDNCSNgKvaz6gfJbsFfYq4Gg8qWAPSb10TeveZq65QAzOlpCK0xk/GpyZcJlaXQT5ymbN8I9BlMUosYIWKLwMqC33LoHqycsnxvJKdw++VvgUO3KFrUm+YaHr3/3XxCeBRYzYyUmHiAreqmnaLIcELYmhuk7PiX3Z8gYPJ/DprplDyDUWguwlp+1msBvNJR2afUA22tALP3ZDoEZ5iUHxR1Ml+GkIo1LtH1KWFMtlljwwpymINAz3pUXAg/aZmcN2UFKuivSbALV6TJt6j1pgnTl3 tea-eggs"
    ret=running_task.run(task_info_obj=task_model)
    assert running_task.check_pass==True
    assert ret !=None
    assert ret["sucess_flag"] == True

def test_AddSudoRunningTask_01():
    """
    测试给用户增加sudo权限操作
    前置条件: cd PROJECTS_PATH/tea-eggs/taskService/osUser/test
    docker-compose up
    ping  172.20.16.2 能通过时再执行测试
    """
    yaml_save_path=_project_root+"/TEST/add_sudo.yml"
    running_task=taskService.osUser.os_user_tasks.ansibleAddSudoTask(
        ansibile_vars=TEST_ANSIBLE_VARS,yaml_save_path=yaml_save_path,become_pass='tea-eggs'
    )
    task_model=storage.osUser.models.AddSudoTask()
    task_model.host="127.0.0.1"
    task_model.username="osuser"
    ret=running_task.run(task_info_obj=task_model)
    assert running_task.check_pass==True
    assert ret !=None
    assert ret["sucess_flag"] == True

def test_AddSudoRunningTask_01():
    """
    测试给用户增加sudo权限操作
    前置条件: cd PROJECTS_PATH/tea-eggs/taskService/osUser/test
    docker-compose up
    ping  172.20.16.2 能通过时再执行测试
    """
    yaml_save_path=_project_root+"/TEST/add_sudo.yml"
    running_task=taskService.osUser.os_user_tasks.ansibleAddSudoTask(
        ansibile_vars=TEST_ANSIBLE_VARS,yaml_save_path=yaml_save_path,become_pass='tea-eggs'
    )
    task_model=storage.osUser.models.AddSudoTask()
    task_model.host="127.0.0.1"
    task_model.username="osuser"
    ret=running_task.run(task_info_obj=task_model)
    assert running_task.check_pass==True
    assert ret !=None
    assert ret["sucess_flag"] == True

def test_AddPublickeyRunningTask_01():
    """
    测试给用户publickey操作
    前置条件: cd PROJECTS_PATH/tea-eggs/taskService/osUser/test
    docker-compose up
    ping  172.20.16.2 能通过时再执行测试
    """
    yaml_save_path=_project_root+"/TEST/add_publickey.yml"
    running_task=taskService.osUser.os_user_tasks.ansibleAddPublickeyTask(
        ansibile_vars=TEST_ANSIBLE_VARS,yaml_save_path=yaml_save_path,become_pass='tea-eggs'
    )
    task_model=storage.osUser.models.AddPublickeyTask()
    task_model.host="127.0.0.1"
    task_model.username="osuser"
    task_model.publickey="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCV0SMm8r9tycALVtCEKWlebDpcRQRq0iunZsu3sFoQaTjG8me9d603c5dnXbEMDNCSNgKvaz6gfJbsFfYq4Gg8qWAPSb10TeveZq65QAzOlpCK0xk/GpyZcJlaXQT5ymbN8I9BlMUosYIWKLwMqC33LoHqycsnxvJKdw++VvgUO3KFrUm+YaHr3/3XxCeBRYzYyUmHiAreqmnaLIcELYmhuk7PiX3Z8gYPJ/DprplDyDUWguwlp+1msBvNJR2afUA22tALP3ZDoEZ5iUHxR1Ml+GkIo1LtH1KWFMtlljwwpymINAz3pUXAg/aZmcN2UFKuivSbALV6TJt6j1pgnTl3 tea-eggs"
    ret=running_task.run(task_info_obj=task_model)
    assert running_task.check_pass==True
    assert ret !=None
    assert ret["sucess_flag"] == True

def test_ChangePasswordRunningTask_01():
    """
    测试修改用户密码操作
    前置条件: cd PROJECTS_PATH/tea-eggs/taskService/osUser/test
    docker-compose up
    ping  172.20.16.2 能通过时再执行测试
    """
    yaml_save_path=_project_root+"/TEST/change_password.yml"
    running_task=taskService.osUser.os_user_tasks.ansibleChangePasswordTask(
        ansibile_vars=TEST_ANSIBLE_VARS,yaml_save_path=yaml_save_path,become_pass='tea-eggs'
    )
    task_model=storage.osUser.models.ChangePasswordTask()
    task_model.host="127.0.0.1"
    task_model.username="MMM"
    task_model.password='666666'
    ret=running_task.run(task_info_obj=task_model)
    assert running_task.check_pass==True
    assert ret !=None
    assert ret["sucess_flag"] == True

def test_AddGroupRunningTask_01():
    """
    测试给用户添加组操作
    前置条件: cd PROJECTS_PATH/tea-eggs/taskService/osUser/test
    docker-compose up
    ping  172.20.16.2 能通过时再执行测试
    """
    yaml_save_path=_project_root+"/TEST/add_group.yml"
    running_task=taskService.osUser.os_user_tasks.ansibleAddGroupTask(
        ansibile_vars=TEST_ANSIBLE_VARS,yaml_save_path=yaml_save_path,become_pass='tea-eggs'
    )
    task_model=storage.osUser.models.AddGroupTask()
    task_model.host="127.0.0.1"
    task_model.username="MMM"
    task_model.groupname="osuser"
    ret=running_task.run(task_info_obj=task_model)
    assert running_task.check_pass==True
    assert ret !=None
    assert ret["sucess_flag"] == True


if __name__ == "__main__":
    #test_lock_user_task_01()
    test_LockUserRunningTask_01()






