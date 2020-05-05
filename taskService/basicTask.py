# -*- coding: utf-8 -*-
'''
    desc: 基础任务
    author: liukun
    date: 2020-04-11
'''
import pathlib
import sys
_project_root = str(pathlib.Path(__file__).resolve().parents[1])
sys.path.append(_project_root)
from taskService.basicException import NoPreCheckException
from storage.basicModel import AbstractTask, TaskStatusEnum
import yaml
import os
from ansibleService import playbook
from typing import List
from pydantic import BaseModel
from datetime import datetime
from storage.basicModel import AbstractTask
from storage  import  util
from config import YAML_PATH

class ResultTask:
    status:bool=True
    code:int=200 # 状态码
    msg:str ="" # 执行信息
    detail:dict={} # 详细信息 

class AnsiblePlaybookTask:
    task_name:str = ""
    yaml_template: str =""
    task_info_obj:AbstractTask = None
    yaml_data=None
    yaml_save_path=""
    check_pass:bool=False #运行前进行条件检查，确保check_pass=True时，run才可以运行。
    check_result: list =[] # 前置检查的条件。
    become_pass=""

    def __init__(self,become_pass:str ,yaml_save_path:str="" , ansibile_vars:dict={} ):
        """[初始化任务参数]
        
        Arguments:
            become_pass {str} -- [sudo密码]
        
        Keyword Arguments:
            yaml_save_path {str} -- [yaml的保存路径] (default: {""})
            ansibile_vars {dict} -- [ansible 相关的参数  例如:ansible_ssh_user,ansible_ssh_port,ansible_ssh_private_key_file] (default: {{}})
        """
        self.become_pass=become_pass
        self.yaml_save_path=yaml_save_path
        self.ansibile_vars  = ansibile_vars

    def do_check_list(self):
        """
        程序执行之前执行初始条件检查，确保满足前置条件。
        """
        self.check_result=[]
        self.check_pass=True
        if self.task_name=="":
            self.check_pass=False
            check_result.append(("task_name",self.task_name,"不能为空"))
        if self.yaml_template=="":
            self.check_pass=False
            check_result.append("yaml_template",self.yaml_template,"不能为空")
        if self.yaml_save_path=="":
            self.check_pass=False
            check_result.append("yaml_save_path",self.yaml_save_path,"不能为空")
        return self.check_result

    def set_yaml_save_path(self,yaml_save_path):
        """
        子类可以重写本方法，用于重新计算或者设置yaml_save_path路径，外部调用。
        """
        self.yaml_save_path=yaml_save_path

    def set_yaml_template(self,tmplate):
        """
        如果yaml_template没有提前定义好，可以使用该方法定义。
        """
        self.yaml_template=tmplate

    def run(self, task_info_obj:AbstractTask):
        self.do_check_list()
        if not self.check_pass:
            raise NoPreCheckException()
        self.task_info_obj= task_info_obj
        self.yaml_data=self.init_yaml_params() # 初始化
        self.init_ansibile_vars()# 初始化ansible相关的参数(主要是涉及可以是ansible可以正常访问远程主机的参数)，
        self.dumps_yaml_file() # 生成yaml文件。
        return self.run_playbook()

    def init_ansibile_vars(self):
        for key,value in self.ansibile_vars.items():
            self.yaml_data[0]['vars'][key]=value
    def init_yaml_params(self):
        """
        子类实现填充ansible-playbook参数
        """
        data = yaml.safe_load(self.yaml_template)
        data[0]['hosts'] = self.task_info_obj.host
        data[0]['vars']['username'] = self.task_info_obj.username
        return data

    def dumps_yaml_file(self):
        with open(self.yaml_save_path, 'w') as yaml_file:
            documents = yaml.dump(self.yaml_data, yaml_file)
#            print(documents)

    def run_playbook(self):        
        return playbook.run_palybook(os.path.abspath(self.yaml_save_path),self.become_pass)



class RunningTask(BaseModel):
    """
    [负责将要执行的任务,从数据库中取出来,并且执行任务]
    """
    task_name: str ="RunningTask"
    db_task_type_name = AbstractTask  # 数据库模型类的名称,子类可以重载
    ansible_task_type_name = AnsiblePlaybookTask # ansible-playbook执行任务的
    ansibile_vars:dict={}  # ansible 客户端使用的参数
    ansible_become_pass: str="tea-eggs"
    yaml_save_path:str =datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')+task_name+'tmp.yaml' # yaml 文件存放的位置.
   # yaml_save_path=datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')+'lock_user.yaml'
   # ansibile_vars={ 
   #         'ansible_ssh_user' : 'ops',
   #         'ansible_ssh_port' : '22222',
   #         'ansible_ssh_private_key_file' : "/Users/mi/git/tea-eggs/taskService/test/sshkey/eggs_rsa"
   #         }


    def get_undo_task(self):
        """"父类已经实现,子类可以改写"""
        return util.get_undo_task(self.db_task_type_name)

    def run(self):
        try:
            task_list=self.get_undo_task()
            print(datetime.now(),'->',len(task_list),self.task_name)
            for task in task_list:
                if task.status == TaskStatusEnum.init:
                    task.set_status(TaskStatusEnum.processing)
                    task.save()
                self.yaml_save_path = YAML_PATH+datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')+self.task_name+'.yaml'
                runtime_task=self.ansible_task_type_name(become_pass=self.ansible_become_pass ,yaml_save_path=self.yaml_save_path,ansibile_vars=self.ansibile_vars)
                result=runtime_task.run(task_info_obj=task)
                if result["sucess_flag"]:
                    task.set_status(TaskStatusEnum.sucess)
                else:
                    task.error_count=task.error_count+1
                    if task.error_count>=5:
                        task.set_status(TaskStatusEnum.failure)
                task.save()
            return True
        except Exception as identifier:
            print(identifier)
            return False
if __name__ == "__main__":
    print("hello word")
