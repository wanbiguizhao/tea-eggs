# -*- coding: utf-8 -*-
'''
    desc: 封装的playbook模块
    author: liukun
    date: 2020-04-04
'''

import pathlib
import sys
import yaml
_project_root = str(pathlib.Path(__file__).resolve().parents[1])
sys.path.append(_project_root)

# coding=utf-8

import json
import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
import ansible.constants as C
from ansible import context
from optparse import Values

class ResultCallback(CallbackBase):
    def __init__(self, *args, **kwargs):
        super(ResultCallback, self).__init__(*args, **kwargs)
        self.task_ok={}

    def v2_runner_on_ok(self, result, *args, **kwargs):
        self.task_ok[result._host.get_name()]=result


results_callback = ResultCallback()

#InventoryManager类
loader = DataLoader()     #读取yaml文件
inventory = InventoryManager(loader=loader, sources=['/git/tea-eggs/usersModel/hosts'])#这里的路径要正确
#variableManager类
variable_manager = VariableManager(loader=loader,inventory=inventory)

#option 执行选项
Options = namedtuple('Optoins',
                     ['connection',
                      'remote_user',
                      'ask_sudo_pass',
                      'verbosity',
                      'ack_pass',
                      'module_path',
                      'forks',
                      'become',
                      'become_method',
                      'become_user',
                      'check',
                      'listhosts',
                      'syntax',
                      'listtags',
                      'listtasks',
                      'sudo_user',
                      'sudo',
                      'diff'])

options = Options(connection='smart',
                   remote_user=None,
                   ack_pass=None,
                   sudo_user=None,
                   forks=5,
                   sudo=None,
                   ask_sudo_pass=False,
                   verbosity=5,
                   module_path=None,
                   become=None,
                   become_method=None,
                   become_user=None,
                   check=False,
                   diff=False,
                   listhosts=None,
                   listtasks=None,
                   listtags=None,
                   syntax=None)

options = {'verbosity': 0, 'ask_pass': False, 'private_key_file': None, 'remote_user': None,
                    'connection': 'smart', 'timeout': 10, 'ssh_common_args': '', 'sftp_extra_args': '',
                    'scp_extra_args': '', 'ssh_extra_args': '', 'force_handlers': False, 'flush_cache': None,
                    'become': False, 'become_method': 'sudo', 'become_user': None, 'become_ask_pass': False,
                    'tags': ['all'], 'skip_tags': [], 'check': False, 'syntax': None, 'diff': False,
                    'inventory': '/Users/caishichao/Code/AnsibleCentrolManagement/inventory/hosts.uat',
                    'listhosts': None, 'subset': None, 'extra_vars': [], 'ask_vault_pass': False,
                    'vault_password_files': [], 'vault_ids': [], 'forks': 5, 'module_path': None, 'listtasks': None,
                    'listtags': None, 'step': None, 'start_at_task': None, 'args': ['fake']}
ops = Values(options)


passwords=dict()
context._init_global_context(ops)
#playbook的路径要正确
playbook=PlaybookExecutor(playbooks=['/git/tea-eggs/test.yaml'],
                          inventory=inventory,
                          variable_manager=variable_manager,
                          loader=loader,
                          #options=options,
                          passwords=passwords)

#playbook.run()

playbook._tqm._stdout_callback=results_callback
playbook.run()

results_raw={'ok':{}}

for host,result in results_callback.task_ok.items():
    results_raw['ok'][host]=result._result

print(results_raw)
# https://lex-lee.blog.csdn.net/article/details/92837916#PlaybookExecutorrun_390 