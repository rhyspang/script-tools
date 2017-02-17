#!/usr/bin/env python2.7

# -*- coding: utf-8 -*-
# @Author: rhys
# @Date:   2016-11-06 13:41:07
# @Last Modified by:   stoonejames
# @Last Modified time: 2017-02-17 21:12:59


"""
Description: 
when I use 'pip install ',  for the poor connection, it always timeout in China.
The script writen in python to write the configuration of pip, using mirror image 
source in China(eg. http://pypi.douban.com/simple) 
"""

import os


INFO_TO_WRITE = '''[global]  
index-url = http://pypi.douban.com/simple/  
[install]  
trusted-host=http://pypi.douban.com/ 
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
