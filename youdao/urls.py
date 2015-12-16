#!/usr/bin/env python
#coding:utf-8
# Author        : tuxpy
# Email         : q8886888@qq.com.com
# Last modified : 2015-12-09 17:06:25
# Filename      : urls.py
# Description   : 
from __future__ import print_function, unicode_literals

login_valid = '/login/acc/login?app=web'
user_cstk = '/yws/mapi/user?keyfrom=web&method=get'
list_notebooks = '/yws/mapi/filemeta?method=get&keyfrom=web&dp=1'
list_notes = '/yws/mapi/search?method=get&keyfrom=web'
note_data = '/yws/mapi/file?method=get&keyfrom=web&dp=0&v=-1'

