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
from storage.basicModel import AbstractTask
import yaml
import os
from ansibleService import playbook
from config import YAML_PATH ,BECOME_PASS

class ResultTask:
    status:bool=True
    code:int=200 # 状态码
    msg:str ="" # 执行信息
    detail:dict={} # 详细信息 

class ansiblePlaybookTask:
    task_name:str = ""
    yaml_template: str =""
    task_info_obj:AbstractTask = None
    yaml_data=None
    yaml_save_path=""
    check_pass:bool=False #运行前进行条件检查，确保check_pass=True时，run才可以运行。
    check_result: list =[] # 前置检查的条件。
    become_pass=""

    def __init__(self,become_pass:str,yaml_save_path:str="",task_name:str=""):
        super().__init__()
        self.become_pass=BECOME_PASS
        self.yaml_save_path=YAML_PATH+'/'+self.task_name+'.yaml'
    
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
        self.dumps_yaml_file() # 生成yaml文件。
        run_playbook = self.run_playbook()
        return run_playbook

#该函数在参数增多的话，无法做到兼容，只能是通过继承类的方法来进行初始化
#    def init_yaml_params(self):
#        """
#        子类实现填充ansible-playbook参数
#        """
#        data = yaml.safe_load(self.yaml_template)
#        data[0]['hosts'] = self.task_info_obj.host
#        data[0]['vars']['username'] = self.task_info_obj.username
#        return data
    def dumps_yaml_file(self):
        with open(self.yaml_save_path, 'w') as yaml_file:
            documents = yaml.dump(self.yaml_data, yaml_file)
#            print(documents)

    def run_playbook(self):        
        task = playbook.run_palybook(os.path.abspath(self.yaml_save_path),self.become_pass)
        if task == True:
            return True

if __name__ == "__main__":
    print("hello word")
