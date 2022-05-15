"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium.webdriver.common.by import By

from prac_po.page_object.base_page import BasePage
from prac_po.utils.log_utils import logger


class HomePage(BasePage):

    __BTN_ADD = (By.LINK_TEXT, "添加成员")

    def click_add(self):
        """2.点击添加成员按钮"""
        logger.info("点击添加成员按钮")
        self.do_find(self.__BTN_ADD).click()

        from prac_po.page_object.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)