#!/usr/bin/env python
# coding=utf-8

"""
<p>
测试接口
</p>
@author: hai ji
@file: test_interface.py
@date: 2022/9/7 
"""
import json

import allure
import pytest

from common.logger import log
from utils.load_yaml import read_testcase
from utils.request_utils import RequestUtil


@allure.epic("接口测试")
@allure.feature("接口测试")
class TestInterface(object):

    @allure.story("测试保存")
    @allure.title("测试一个接口")
    @pytest.mark.parametrize("args_name", read_testcase("demo/test_interface.yaml"))
    def test_01(self, args_name):
        with allure.step("获取需要的参数"):
            url = args_name['request']['url']
            method = args_name['request']['method']
            data = args_name['request']['data']
            headers = args_name['request']['headers']
            log.info("接的入参 %s " % data)
        with allure.step("发送请求"):
            res = RequestUtil('interface', 'url').send_request(method, url, data=json.dumps(data), headers=headers).text
        with allure.step("获取返回值"):
            res = json.loads(res)
            log.info("测试接口的返回值 %s" % res)
        # 这里我们时接口传入什么我们返回什么
        with allure.step("进行断言"):
            assert data == res
