from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.homeUserBtn = "[href='/users/auth/dexcom_sts']"

    def get_home_user_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.homeUserBtn)

    def click_home_user_button(self):
        self.get_home_user_button().click()