"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium.webdriver.common.by import By
from web_auto.web_po.base.base_page import BasePage


class PostsPage(BasePage):

    # 帖子标题
    _POSTS_TITLE = By.XPATH, '//*[@class="fancy-title"]'

    def get_page_title(self) -> str:
        # 显式等待帖子标题加载完毕
        self.wait_ele_locate(*self._POSTS_TITLE)
        # 获取页面标题断言
        result_page_title = self.driver.title
        print(f"跳转页面的标题为：{result_page_title}")
        return result_page_title