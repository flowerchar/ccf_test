 
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager

from web_auto.web_po.utils.log_util import logger


class BasePage:

    def __init__(self, driver: WebDriver=None):
        logger.info(f"当前页面的 driver 为 {driver}")
        if driver == None:
            # 初始化 driver
            # 配置 driver
            # service = Service(executable_path=ChromeDriverManager().install())
            # 初始化 driver
            # self.driver = webdriver.Chrome(service=service)
            self.driver = webdriver.Chrome()
            # 设置隐式等待
            self.driver.implicitly_wait(15)
            # 最大化窗口
            self.driver.maximize_window()
        else:
            self.driver = driver


    def close_browser(self):
        '''
        关闭浏览器
        :return:
        '''
        logger.info("关闭浏览器")
        self.driver.quit()

    def open_url(self, url):
        '''
        打开页面
        :param url: 要打开页面的 url
        :return:
        '''
        info_text = f"打开页面的 url 为 {url}"
        self.driver.get(url)
        logger.info(info_text)


    def find_ele(self, by, value):
        '''
        定位单个元素
        :param by: 元素定位方式
        :param value: 元素定位表达式
        :return: 找到的元素对象
        '''
        info_text = f"定位单个元素，定位方式为 {by}, 定位表达式为 {value}"
        logger.info(info_text)
        try:
            ele = self.driver.find_element(by, value)
        except Exception as e:
            ele = None
            logger.info(f"单个元素没有找到 {e}")
            # 截图
            self.srceen_image()
            # 保存 pagesource
            self.save_page_source()
        return ele

    def find_eles(self, by, value):
        '''
        定位多个元素
        :param by: 元素定位方式
        :param value: 元素定位表达式
        :return: 找到的元素对象的列表
        '''
        logger.info(f"定位多个元素，定位方式为 {by}, 定位表达式为 {value}")
        try:
            ele_list = self.driver.find_elements(by, value)
        except Exception as e:
            ele_list = []
            logger.info(f"单个元素没有找到 {e}")
            # 截图
            self.srceen_image()
            # 保存 pagesource
            self.save_page_source()
        return ele_list

    def find_and_get_text(self, by, value):
        '''
        获取单个元素的文本属性
        :param by: 元素定位方式
        :param value: 元素定位表达式
        :return: 文本内容
        '''
        text_value = self.find_ele(by, value).text
        logger.info(f"元素的文本属性为 {text_value}")
        return text_value

    def find_and_click(self, by, value):
        '''
        查找单个元素并点击
        :param by: 元素定位方式
        :param value: 元素定位表达式
        '''
        self.find_ele(by, value).click()

    def ele_sendkeys(self, by, value, text):
        '''
        单个元素输入内容
        :param by: 元素定位方式
        :param value: 元素定位表达式
        :param text: 元素要输入的字符串
        '''
        ele = self.find_ele(by, value)
        # 先清空输入框
        ele.clear()
        # 输入内容
        logger.info(f"元素要输入的内容为 {text}")
        ele.send_keys(text)

    def wait_ele_locate(self, by, value, timeout=10):
        '''
        显式等待元素可以被定位
        :param by: 元素定位方式
        :param value: 元素定位表达式
        :param timeout: 等待时间
        :return: 定位到的元素对象
        '''
        logger.info(f"显式等待元素可以被定位，定位方式为 {by}, 定位表达式为 {value}")
        ele = WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located((by, value))
        )
        return ele

    def wait_ele_click(self, by, value, timeout=10):
        '''
        显式等待元素可以被点击
        :param by: 元素定位方式
        :param value: 元素定位表达式
        :param timeout: 等待时间
        :return: 定位到的元素对象
        '''
        logger.info(f"显式等待元素可以被点击，定位方式为 {by}, 定位表达式为 {value}")
        ele = WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable((by, value))
        )
        return ele

    def get_path(self, path_name):
        '''
        获取绝对路径
        :param path_name: 目录名称
        :return: 获取到的绝对路径
        '''
        # 获取当前⼯具⽂件所在的路径
        root_path = os.path.dirname(os.path.abspath(__file__))
        # 拼接当前要输出⽇志的路径
        log_dir_path = os.sep.join([root_path, '..', path_name])
        return log_dir_path

    def srceen_image(self):
        '''
        截图
        :return: 图片保存的路径
        '''
        # 截图命名
        if not os.path.exists('./../images'):
            os.mkdir('./../images')
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        image_name = f"{now_time}.png"
        # 拼接图片保存路径
        # windows image_path = f"{self.get_path('images')}\\{image_name}"
        image_path = f"{self.get_path('images')}\\{image_name}"
        logger.info(f"截图保存的路径为 {image_path}")
        # 截图
        self.driver.save_screenshot(image_path)
        return image_path

    def save_page_source(self):
        '''
        保存页面源码
        :return:
        '''
        # 文件命名
        if not os.path.exists('./../pagesource'):
            os.mkdir('./../pagesource')
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        pagesource_name = f"{now_time}.html"
        # 拼接文件保存路径
        # windows pagesource_path = f"{self.get_path('pagesource')}\\{pagesource_name}"
        pagesource_path = f"{self.get_path('pagesource')}\\{pagesource_name}"
        logger.info(f"page source 文件保存的路径为 {pagesource_path}")
        # 获取 page source 写入文件
        with open(pagesource_path, "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)
        return pagesource_path



