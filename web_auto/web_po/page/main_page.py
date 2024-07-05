"""
 
"""
from selenium.webdriver.common.by import By
from web_auto.web_po.base.base_page import BasePage
from web_auto.web_po.page.more_search_page import MoreSearchPage


class MainPage(BasePage):

    # 搜索按钮
    _SEARCH_BTN = By.CSS_SELECTOR, "#search-button"
    # 搜索框
    _SEARCH_INPUT = By.ID, "search-term"
    # 高级页面按钮
    _ADVANCED_SEARCH_BTN = By.CLASS_NAME, 'show-advanced-search'

    def open_main(self):
        # 进入首页
        self.open_url("https://ceshiren.com/")
        return self

    def goto_more_search_page(self, search_key):
        '''
        跳转到高级搜索页面
        :return:
        '''
        # 点击搜索按钮
        self.find_and_click(*self._SEARCH_BTN)
        # 输入搜索关键字
        ele_send = self.find_ele(*self._SEARCH_INPUT)
        ele_send.clear()
        ele_send.send_keys(search_key)
        # 点击进入高级搜索页面
        ele = self.wait_ele_locate(*self._ADVANCED_SEARCH_BTN)
        ele.click()
        # 跳转到高级搜索页面
        return MoreSearchPage(self.driver)