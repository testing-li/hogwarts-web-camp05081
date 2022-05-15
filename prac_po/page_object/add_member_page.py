"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium.webdriver.common.by import By

from prac_po.page_object.base_page import BasePage
from prac_po.utils.log_utils import logger


class AddMemberPage(BasePage):

    __INPUT_USERNAME = (By.ID, "username")
    __INPUT_ACCTID = (By.ID, "memberAdd_acctid")
    __INPUT_MOBILE = By.ID, "memberAdd_phone"
    __BTN_SAVE = (By.CSS_SELECTOR, "a.qui_btn.ww_btn.js_btn_save")

    def fill_in_info(self, username, acctid, mobile):
        # 3.填写成员信息
        logger.info("填写成员信息")
        # 3.1输入用户名
        self.do_send_keys(username, self.__INPUT_USERNAME)
        # 3.2输入acctid
        self.do_send_keys(acctid, self.__INPUT_ACCTID)
        # 3.3输入手机号
        self.do_send_keys(mobile, self.__INPUT_MOBILE)
        # 3.4点击保存
        logger.info("点击保存")
        self.do_finds(self.__BTN_SAVE)[0].click()

        from prac_po.page_object.contact_page import ContactPage
        return ContactPage(self.driver)