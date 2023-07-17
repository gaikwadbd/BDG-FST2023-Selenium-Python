import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

driver = None


@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("--------------------setup---------------")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")

    yield
    print("--------------------tear down---------------")
    driver.quit()


@allure.feature('Feature2')
@allure.story('Story2', 'Story3')
@allure.story('Story4')
@allure.description("validation of title")
@allure.severity(severity_level="CRITICAL")
@pytest.mark.usefixtures("init_driver")
def test_google_title():
    try:
        assert driver.title == "Googlex"
    finally:
        if AssertionError:
            allure.attach(driver.get_screenshot_as_png(), name="Invalid URL",
                          attachment_type=allure.attachment_type.PNG)


@allure.feature('Feature3')
@allure.story('Story4', 'Story5')
@allure.story('Story6')
@allure.description("validation of Current URL")
@allure.severity(severity_level="NORMAL")
@pytest.mark.usefixtures("init_driver")
def test_google_url():
    assert driver.current_url == "https://www.google.com/?gws_rd=ssl"