from selenium import webdriver


class DriverFactory:
    @staticmethod
    def create_driver(browser="chrome"):
        if browser == "chrome":
            driver = webdriver.Chrome(r'C:\Users\Bharat\Documents\SeleniumWebdrivers\chromedriver.exe')
            driver.maximize_window()
            driver.implicitly_wait(10)
            return driver
        else:
            raise ValueError(f"Unsupported browser: {browser}")