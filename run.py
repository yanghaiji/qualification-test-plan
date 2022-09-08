#!/usr/bin/env python
# coding=utf-8

"""
<p>
项目启动类
</p>
@author: hai ji
@file: run.py
@date: 2022/9/7 
"""
import os

import pytest

from config.conf import cm

if __name__ == '__main__':
    # 当前路径(使用 abspath 方法可通过dos窗口执行)
    current_path = cm.BASE_DIR
    # json报告路径
    json_report_path = os.path.join(current_path, 'report/json')
    # html报告路径
    html_report_path = os.path.join(current_path, 'report/html')

    # 执行pytest下的用例并生成json文件
    pytest.main(['-s', '-v', '--alluredir=%s' % json_report_path, '--clean-alluredir'])
    # 把json文件转成html报告 要以管理员运行 pycharm
    # print('allure generate %s -o %s --clean' % (json_report_path, html_report_path))
    os.system('allure generate %s -o %s --clean' % (json_report_path, html_report_path))