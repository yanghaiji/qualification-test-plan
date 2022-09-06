#!/usr/bin/env python
# coding=utf-8

"""
<p>
测试配置
</p>
@author: hai ji
@file: test_demo.py
@date: 2022/8/31 
"""
import re

import allure
import pytest

from common.logger import log
from page_object.demo.baidu_test import SearchPage
from utils.load_yaml import read_config_file

url = read_config_file("base", "url")


@allure.feature("测试项目")
class TestSearch:

    @pytest.fixture(scope='function', autouse=True)
    def open_baidu(self, drivers):
        """打开百度"""
        search = SearchPage(drivers)
        with allure.step("step1：打开登录首页"):
            search.get_url(url)

    @allure.title("第一个测试用例")
    def test_001(self, drivers):
        """搜索"""
        search = SearchPage(drivers)
        with allure.step("step2:输入搜索内容"):
            search.input_search("selenium")
        with allure.step("step3:确认搜素"):
            search.click_search()
        with allure.step("step4:获取反回值"):
            result = re.search(r'selenium', search.get_source)
        log.info("页面返回值 %s" % result)
        assert result

    @allure.title("测试失败后截图的操作")
    def test_002(self, drivers):
        """搜索"""
        search = SearchPage(drivers)
        with allure.step("step2:输入搜索内容"):
            search.input_search("selenium")
        with allure.step("step3:确认搜素"):
            search.click_search()
        with allure.step("step4:获取反回值"):
            result = re.search(r'Java有货交流群，联系小编', search.get_source)
        log.info("页面返回值 %s" % result)
        assert result
