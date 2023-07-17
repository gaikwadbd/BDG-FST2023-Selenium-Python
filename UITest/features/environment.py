from behave import fixture
from dotenv import load_dotenv
from frontend.utils.driver_factory import DriverFactory
from frontend.pages.LoginPage import LoginPage
from frontend.pages.MainPage import MainPage
import os

load_dotenv()


@fixture
def main_page(context):
    driver = context.driver
    return MainPage(driver)

@fixture
def login_page(context):
    driver = context.driver
    return LoginPage(driver)


def before_all(context):
    context.driver = DriverFactory.create_driver()
    context.main_page = main_page(context)
    context.login_page = login_page(context)
    context.base_url = os.getenv('BASE_URL')
    context.username = os.getenv('TEST_USERNAME')
    context.password = os.getenv('PASSWORD')


def after_all(context):
    context.driver.quit()