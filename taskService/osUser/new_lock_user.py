# -*- coding: utf-8 -*-
'''
    desc: 锁定用户模块
    author: liukun
    date: 2020-04-08
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
from taskService.basicTask import ansiblePlaybookTask
from config import ansible_ssh_user,ansible_ssh_port,ansible_ssh_private_key_file



class ansibleLockUserTask(ansiblePlaybookTask):
    task_name="lockUser"
    yaml_template="""
- hosts: params_host
  become: yes
  become_user: root
  gather_facts: F #开启debug模式
  vars:
    username: params_username
    ansible_ssh_user : params_user
    ansible_ssh_port : params_port
    ansible_ssh_private_key_file : params_key_file
  tasks:
  - name: ping the machine
    ping:  
  - name: lock user |chang user login shell
    shell: usermod {{username}} -s /usr/sbin/nologin 
    """
    
    def init_yaml_params(self):
        data = yaml.safe_load(self.yaml_template)
        data[0]['hosts'] = self.task_info_obj.host
        data[0]['vars']['username'] = self.task_info_obj.username
        data[0]['vars']['ansible_ssh_user'] = ansible_ssh_user
        data[0]['vars']['ansible_ssh_port'] = ansible_ssh_port
        data[0]['vars']['ansible_ssh_private_key_file'] = ansible_ssh_private_key_file
        return data

