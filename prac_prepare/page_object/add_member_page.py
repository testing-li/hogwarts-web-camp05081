"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium.webdriver.common.by import By

from prac_prepare.page_object.base_page import BasePage
from prac_prepare.utils.log_utils import logger


class AddMemberPage(BasePage):
    """添加成员页面"""

    def fill_in_info(self, username, acctid, mobile):
        """填写成员信息"""
        logger.info("填写成员信息")
        # 3.1输入用户名
        self.do_find(By.ID, "username").send_keys(username)
        # 3.2输入acctid
        self.do_find(By.ID, "memberAdd_acctid").send_keys(acctid)
        # 3.3输入手机号
        self.do_find(By.ID, "memberAdd_phone").send_keys(mobile)
        # 3.4点击保存
        logger.info("点击保存")
        self.do_finds(By.CSS_SELECTOR, "a.qui_btn.ww_btn.js_btn_save")[0].click()

        from prac_prepare.page_object.contact_page import ContactPage
        return ContactPage(self.driver)