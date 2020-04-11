
# -*- coding: utf-8 -*-
'''
    desc: 基础异常
    author: liukun
    date: 2020-04-11
'''
import pathlib
import sys
_project_root = str(pathlib.Path(__file__).resolve().parents[1])
sys.path.append(_project_root)
from traceback import print_exc
class NoPreCheckException(Exception):
    '''自定义异常类'''
    code="100"
    msg="ansible 任务运行之前需要进行前置检查"
    def __init__(self):
        print_exc()
    
    def __repr__(self):
        return " code:{0}  msg:{1} type:{2}".format(self.code,self.msg,"NoPreCheckException")