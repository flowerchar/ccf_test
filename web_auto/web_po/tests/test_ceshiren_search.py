"""
 
"""
import pytest
from web_auto.web_po.page.main_page import MainPage


class TestCeshirenSearch:

    def setup_method(self):
        self.main = MainPage().open_main()

    def teardown_method(self):
        # driver 退出
        self.main.close_browser()

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
        more_search = self.main.goto_more_search_page(search_key)
        # 获取高级搜索页面第一个帖子标题
        search_text = more_search.get_search_result_title()
        # 获取帖子详情页面 title
        result_page_title = more_search.goto_posts_page().get_page_title()
        # 断言
        assert search_text in result_page_title

    # 为空
    def test_search_none(self):
        search_key = ""
        # 获取为空搜索时的提示信息
        msg = self.main.goto_more_search_page(search_key).get_none_msg()
        # 断言
        assert msg == "您的搜索词过短。"

    # 无搜索结果
    def test_search_no_result(self):
        search_key = "ooooooooooo"
        # 获取无搜索结果时的提示信息
        msg = self.main.goto_more_search_page(search_key).get_no_result_msg()
        # 断言
        assert msg == "找不到结果。"