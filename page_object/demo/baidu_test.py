#!/usr/bin/env python
# coding=utf-8

"""
<p>
用户搜索
</p>
@author: hai ji
@file: baidu_test.py
@date: 2022/8/31 
"""
from common.readelement import Element
from page.webpage import WebPage

search = Element('demo/demo')


class SearchPage(WebPage):
    """搜索类"""

    def input_search(self, content):
        """输入搜索"""
        self.input_text(search['inputelment'], txt=content)

    def click_search(self):
        """点击搜索"""
        self.is_click(search['click_search'])
