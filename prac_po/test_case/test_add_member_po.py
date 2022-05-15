"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import yaml
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from prac.utils.log_utils import logger
from prac_po.page_object.login_page import LoginPage


class TestAddMemberFromHome:

    def setup_class(self):
        fake = Faker("zh_CN")
        self.username = fake.name()
        self.acctid = fake.ssn()
        self.mobile = fake.phone_number()
        # 打开登录页
        self.browser = LoginPage()

    def teardown_class(self):
        self.browser.do_quit()

    def test_add_member_po(self):
        value = self.browser\
            .login()\
            .click_add()\
            .fill_in_info(self.username, self.acctid, self.mobile)\
            .get_tips()

        assert "保存成功" == value

    def test_add_member(self):
        pass

        # # 3.填写成员信息
        # logger.info("填写成员信息")
        # # 3.1输入用户名
        # self.driver.find_element(By.ID, "username").send_keys(self.username)
        # # 3.2输入acctid
        # self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(self.acctid)
        # # 3.3输入手机号
        # self.driver.find_element(By.ID, "memberAdd_phone").send_keys(self.mobile)
        # # 3.4点击保存
        # logger.info("点击保存")
        # self.driver.find_elements(By.CSS_SELECTOR, "a.qui_btn.ww_btn.js_btn_save")[0].click()
        # 4.断言结果
        # loc_tips = (By.ID, "js_tips")
        # WebDriverWait(self.driver, 10, 2).until(expected_conditions.visibility_of_element_located(loc_tips))
        # tips_value = self.driver.find_element(*loc_tips).text

        # assert "保存成功" == tips_value
