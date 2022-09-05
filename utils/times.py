#!/usr/bin/env python
# coding=utf-8

"""
<p>
时间处理工具
</p>
@author: hai ji
@file: times.py
@date: 2022/8/31 
"""

import datetime
import time
from functools import wraps


def timestamp():
    """时间戳"""
    return time.time()


def dt_fmt(fmt="%Y%m%d"):
    """
    datetime格式化时间
    :param fmt "%Y%m%d %H%M%S
    """
    return datetime.datetime.now().strftime(fmt)


def sleep(seconds=1.0):
    """
    睡眠时间
    """
    time.sleep(seconds)


def running_time(func):
    """函数运行时间"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = timestamp()
        res = func(*args, **kwargs)
        print("校验元素done！用时%.3f秒！" % (timestamp() - start))
        return res

    return wrapper


if __name__ == '__main__':
    print(dt_fmt())
