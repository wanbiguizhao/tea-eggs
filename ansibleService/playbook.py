# -*- coding: utf-8 -*-
'''
    desc: 封装的playbook模块
    author: liukun
    date: 2020-04-04
'''

import shutil
import json
from optparse import Values
from ansible import context
import ansible.constants as C
from ansible.plugins.callback import CallbackBase
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader
from collections import namedtuple
import pathlib
import sys
import yaml
_project_root = str(pathlib.Path(__file__).resolve().parents[1])
sys.path.append(_project_root)
from config import HOSTS_PATH

test=''

class ResultCallback(CallbackBase):
    """A sample callback plugin used for performing an action as results come in

    If you want to collect all results into a single object for processing at
    the end of the execution, look into utilizing the ``json`` callback plugin
    or writing your own custom callback plugin
    """

    def v2_runner_on_ok(self, result, **kwargs):
        """Print a json representation of the result

        This method could store the result in an instance attribute for retrieval later
        """
        host = result._host
        print(json.dumps({host.name: result._result},
                         indent=4, ensure_ascii=False))
        global test
        test = 'ok'
    def v2_runner_on_failed(self, result, **kwargs):
        host = result._host.get_name()
        self.runner_on_failed(host, result._result, False)
        print('===v2_runner_on_failed====host=%s===result=%s' %
              (host, result._result))
        test = 'faild'
    def v2_runner_on_unreachable(self, result):
        host = result._host.get_name()
        self.runner_on_unreachable(host, result._result)
        print('===v2_runner_on_unreachable====host=%s===result=%s' %
              (host, result._result))
        test = 'unreachable'
    def v2_runner_on_skipped(self, result):
        if C.DISPLAY_SKIPPED_HOSTS:
            host = result._host.get_name()
            self.runner_on_skipped(host, self._get_item(
                getattr(result._result, 'results', {})))
            print("this task does not execute,please check parameter or condition.")
            test = 'skipped'
    def v2_playbook_on_stats(self, stats):
        print('===========play executes completed========')

def run_palybook(playbook_path, become_pass):
    # InventoryManager类
    loader = DataLoader()  # 读取yaml文件
    inventory = InventoryManager(loader=loader, sources=[HOSTS_PATH])  # 这里的路径要正确
    # variableManager类
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # option 执行选项
    options = {'verbosity': 0, 'ask_pass': False, 'private_key_file': None, 'remote_user': None,
               'connection': 'smart', 'timeout': 10, 'ssh_common_args': '', 'sftp_extra_args': '',
               'scp_extra_args': '', 'ssh_extra_args': '', 'force_handlers': False, 'flush_cache': None,
               'become': True, 'become_method': 'sudo', 'become_user': 'memect_ops', 'become_ask_pass': False,
               'tags': ['all'], 'skip_tags': [], 'check': False, 'syntax': None, 'diff': False,
               'inventory': '/Users/caishichao/Code/AnsibleCentrolManagement/inventory/hosts.uat',
               'listhosts': None, 'subset': None, 'extra_vars': [], 'ask_vault_pass': False,
               'vault_password_files': [], 'vault_ids': [], 'forks': 5, 'module_path': None, 'listtasks': None,
               'listtags': None, 'step': None, 'start_at_task': None, 'args': ['fake']}
    ops = Values(options)
    passwords = {'conn_pass': '', 'become_pass': become_pass}
    context._init_global_context(ops)
    playbook = PlaybookExecutor(playbooks=[playbook_path],
                                inventory=inventory,
                                variable_manager=variable_manager,
                                loader=loader,
                                passwords=passwords)
    results_callback = ResultCallback()
    playbook._tqm._stdout_callback = results_callback
    playbook.run()
    if test == 'ok':
        return True
    

if __name__ == "__main__":
    pass
# https://lex-lee.blog.csdn.net/article/details/92837916#PlaybookExecutorrun_390
