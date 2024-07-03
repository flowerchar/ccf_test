"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

import pytest

from interface_auto.interface_frame.apis.ceshiren_search import CeshirenSearch


class TestCeshirenSearch:

    def setup_class(self):
        # 实例化搜索类
        self.ceshiren_search = CeshirenSearch()

    def teardown_method(self):
        time.sleep(1)

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
        r = self.ceshiren_search.search(params)
        results = r.json().get("posts")
        print(f"响应结果中 posts 结果数量为 {results}")
        assert results != None

    # 搜索关键词为空
    def test_search_none(self):
        params = {
            "q": "",
            "page": 1
        }
        r = self.ceshiren_search.search(params)
        print(r.text)
        assert r.json().get("grouped_search_result") == None

    # 搜索结果为空
    def test_search_no_result(self):
        params = {
            "q": "ooooooooooo",
            "page": 1
        }
        r = self.ceshiren_search.search(params)
        print(r.text)
        assert r.json().get("posts") == []

    # 缺少请求参数 q
    def test_search_noq(self):
        params = {
            "page": 1
        }
        r = self.ceshiren_search.search(params)
        print(r.text)
        assert r.json().get("grouped_search_result") == None

    # 缺少请求参数 page
    def test_search_nopage(self):
        params = {
            "q": "测试用例"
        }
        r = self.ceshiren_search.search(params)
        print(r.text)
        results = r.json().get("posts")
        print(f"响应结果中 posts 结果数量为 {results}")
        assert results != None

    # 不传请求参数
    def test_search_noparams(self):
        r = self.ceshiren_search.search(None)
        print(r.text)
        assert r.json().get("grouped_search_result") == None


