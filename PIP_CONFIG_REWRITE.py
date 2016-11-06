# -*- coding: utf-8 -*-
# @Author: rhys
# @Date:   2016-11-06 13:41:07
# @Last Modified by:   rhys
# @Last Modified time: 2016-11-06 14:14:36


"""
Description: 
when I use 'pip install ',  for the poor connection, it always timeout in China.
The script writen in python to write the configuration of pip, using mirror image 
source in China(eg. pypi.doubanio.com) 
"""

import os


INFO_TO_WRITE = '''[global]  
index-url = https://pypi.doubanio.com/simple/  
[install]  
trusted-host=pypi.doubanio.com  
disable-pip-version-check = true  
timeout = 6000  
'''

DIR_NAME = '.pip'

CONF_FILE_NAME = 'pip.conf'

PIP_CONFIG_PATH = os.path.join(os.environ['HOME'], DIR_NAME)


if not os.path.exists(PIP_CONFIG_PATH):
	os.mkdir(PIP_CONFIG_PATH)

with open(os.path.join(PIP_CONFIG_PATH, CONF_FILE_NAME), 'w+') as f:
	f.write(INFO_TO_WRITE)

print('rewrite pip configuration successfully')