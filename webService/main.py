# -*- coding: utf-8 -*-
'''
    desc: web接口模块
    author: liukun
    date: 2020-04-05
'''
import sys
import pathlib
from fastapi import FastAPI
_project_root = str(pathlib.Path(__file__).resolve().parents[1])
sys.path.append(_project_root)
from webService.osUser.main import osUserApp
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

app.mount("/osuser", osUserApp)  # webService 每次新增加一个模块，都在这里使用app mount挂载一下
