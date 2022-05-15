"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import yaml

from prac_prepare.page_object.base_page import BasePage
from prac_prepare.utils.log_utils import logger


class LoginPage(BasePage):
    """登录页"""

    _BASE_URL = "https://work.weixin.qq.com/wework_admin/frame"

    def login(self):
        logger.info("登录")
        # 一、登录
        # 1、访问企业微信首页Domain
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 2、获取本地的cookie
        with open("../data/cookies.yaml", "r") as f:
            cookies = yaml.safe_load(f)
        # 3、植入cookie
        for ck in cookies:
            self.driver.add_cookie(ck)
        # 4、访问企业微信首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        from prac_prepare.page_object.home_page import HomePage
        return HomePage(self.driver)