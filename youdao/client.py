#!/usr/bin/env python
#coding:utf-8
# Author        : tuxpy
# Email         : q8886888@qq.com.com
# Last modified : 2015-12-10 11:39:06
# Filename      : client.py
# Description   : 
from __future__ import print_function, unicode_literals

from youdao import (auth, notebook, api)

class Youdao(object):
    def __init__(self, username = None, password = None, auto_login = True):
        self.auth_manager = auth.AuthManager(username, password)
        if auto_login:
            self.auth_manager.login()
        self.is_logged = self.auth_manager.is_logged

        self.notebook_manager = notebook.NoteBookManager(self)

    def login(self, username = None, password = None):
        return self.auth_manager.login(username, password)

    def ls(self):
        return self.notebook_manager.ls()

    def ls_notebooks(self):
        return self.ls()

