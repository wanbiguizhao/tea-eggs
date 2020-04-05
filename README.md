# tea-eggs
利用ansible给程序员节省一个吃茶叶蛋的时间。
# 前置工作
## 单元测试

pytest

## 代码规范化检测
pylint --rcfile=default.pylintrc */*.py

## 生成依赖requirements.txt
pipreqs  --ignore=venv,web-server . --force
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
# 模型说明
## usersModel
linux系统管理用户的工具集合
- 增加用户(用户组是用户的组)
- 给用户重置密码
- 更新用户密钥
- 增加用户辅助组
- 增加sudo权限

## tools
系统运行涉及的常用工具  
