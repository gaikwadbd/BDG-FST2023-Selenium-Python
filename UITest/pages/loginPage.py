from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.userTxtBox = "username"
        self.passTxtBox = "password"
        self.loginBtn = "input[name='op']"

    def get_user_textbox(self):
        return self.driver.find_element(By.ID, self.userTxtBox)

    def get_pass_textbox(self):
        return self.driver.find_element(By.ID, self.passTxtBox)

    def get_login_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.loginBtn )

    def set_username(self, username):
        self.get_user_textbox().send_keys(username)

    def set_password(self, password):
        self.get_pass_textbox().send_keys(password)

    def click_login_button(self):
        self.get_login_button().click()