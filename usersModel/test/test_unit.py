# -*- coding: utf-8 -*-
'''
    desc: 测试 lock_user 模块
    author: liu kun
    date: 2020-04-04
'''

import pathlib
import sys
import os
from datetime import datetime
_project_root = str(pathlib.Path(__file__).resolve().parents[2])
sys.path.append(_project_root)

from usersModel import lock_user






def test_lock_user_01():
    """
    [测试 lock_user.run_task_yaml ]
    
    Returns:
        [type] -- [description]
    """
    obj=lock_user.TaskInfo()
    obj.username="labs"
    obj.host_ip="127.0.0.1"
    yaml_save_path=datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')+'lock_user.yaml'
    assert os.path.exists(yaml_save_path)==False
    lock_user.run_task_yaml(task_info_obj=obj,yaml_save_path=yaml_save_path)
    assert os.path.exists(yaml_save_path)==True
    with open(yaml_save_path ,'r') as test_yaml_file:
        yaml_str=test_yaml_file.read()
        assert obj.username in yaml_str
        assert obj.host_ip in yaml_str
    os.remove(yaml_save_path)
    assert os.path.exists(yaml_save_path)==False
    return True
def test_unlock_user_01():
    """
    [测试 unlock_user.run_task_yaml ]
    
    Returns:
        [type] -- [description]
    """
    
if __name__ == "__main__":
    test_lock_user_01()