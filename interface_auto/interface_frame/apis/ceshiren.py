"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from interface_auto.interface_frame.apis.base_api import BaseApi

# 定义产品特性

class Ceshiren(BaseApi):

    def __init__(self):
        self.base_url = "https://ceshiren.com"
