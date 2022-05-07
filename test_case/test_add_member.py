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
from utils.log_utils import logger


class TestAddMember:

    def setup_class(self):
        """前置处理"""

        # 实例化驱动
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        # 造数据
        fake = Faker('zh_CN')
        self.username = fake.name()
        self.acctid = fake.ssn()
        self.mobile = fake.phone_number()

        """登录"""
        # 1、访问企业微信首页 CookieDomain
        logger.info("1、访问企业微信首页 CookieDomain")
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 2、获取本地 cookies
        logger.info("2、获取本地 cookies")
        with open("../data/cookies.yaml", "r") as f:
            cookies = yaml.safe_load(f)
        # 3、植入cookies
        logger.info("3、植入cookies")
        for ck in cookies:
            self.driver.add_cookie(ck)
        # 4、访问首页
        logger.info("4、访问首页")
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def teardown_class(self):
        """后置处理"""
        self.driver.quit()

    def test_add_member(self):
        """添加成员的测试用例"""

        """点击添加成员按钮"""
        self.driver.find_element(By.LINK_TEXT, '添加成员').click()

        """填写成员信息"""
        self.driver.find_element(By.NAME, 'username').send_keys(self.username)
        self.driver.find_element(By.NAME, 'acctid').send_keys(self.acctid)
        self.driver.find_element(By.NAME, 'mobile').send_keys(self.mobile)
        self.driver.find_element(By.CSS_SELECTOR, 'a.qui_btn.ww_btn.js_btn_save').click()

        """断言结果"""
        tips_loc = (By.ID, "js_tips")
        WebDriverWait(self.driver, 10, 2).until(expected_conditions.visibility_of_element_located(tips_loc))
        tips = self.driver.find_element(*tips_loc).text
        logger.info(f"{tips}")

        assert "保存成功" == tips