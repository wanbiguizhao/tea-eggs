# -*- coding: utf-8 -*-
'''
	用于检测代码关键文件和目录是否存在
'''
import sys
import pathlib
import configparser
_project_root = str(pathlib.Path(__file__).resolve().parents[1])
sys.path.append(_project_root)
config = configparser.ConfigParser()
def check_config():
    '''
        检测配置文件是否存在
    '''
	config_path = pathlib.Path("../config.ini")
	if config_path.exists() and config_path.is_file():
		print('*' * 15 +'配置文件存在:{config_path}'.format(config_path=config_path) + '*' * 15 + 'OK')
		return True
	else:
		print('*' * 15 + "配置文件缺失，需创建:{config_path}".format(config_path=config_path)+ '*' * 15 + 'Not found')
		return False
def check_yaml_path():
	#config.read("../config.ini")
	#yaml_path = config['yaml_file_path']['path']
	yaml_path = pathlib.Path('../YAML')
	if yaml_path.exists() and yaml_path.is_dir():
		print('*' * 15 +'存放yaml文件的文件夹存在:{yaml_path}'.format(yaml_path=yaml_path) + '*' * 15 + 'OK')
	else:
		print('*' * 15 +'存放yaml文件的文件夹缺失，需创建:{yaml_path}'.format(yaml_path=yaml_path) + '*' * 15 + 'Not found')

if __name__ == '__main__':
	check_config = check_config()
	if check_config is True:
		check_yaml_path()
