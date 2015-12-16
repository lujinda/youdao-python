#!/usr/bin/env python
#coding:utf-8
# Author        : tuxpy
# Email         : q8886888@qq.com.com
# Last modified : 2015-12-10 10:08:33
# Filename      : util.py
# Description   : 
from __future__ import print_function, unicode_literals
import hashlib
from functools import wraps
import re
import HTMLParser

def md5(s):
    hash_instance = hashlib.md5()
    hash_instance.update(s)

    return hash_instance.hexdigest()

def utf8(s):
    if isinstance(s, unicode):
        return s.encode('utf-8')
    return s

def _generate_cache_key(cls, func, args, kwargs):
    key = cls.__class__.__name__ + func.__name__
    key += str(args) +  str(kwargs)
    return key


def cache_self(func):
    @wraps(func)
    def wrap(self, *args, **kwargs):
        key = '_' + _generate_cache_key(self, func, args, kwargs)
        if hasattr(self, key):
            return getattr(self, key)
        else:
            value = func(self, *args, **kwargs)
            setattr(self, key, value)
            return value

    return wrap

def get_text_from_html(html):
    re_html_tag_text = re.compile(r'<\s*?(script|style).*?>(.*?)<\s*?/(\1)\s*?>', re.M|re.S)
    re_html_tag = re.compile(r'<(.+?)>', re.M | re.S)
    re_space = re.compile(r'(\s+)');
    html = re_html_tag_text.sub('', html)
    html = re_html_tag.sub(b' ', html)
    html = re_space.sub(lambda m: m.group(1)[0], html)

    html = HTMLParser.HTMLParser().unescape(html.strip())

    return html

def get_images_from_html(html):
    return re.findall('<img src="(.+?)"', html, re.U)

