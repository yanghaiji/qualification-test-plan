#!/usr/bin/env python
# coding=utf-8

"""
<p>
日志封装
</p>
@author: hai ji
@file: logger.py
@date: 2022/8/31 
"""
import logging

from config.conf import cm


class Logger(object):

    def __init__(self):
        self.log_name = cm.log_file
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.DEBUG)

        self.formater = logging.Formatter('[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')

        self.filelogger = logging.FileHandler(self.log_name, mode='a', encoding="UTF-8")
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.INFO)
        self.filelogger.setLevel(logging.DEBUG)
        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)


log = Logger().logger

if __name__ == '__main__':
    log.info('hello world')
