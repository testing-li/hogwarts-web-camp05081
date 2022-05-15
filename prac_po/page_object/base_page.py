"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """与浏览器driver交互"""

    _BASE_URL = ""

    # 构造方法
    def __init__(self, base_driver=None):
        if base_driver:
            self.driver = base_driver
        else:
            # 实例化
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

        if not self.driver.current_url.startswith("http"):
            self.driver.get(self._BASE_URL)

    def do_find(self, by, locator=None):
        """获取单个元素"""
        if locator:
            return self.driver.find_element(by, locator)
        else:
            return self.driver.find_element(*by)

    def do_finds(self,by, locator=None):
        """获取多个元素"""
        if locator:
            return self.driver.find_elements(by, locator)
        else:
            return self.driver.find_elements(*by)

    def do_send_keys(self, value, by, locator=None):
        """输入文本"""
        ele = self.do_find(by, locator)
        ele.clear()
        ele.send_keys(value)

    def do_quit(self):
        """退出浏览器"""
        self.driver.quit()

    def wait_visible(self, locator: tuple):
        """等待可见"""
        return WebDriverWait(self.driver, 10)\
            .until(expected_conditions.visibility_of_element_located(locator))
