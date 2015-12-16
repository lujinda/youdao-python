#!/usr/bin/env python
#coding:utf-8
# Author        : tuxpy
# Email         : q8886888@qq.com.com
# Last modified : 2015-12-10 14:23:01
# Filename      : notebook.py
# Description   : 
from __future__ import print_function, unicode_literals

from youdao import (api, urls, note, util)

class NoteBook(object):
    def __init__(self, name, guid, size):
        self.guid = guid
        self.name = name
        self.size = size

    def ls(self):
        """list the notebook all notes"""
        response = api.api_request(urls.list_notes, 'POST', 
                data = {
                    'b'     :   '0',
                    'l'     :   '200',
                    'm'     :   '0',
                    'nb'    :   self.guid,
                    'v'     :   '-1',
                    })
        total, records = response
        notes = []
        for record in records:
            _note = note.Note(self, record['tl'], record['p'])
            notes.append(_note)

        return notes

    def __repr__(self):
        return util.utf8("< {name} : {guid} note_total: {size} >".format(
                name = self.name, guid = self.guid, size = self.size))

class NoteBookManager(object):
    def __init__(self, client):
        self.client = client

    def ls(self):
        response = api.api_request(urls.list_notebooks)
        notebooks = []
        for record in response:
            if not record['tl']:
                continue
            notebook = NoteBook(record['tl'],
                    record['p'],
                    record['nn'])
            notebooks.append(notebook)

        return notebooks

