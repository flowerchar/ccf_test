 
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager


class TestCeshirenSearch:

    def setup_method(self):
        # 打开 Chrome 浏览器 data; 空白页面
        # service = Service(executable_path=ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(service=service)
        self.driver = webdriver.Chrome()
        # 隐式等待，全局等待时间
        self.driver.implicitly_wait(10)
        # --------------- 1. 打开测试人论坛 ---------------
        self.driver.get("https://ceshiren.com/")
        self.driver.maximize_window()

    def teardown_method(self):
        # driver 退出
        self.driver.quit()

    def close_msg(self):
        # 处理可能出现的弹窗
        if "确定" in self.driver.page_source:
            self.driver.find_element(By.XPATH, '//*[text()="确定"]').click()

    # parametrize 只能在test_ python文件中的test_开头的方法上使用
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
        # --------------- 2. 点击搜索按钮 ---------------
        self.driver.find_element(By.CSS_SELECTOR, "#search-button").click()
        # --------------- 3. 输入搜索关键字---------------
        ele_send = self.driver.find_element(By.ID, "search-term")
        ele_send.clear()
        ele_send.send_keys(search_key)
        # --------------- 4. 点击进入高级搜索页面 ---------------
        ele = WebDriverWait(self.driver, 10, 0.2).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'show-advanced-search'))
        )
        ele.click()

        # 显示等待，等待搜索结果可以被点击的时候再进行操作
        search_ele = WebDriverWait(self.driver, 5, 0.2).until(
            expected_conditions.element_to_be_clickable((By.CLASS_NAME, "search-link"))
        )
        # 高级搜索页面下第一个标题的文本获取
        search_text = search_ele.text
        print(f"高级搜索页面下第一个标题的文本为：{search_text}")

        # 处理可能出现的弹窗
        self.close_msg()

        # --------------- 5. 点击高级搜索页面下第一个标题 ---------------
        search_ele.click()
        # 显式等待帖子标题加载完毕
        WebDriverWait(self.driver, 5, 0.1).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//*[@class="fancy-title"]'))
        )
        # --------------- 6. 获取页面标题 断言 ---------------
        # 高级搜索页面下第一个标题的文本 == 页面跳转成功的title
        result_page_title = self.driver.title
        print(f"跳转页面的标题为：{result_page_title}")
        assert search_text in result_page_title

    # 为空
    def test_search_none(self):
        # --------------- 2. 点击搜索按钮 ---------------
        self.driver.find_element(By.CSS_SELECTOR, "#search-button").click()
        # --------------- 3. 输入搜索关键字---------------
        ele_send = self.driver.find_element(By.ID, "search-term")
        ele_send.clear()
        ele_send.send_keys("")

        # 处理可能出现的弹窗
        self.close_msg()

        # --------------- 4. 点击进入高级搜索页面 ---------------
        ele = WebDriverWait(self.driver, 10, 0.2).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'show-advanced-search'))
        )
        ele.click()
        # 点击搜索按钮
        self.driver.find_element(By.CSS_SELECTOR, ".search-cta").click()
        # --------------- 5. 断言 ---------------
        msg = self.driver.find_element(By.XPATH, "//*[@class='fps-invalid']").text
        print(f"提示信息为：{msg}")
        assert msg == "您的搜索词过短。"

    # 无搜索结果
    def test_search_no_result(self):
        # --------------- 2. 点击搜索按钮 ---------------
        self.driver.find_element(By.CSS_SELECTOR, "#search-button").click()
        # --------------- 3. 输入搜索关键字---------------
        ele_send = self.driver.find_element(By.ID, "search-term")
        ele_send.clear()
        ele_send.send_keys("ooooooooooo")

        # 处理可能出现的弹窗
        self.close_msg()

        # --------------- 4. 点击进入高级搜索页面 ---------------
        ele = WebDriverWait(self.driver, 10, 0.2).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'show-advanced-search'))
        )
        ele.click()
        # 点击搜索按钮
        self.driver.find_element(By.CSS_SELECTOR, ".search-cta").click()
        # --------------- 5. 断言 ---------------
        msg = self.driver.find_element(By.CSS_SELECTOR, ".loading-container > h3").text
        print(f"提示信息为：{msg}")
        assert msg == "找不到结果。"