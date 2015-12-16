#!/usr/bin/env python
#coding:utf-8
# Author        : tuxpy
# Email         : q8886888@qq.com.com
# Last modified : 2015-12-10 11:40:41
# Filename      : test.py
# Description   : 
from __future__ import print_function, unicode_literals
from youdao import client

if __name__ == "__main__":
    youdao = client.Youdao('*', '*')
    assert youdao.is_logged(), 'user must login'
    notebooks = youdao.ls()
    for notebook in notebooks:
        print(notebook.name)
        for note in notebook.ls():
            print(note.data.images[0].url)

