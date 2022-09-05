#!/usr/bin/env python
# coding=utf-8

"""
<p>
全局配置
</p>
@author: hai ji
@file: times.py
@date: 2022/8/31
"""
import logging

import allure
import pytest
from selenium import webdriver

driver = None


@pytest.fixture(scope='session', autouse=True)
def drivers(request):
    global driver
    if driver is None:
        driver = webdriver.Chrome()
        driver.maximize_window()

    def fn():
        driver.quit()

    request.addfinalizer(fn)
    return driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # 什么时候去识别用例的执行结果呢？
    # 后置处理 yield：表示测试用例执行完了
    outcome = yield
    rep = outcome.get_result()  # 获取测试用例执行完成之后的结果
    if rep.when == 'call' and rep.failed:  # 判断用例执行情况：被调用并且失败
        # 实现失败截图并添加到allure附件。截图方法需要使用driver对象，想办法把driver传过来
        # 如果操作步骤过程中有异常，那么用例失败，在这里完成截图操作
        img = driver.get_screenshot_as_png()
        # 将截图展示在allure测试报告上
        allure.attach(img, '失败截图', allure.attachment_type.PNG)


# 往allure里面写日志
class AllureLoggingHandler(logging.Handler):
    def log(self, message):
        with allure.step('{}'.format(message)):
            pass

    def emit(self, record):
        self.log("{}-{}-: {}".format(record.asctime, record.levelname, record.getMessage()))


class AllureCatchLogs:
    def __init__(self):
        self.rootlogger = logging.getLogger()
        self.allurehandler = AllureLoggingHandler()

    def __enter__(self):
        if self.allurehandler not in self.rootlogger.handlers:
            self.rootlogger.addHandler(self.allurehandler)

    def __exit__(self, exc_type, exc_value, traceback):
        self.rootlogger.removeHandler(self.allurehandler)
