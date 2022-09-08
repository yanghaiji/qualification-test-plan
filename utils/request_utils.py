"""
自定义request
"""

import requests

from common.logger import Logger, log
from utils.load_yaml import read_config_file


class RequestUtil:
    # 全局变量
    sess = requests.session()

    def __init__(self, base, base_url):
        self.base_url = read_config_file(base, base_url)

    def send_request(self, method, url, **kwargs):
        """
        发送请求，**kwargs表示可变长度的字典
        :param method: 请求方法
        :param url:  url
        :param kwargs: 参数
        :return:
        """
        self.base_url = self.base_url + url
        log.info("url 预处理 >>>>>>> " + self.base_url)
        method = str(method).lower()
        res = RequestUtil.sess.request(method=method, url=self.base_url, **kwargs)
        return res
