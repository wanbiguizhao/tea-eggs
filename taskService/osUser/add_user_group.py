# -*- coding: utf-8 -*-
'''
	desc: 增加用户辅助组模块
	author：miguitian
	date：2020-04-10
'''

import pathlib
import sys
import os
import yaml
from ansible.playbook import Playbook
from ansible.vars.manager import VariableManager
from ansible.executor.playbook_executor import PlaybookExecutor
_project_root = str(pathlib.Path(__file__).resolve().parents[2])
sys.path.append(_project_root)
from ansibleService import playbook
from config import config

YAML_PATH = config['add_user_group']['yaml_path']
BECOME_PASS = config['add_user_group']['become_pass']
HOST = config['add_user_group']['host']
USERNAME = config['add_user_group']['username']
GROUPNAME = config['add_user_group']['groupname']

#publickey的密钥文件需要存放在YAML_PATH路径的vars文件夹内
yaml_template = """
- hosts: params_host
  become: yes
  become_user: root
  gather_facts: F #开启debug模式
  vars:
    username: params_username
    groupname: params_groupname
  tasks:
  - name: ping the machine
    ping:
  - name: add group
    shell: usermod -aG {{groupname}} {{username}}
"""

class TaskInfo:
    host = ""
    username = ""
    groupname = ""

def run_task_yaml(task_info_obj  , yaml_save_path):
    data = yaml.safe_load(yaml_template)
    data[0]['hosts'] = task_info_obj.host
    data[0]['vars']['username'] = task_info_obj.username
    data[0]['vars']['groupname'] = task_info_obj.groupname
    with open(yaml_save_path, 'w') as yaml_file:
        documents = yaml.dump(data, yaml_file)
#        print(documents)
    become_pass=BECOME_PASS
    #os.path.abspath(yaml_save_path)
    playbook.run_palybook(os.path.abspath(yaml_save_path),become_pass)
    return True # todo 根据事情情况判断执行是否成功，返回的数据也不是单纯的True或者False


def run_task():
    playbook.playbook_run()
    Playbook.load()

if __name__ == "__main__":
    task_info_obj = TaskInfo()
    task_info_obj.host = HOST
    task_info_obj.username = USERNAME
    task_info_obj.groupname = GROUPNAME
    yaml_save_path = YAML_PATH
    run_task_yaml(task_info_obj, yaml_save_path)
    pass
