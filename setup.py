#!/usr/bin/env python
#coding:utf-8
# Author        : tuxpy
# Email         : q8886888@qq.com.com
# Last modified : 2015-12-10 15:55:24
# Filename      : setup.py
# Description   : 
from distutils.core import setup
import youdao

setup(
        name = 'youdao-python',
        version = str(youdao.version),
        author = 'moment-x',
        author_email = 'q8886888@qq.com',
        license = 'GPL3',
        description = 'youdao note third party sdk',
        packages = [
            'youdao',
            ],
        )

