import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
import time

sys.path.append("C:\\Users\\Luis\\Desktop\\Python_Selenium_SDET")
import activity_test45


class LoginTest(unittest.TestCase):
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp = activity_test45(self.driver)
        lp.setUserName(self.username)
        lp.setPasswrod(self.password)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "webpage title is not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\Luis\\Desktop\\Python_Selenium_SDET\\Reports"))
