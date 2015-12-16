#!/usr/bin/env python
#coding:utf-8
# Author        : tuxpy
# Email         : q8886888@qq.com.com
# Last modified : 2015-12-09 17:14:29
# Filename      : auth.py
# Description   : 
from __future__ import print_function, unicode_literals

from youdao import (urls, e, request, util)
from youdao.api import api_request

__all__ = ['AuthManager']

cookie_manager = request.CookieManager()

class AuthManager(object):
    def __init__(self, username = None, password = None):
        self.username = username
        self.password = password

    def login(self, username = None, password = None):
        username = username or self.username
        password = password or self.password
        if not (username and password):
            raise e.LoginError('username or password is empty')

        response = api_request(urls.login_valid, data = {
            'username'      :       username,
            'password'      :       util.md5(password),
            'product'       :       'YNOTE',
            'tp'            :       'urstoken',
            'cf'            :       '6',
            'fr'            :       '1',
            'systemName'    :       'linux',
            'deviceType'    :       'linuxPC',
            'er'            :       'http://note.youdao.com/signIn//loginCallback.html',
            'ru'            :       'http://note.youdao.com/signIn//loginCallback.html',
            })
        if not self.is_logged():
            raise e.LoginError('user valid failed')
        api_request(urls.user_cstk)

    def is_logged(self):
        return bool(cookie_manager.cookies.get('YNOTE_SESS'))

