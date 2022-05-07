"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

import yaml
from selenium import webdriver


class TestCookieLogin:

    def setup_class(self):
        """前置动作"""
        self.driver = webdriver.Chrome()

    def teardown_class(self):
        """后置处理"""
        self.driver.quit()

    def test_save_cookies(self):
        """获取cookie"""

        # 1、访问企业微信首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        # 2、直接等待，手工扫码
        time.sleep(10)

        # 3、登录成功后，获取cookie
        cookies = self.driver.get_cookies()

        # 4、保存cookie
        with open("../data/cookies.yaml", "w") as f:
            yaml.safe_dump(data=cookies, stream=f)

    def test_add_cookie(self):
        """植入cookie"""

        # 1、访问企业微信首页 CookieDomain
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        # 2、获取本地 cookies
        with open("../data/cookies.yaml", "r") as f:
            cookies = yaml.safe_load(f)

        # 3、植入cookies
        for ck in cookies:
            self.driver.add_cookie(ck)

        # 4、访问企业微信首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
