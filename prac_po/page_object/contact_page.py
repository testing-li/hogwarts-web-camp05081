"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium.webdriver.common.by import By

from prac_po.page_object.base_page import BasePage


class ContactPage(BasePage):
    __TEXT_TIPS = (By.ID, "js_tips")

    def get_tips(self):

        # WebDriverWait(self.driver, 10, 2).until(expected_conditions.visibility_of_element_located(loc_tips))
        self.wait_visible(self.__TEXT_TIPS)
        tips_value = self.do_find(self.__TEXT_TIPS).text
        return tips_value