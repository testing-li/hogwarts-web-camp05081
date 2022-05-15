"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium.webdriver.common.by import By

from prac_prepare.page_object.base_page import BasePage


class ContactPage(BasePage):
    """通讯录页面"""

    def get_tips(self):
        """获取冒泡文本"""
        loc_tips = (By.ID, "js_tips")
        # WebDriverWait(self.driver, 10, 2).until(expected_conditions.visibility_of_element_located(loc_tips))
        self.wait_element_until_visible(loc_tips)
        tips_value = self.driver.find_element(*loc_tips).text

        return tips_value