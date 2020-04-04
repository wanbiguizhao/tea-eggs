# -*- coding: utf-8 -*-
'''
    desc: 锁定用户模块
    author: liukun
    date: 2020-04-04
'''

import pathlib
import sys
import yaml
_project_root = str(pathlib.Path(__file__).resolve().parents[1])
sys.path.append(_project_root)


yaml_template = """
- hosts: params_host_ip
  gather_facts: F #开启debug模式
  vars:
    username: params_username
  tasks:
  - name: ping the machine
    ping:  
  - name: lock user |chang user login shell
    shell: usermod {{username}} -s /usr/sbin/nologin 
    sudo: yes
"""


class TaskInfo:
    host_ip = ""
    username = ""


def dump_task_yaml(task_info_obj, yaml_save_path):
    data = yaml.safe_load(yaml_template)
    data[0]['hosts'] = task_info_obj.host_ip
    data[0]['vars']['username'] = task_info_obj.username
    with open(yaml_save_path, 'w') as yaml_file:
        documents = yaml.dump(data, yaml_file)
        print(documents)


if __name__ == "__main__":
    # task_info_obj = TaskInfo()
    # task_info_obj.host_ip = "127.0.0.1"
    # task_info_obj.username = "labs"
    # yaml_save_path = "./test.yaml"
    # dump_task_yaml(task_info_obj, yaml_save_path)
    pass
