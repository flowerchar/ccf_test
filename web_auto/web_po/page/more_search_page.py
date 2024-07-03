"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium.webdriver.common.by import By

from web_auto.web_po.base.base_page import BasePage
from web_auto.web_po.page.posts_page import PostsPage
from web_auto.web_po.utils.log_util import logger


class MoreSearchPage(BasePage):

    # 确定按钮
    _ACCEPT_BTN = By.XPATH, '//*[text()="确定"]'
    # 搜索结果
    _SEARCH_RESULT = By.CLASS_NAME, "search-link"
    # 搜索按钮
    _SEARCH_BTN = By.CSS_SELECTOR, ".search-cta"
    # 为空提示信息
    _NONE_MSG = By.XPATH, "//*[@class='fps-invalid']"
    # 无搜索结果提示信息
    _NO_RESULT_MSG = By.CSS_SELECTOR, ".loading-container > h3"

    def close_msg(self):
        '''
        关闭可能出现的弹窗
        :return:
        '''
        if "确定" in self.driver.page_source:
            self.find_and_click(*self._ACCEPT_BTN)

    def get_search_result_title(self):
        '''
        获取搜索结果的第一个帖子的标题
        :return:
        '''
        # 显示等待，等待搜索结果可以被点击的时候再进行操作
        search_ele = self.wait_ele_click(*self._SEARCH_RESULT)
        self.close_msg()
        # 高级搜索页面下第一个标题的文本获取
        search_text = search_ele.text
        logger.info(f"高级搜索页面下第一个标题的文本为：{search_text}")
        return search_text

    def goto_posts_page(self):
        '''
        跳转到帖子详情页
        :return:
        '''
        # 显示等待，等待搜索结果可以被点击的时候再进行操作
        search_ele = self.wait_ele_click(*self._SEARCH_RESULT)
        self.close_msg()
        # 点击高级搜索页面下第一个标题
        search_ele.click()
        return PostsPage(self.driver)

    def get_none_msg(self):
        '''
        获取搜索关键词为空的提示信息
        :return:
        '''
        # 点击搜索按钮
        self.find_and_click(*self._SEARCH_BTN)
        # --------------- 5. 断言 ---------------
        msg = self.find_and_get_text(*self._NONE_MSG)
        logger.info(f"提示信息为：{msg}")
        return msg

    def get_no_result_msg(self):
        '''
        获取没有搜索结果的提示信息
        :return:
        '''
        # 点击搜索按钮
        self.find_and_click(*self._SEARCH_BTN)
        # 获取没有搜索结果的提示信息
        msg = self.find_and_get_text(*self._NO_RESULT_MSG)
        logger.info(f"提示信息为：{msg}")
        return msg
