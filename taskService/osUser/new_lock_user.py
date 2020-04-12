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




class ansibleLockUserTask(ansiblePlaybookTask):
    task_name="lockUser"
    yaml_template="""
- hosts: params_host
  become: yes
  become_user: root
  gather_facts: F #开启debug模式
  vars:
    username: params_username
  tasks:
  - name: ping the machine
    ping:  
  - name: lock user |chang user login shell
    shell: usermod {{username}} -s /usr/sbin/nologin 
    """
    

