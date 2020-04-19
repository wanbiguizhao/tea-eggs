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

YAML_PATH = config.get('yaml','BASICE_PATH')
HOSTS_PATH = config.get('hosts','BASICE_PATH')
DATABASE = config.get('database','SQLALCHEMY_DATABASE_URL')
BECOME_PASS = config.get('ansible','become_pass')
