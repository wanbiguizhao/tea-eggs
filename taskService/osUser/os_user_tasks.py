# -*- coding: utf-8 -*-
'''
    desc: 用户任务相关的所有模块
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
from config import ANSIBLE_SSH_USER,ANSIBLE_SSH_PORT,ANSIBLE_SSH_PRIVATE_KEY_FILE



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
        data[0]['vars']['ansible_ssh_user'] = ANSIBLE_SSH_USER
        data[0]['vars']['ansible_ssh_port'] = ANSIBLE_SSH_PORT
        data[0]['vars']['ansible_ssh_private_key_file'] = ANSIBLE_SSH_PRIVATE_KEY_FILE
        return data

class ansibleUnLockUserTask(ansiblePlaybookTask):
    task_name="unlockUser"
    yaml_template = """
- hosts: params_host
  become: yes
  become_user: root
  gather_facts: F #开启debug模式
  vars:
    username: params_username
  tasks:
  - name: ping the machine
    ping:
  - name: unlock user |chang user login shell
    shell: usermod {{username}} -s /bin/bash
"""
    def init_yaml_params(self):
        data = yaml.safe_load(self.yaml_template)
        data[0]['hosts'] = self.task_info_obj.host
        data[0]['vars']['username'] = self.task_info_obj.username
        data[0]['vars']['ansible_ssh_user'] = ANSIBLE_SSH_USER
        data[0]['vars']['ansible_ssh_port'] = ANSIBLE_SSH_PORT
        data[0]['vars']['ansible_ssh_private_key_file'] = ANSIBLE_SSH_PRIVATE_KEY_FILE
        return data

class ansibleAddUserTask(ansiblePlaybookTask):
    task_name='adduser'
    yaml_template = """
- hosts: params_host
  become: yes
  become_user: root
  gather_facts: F #开启debug模式
  vars:
    username: params_username
    password: params_password
    public_key: params_public_key
  tasks:
  - name: ping the machine
    ping:
  - name: add user
    user:
      name: '{{username}}'
      password: '{{password | password_hash("sha512")}}'
      shell: /bin/bash
      append: yes
  - name: create key directory
    action: file path=/home/{{username}}/.ssh mode=0700 state=directory owner={{username}}
      group={{username}}
  - name: set authorized key
    authorized_key:
      key: '{{public_key}}'
      state: present
      user: '{{username}}'
"""
    def init_yaml_params(self):
        data = yaml.safe_load(self.yaml_template)
        data[0]['hosts'] = self.task_info_obj.host
        data[0]['vars']['username'] = self.task_info_obj.username
        data[0]['vars']['password'] = self.task_info_obj.password
        data[0]['vars']['public_key'] = self.task_info_obj.publickey
        data[0]['vars']['ansible_ssh_user'] = ANSIBLE_SSH_USER
        data[0]['vars']['ansible_ssh_port'] = ANSIBLE_SSH_PORT
        data[0]['vars']['ansible_ssh_private_key_file'] = ANSIBLE_SSH_PRIVATE_KEY_FILE
        return data

class ansibleAddSudoTask(ansiblePlaybookTask):
    task_name="addsudo"
    yaml_template = """
- hosts: params_host
  become: yes
  become_user: root
  gather_facts: F #开启debug模式
  vars:
    username: params_username
  tasks:
  - name: ping the machine
    ping:
  - name: add user sudo
    lineinfile: dest=/etc/sudoers state=present  line='{{item}}' validate='visudo -cf %s'
    with_items:
      - "{{username}} ALL=(ALL) NOPASSWD: ALL"
"""
    def init_yaml_params(self):
        data = yaml.safe_load(self.yaml_template)
        data[0]['hosts'] = self.task_info_obj.host
        data[0]['vars']['username'] = self.task_info_obj.username
        data[0]['vars']['ansible_ssh_user'] = ANSIBLE_SSH_USER
        data[0]['vars']['ansible_ssh_port'] = ANSIBLE_SSH_PORT
        data[0]['vars']['ansible_ssh_private_key_file'] = ANSIBLE_SSH_PRIVATE_KEY_FILE
        return data

class ansibleAddPublickeyTask(ansiblePlaybookTask):
    task_name='addpublickey'
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
  - name: set authorized key
    authorized_key:
      key: '{{public_key}}'
      state: present
      user: '{{username}}'
"""
    def init_yaml_params(self):
        data = yaml.safe_load(self.yaml_template)
        data[0]['hosts'] = self.task_info_obj.host
        data[0]['vars']['username'] = self.task_info_obj.username
        data[0]['vars']['public_key'] = self.task_info_obj.publickey
        data[0]['vars']['ansible_ssh_user'] = ANSIBLE_SSH_USER
        data[0]['vars']['ansible_ssh_port'] = ANSIBLE_SSH_PORT
        data[0]['vars']['ansible_ssh_private_key_file'] = ANSIBLE_SSH_PRIVATE_KEY_FILE
        return data

class ansibleChangePasswordTask(ansiblePlaybookTask):
    task_name='changepassword'
    yaml_template = """
- hosts: params_host
  become: yes
  become_user: root
  gather_facts: F #开启debug模式
  vars:
    username: params_username
    password: params_password
  tasks:
  - name: ping the machine
    ping:
  - name: change user password
    user:
      name: '{{username}}'
      password: '{{password | password_hash("sha512")}}'
      shell: /bin/bash
      update_password: always
"""
    def init_yaml_params(self):
        data = yaml.safe_load(self.yaml_template)
        data[0]['hosts'] = self.task_info_obj.host
        data[0]['vars']['username'] = self.task_info_obj.username
        data[0]['vars']['password'] = self.task_info_obj.password
        data[0]['vars']['ansible_ssh_user'] = ANSIBLE_SSH_USER
        data[0]['vars']['ansible_ssh_port'] = ANSIBLE_SSH_PORT
        data[0]['vars']['ansible_ssh_private_key_file'] = ANSIBLE_SSH_PRIVATE_KEY_FILE
        return data

class ansibleAddGroupTask(ansiblePlaybookTask):
    task_name='addgroup'
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
    def init_yaml_params(self):
        data = yaml.safe_load(self.yaml_template)
        data[0]['hosts'] = self.task_info_obj.host
        data[0]['vars']['username'] = self.task_info_obj.username
        data[0]['vars']['groupname'] = self.task_info_obj.groupname
        data[0]['vars']['ansible_ssh_user'] = ANSIBLE_SSH_USER
        data[0]['vars']['ansible_ssh_port'] = ANSIBLE_SSH_PORT
        data[0]['vars']['ansible_ssh_private_key_file'] = ANSIBLE_SSH_PRIVATE_KEY_FILE
        return data
