"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from time import sleep

import pytest
import requests


class TestCeshirenSearch:

    def setup_class(self):
        self.base_url = "https://ceshiren.com"
        # 搜索接口 url
        self.search_url = f"{self.base_url}/search"

    def setup_method(self):
        sleep(1)

    # 正向用例
    @pytest.mark.parametrize(
        "search_key",
        [
            "pytest",
            "面试题",
            "a",
            "appium desktop连接真机，start session，出现报错，手机上appium setting打开闪退，但是进程显示是进行中。报错内容：An unknown server-side error occurred while processing the command. Original error: Could not find a connected Android device in 20364ms.",
        ]
    )
    def test_search(self, search_key):
        params = {
            "q": search_key,
            "page": 1
        }
        headers = {
            "Accept": "application/json"
        }
        r = requests.request(method="GET", url=self.search_url, params=params, headers=headers)
        print(r.text)
        results = len(r.json().get("posts"))
        print(f"响应结果中 posts 结果数量为 {results}")
        assert results != 0

    # 搜索关键词为空
    def test_search_none(self):
        params = {
            "q": "",
            "page": 1
        }
        headers = {
            "Accept": "application/json"
        }
        r = requests.request(method="GET", url=self.search_url, params=params, headers=headers)
        print(r.text)
        # print(r.json().get("grouped_search_result"), type(r.json().get("grouped_search_result")))
        assert r.json().get("grouped_search_result") == None

    # 搜索结果为空
    def test_search_no_result(self):
        params = {
            "q": "ooooooooooo",
            "page": 1
        }
        headers = {
            "Accept": "application/json"
        }
        r = requests.request(method="GET", url=self.search_url, params=params, headers=headers)
        print(r.text)
        assert r.json().get("posts") == []

    # 缺少请求参数 q
    def test_search_noq(self):
        params = {
            "page": 1
        }
        headers = {
            "Accept": "application/json"
        }
        r = requests.request(method="GET", url=self.search_url, params=params, headers=headers)
        print(f"aaaaa{r.text}")
        # print(r.json().get("grouped_search_result"))
        assert r.json().get("grouped_search_result") == None

    # 缺少请求参数 page
    def test_search_nopage(self):
        params = {
            "q": "测试用例"
        }
        headers = {
            "Accept": "application/json"
        }
        r = requests.request(method="GET", url=self.search_url, params=params, headers=headers)
        print(r.text)
        results = len(r.json().get("posts"))
        print(f"响应结果中 posts 结果数量为 {results}")
        assert results != 0

    # 不传请求参数
    def test_search_noparams(self):
        headers = {
            "Accept": "application/json"
        }
        r = requests.request(method="GET", url=self.search_url, headers=headers)
        print(r.text)
        assert r.json().get("grouped_search_result") == None


