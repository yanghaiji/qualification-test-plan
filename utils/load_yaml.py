#!/usr/bin/env python
# coding=utf-8

"""
<p>
yaml 相关操作
</p>
@author: hai ji
@file: load_yaml.py
@date: 2022/8/31
"""
import os
import pathlib

import yaml


# 读取
def read_yaml():
    with open(os.getcwd() + '/xx.yaml', mode='r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value


# 写入
def write_yaml(data):
    with open(os.getcwd() + '/xx.yaml', mode='a', encoding='utf-8') as f:
        yaml.dump(data, stream=f, allow_unicode=True)


# 清空
def clear_yaml():
    with open(os.getcwd() + '/xx.yaml', mode='w', encoding='utf-8') as f:
        f.truncate()


# 读取yaml
def read_testcase(yaml_name):
    path = str(pathlib.Path(os.getcwd() + '/data/', yaml_name))
    with open(path, mode='r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
    return value


# 读取config.yml文件
def read_config_file(base, base_url):
    path = str(pathlib.Path(os.getcwd() + '/config/application.yaml'))
    with open(path, encoding="utf-8") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[base][base_url]

