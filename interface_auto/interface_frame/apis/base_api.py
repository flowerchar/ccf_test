"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import requests

from interface_auto.interface_frame.utils.log_util import logger


class BaseApi:

    def send_api(self, req):
        '''
        对 requests 进行二次封装
        :return: 接口响应
        '''
        # req = {
        #     "method": "get",
        #     "url": "xxxxx",
        #     "params": {},
        #     "json": {}
        # }
        # 等同于 requests.request(method="get", url="xxxxx", params={}, json={})
        logger.debug(f"请求数据为==========>{req}")
        r = requests.request(**req)
        logger.debug(f"响应数据为==========>{r.text}")
        return r
