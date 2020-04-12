
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


from taskService.osUser.new_lock_user import ansibleLockUserTask
from storage.osUser.models import LockUserTask


def test_lock_user_task_01():
    """
    测试锁用户操作
    前置条件: cd PROJECTS_PATH/tea-eggs/taskService/osUser/test
    docker-compose up 
    ping  172.20.16.2 能通过时再执行测试
    """

    runtime_task=ansibleLockUserTask(become_pass="tea-eggs",yaml_save_path=_project_root+"/tmp.yml")
    task_model=LockUserTask()
    task_model.host="172.20.16.2"
    task_model.username="ops"
    ret=runtime_task.run(task_info_obj=task_model)
    assert runtime_task.check_pass==True
    assert ret !=None







