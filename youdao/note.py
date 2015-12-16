#!/usr/bin/env python
#coding:utf-8
# Author        : tuxpy
# Email         : q8886888@qq.com.com
# Last modified : 2015-12-10 14:40:57
# Filename      : note.py
# Description   : 
from __future__ import print_function, unicode_literals
from youdao import (util, api, urls)

class NoteImage(object):
    def __init__(self, url):
        self.url = url

    @property
    @util.cache_self
    def data(self):
        return api.api_request(self.url)

class NoteData(object):
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @property
    @util.cache_self
    def text(self):
        return util.get_text_from_html(self.raw_data)

    @property
    @util.cache_self
    def images(self):
        image_urls = util.get_images_from_html(self.raw_data)
        if not image_urls:
            return []
        return [NoteImage(image_url) for image_url in image_urls]

class Note(object):
    def __init__(self, notebook, title, guid):
        self.notebook = notebook
        self.title = title
        self.guid = guid

    def __repr__(self):
        return util.utf8("< {notebook_name} -> {title} : {guid} >".format(
            notebook_name = self.notebook.name, title = self.title, guid = self.guid))

    @property
    @util.cache_self
    def data(self):
        response = api.api_request(urls.note_data,
                data = {'p': self.guid})
        return NoteData(response)

