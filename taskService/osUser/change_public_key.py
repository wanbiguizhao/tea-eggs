# -*- coding: utf-8 -*-
'''
	desc: 更新用户密钥模块
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

YAML_PATH = config['change_public_key']['yaml_path']
BECOME_PASS = config['change_public_key']['become_pass']
HOST = config['change_public_key']['host']
USERNAME = config['change_public_key']['username']
PUBLICKEY = config['change_public_key']['publickey']

#publickey的密钥文件需要存放在YAML_PATH路径的vars文件夹内
yaml_template = """
- hosts: params_host
  become: yes
  become_user: root
  gather_facts: F #开启debug模式
  vars:
    username: params_username
    public_key: params_public_key
  tasks:
  - name: ping the machine
    ping:
  - name: backup authorized key
    shell: mv /home/{{username}}/.ssh/authorized_keys  /home/{{username}}/.ssh/authorized_keys.$(date +%F).bak
  - name: set authorized key
    authorized_key:
      key: '{{lookup("file","vars/{{public_key}}")}}'
      state: present
      user: '{{username}}'
"""

class TaskInfo:
    host = ""
    username = ""
    publickey = ""

def run_task_yaml(task_info_obj  , yaml_save_path):
    data = yaml.safe_load(yaml_template)
    data[0]['hosts'] = task_info_obj.host
    data[0]['vars']['username'] = task_info_obj.username
    data[0]['vars']['public_key'] = task_info_obj.publickey
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
    task_info_obj.publickey = PUBLICKEY
    yaml_save_path = YAML_PATH
    run_task_yaml(task_info_obj, yaml_save_path)
    pass
