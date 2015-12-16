#!/usr/bin/env python
#coding:utf-8
# Author        : tuxpy
# Email         : q8886888@qq.com.com
# Last modified : 2015-12-09 17:02:17
# Filename      : api.py
# Description   : 
from __future__ import print_function, unicode_literals
from youdao import request, config
import urlparse

__all__ = ['api_request']

cookie_manager = request.CookieManager()

def api_request(path, method = 'GET', data = None, headers = None):
    data = data or {}
    cstk = cookie_manager.cookies.get('YNOTE_CSTK')
    if cstk:
        data['cstk'] = cstk
    api_url = urlparse.urljoin(config.HOST, path) # 当path 为绝对路径时,就可以借用urljoin来处理,会返回path返回 
    request_method = getattr(request, method.lower())
    response = request_method(api_url, data = data, auto_redirect = True)
    return response.json() or response.text

