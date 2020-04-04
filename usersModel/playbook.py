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

from ansible.playbook import PlayBook


pb = PlayBook(playbook='/path/to/book.yml, --other initializers--')