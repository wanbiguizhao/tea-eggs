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
DATABASE_URL = config.get('database','SQLALCHEMY_DATABASE_URL')
BECOME_PASS = config.get('ansible','become_pass')
ANSIBLE_SSH_USER = config.get('ansible','ansible_ssh_user')
ANSIBLE_SSH_PORT = config.get('ansible','ansible_ssh_port')
ANSIBLE_SSH_PRIVATE_KEY_FILE = config.get('ansible','ansible_ssh_private_key_file')
TEST_ANSIBLE_VARS={   
          'ansible_ssh_user' : 'ops',  
          'ansible_ssh_port' : '22222',  
          'ansible_ssh_private_key_file' : "/Users/mi/git/tea-eggs/taskService/test/sshkey/eggs_rsa"  
          }
