"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium.webdriver.common.by import By
from prac_prepare.page_object.base_page import BasePage
from prac_prepare.utils.log_utils import logger


class HomePage(BasePage):
    """首页"""

    def click_add_member(self):
        """点击添加成员"""
        logger.info("点击添加成员按钮")
        self.do_find(By.LINK_TEXT, "添加成员").click()

        from prac_prepare.page_object.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)