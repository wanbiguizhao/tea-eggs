import os
import configparser


project_root = os.path.dirname(
    os.path.realpath(__file__)
)


"""
    configer
"""
config = configparser.ConfigParser()
current_dir = os.path.dirname(os.path.realpath(__file__))
config.read(os.path.join(current_dir, 'config.ini'), encoding="utf-8")

