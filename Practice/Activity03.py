from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def activity03Function():
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    driver = webdriver.Chrome(chrome_options=options)

    driver.get('https://allure.x5.ru/project/123/test-cases?treeId=419')
    driver.implicitly_wait(10)
    login_field = driver.find_element('name', 'username')
    login_field.click()
    login_field.send_keys('Ariadna.Kraynova')
    password_field = driver.find_element('name', 'password')
    password_field.click()
    password_field.send_keys('Qwerty12345!')
    button = driver.find_element('xpath', '//button')
    button.click()

    case_display_switch = driver.find_element('xpath',
                                              "//div[@class = 'LoadableTreeViewToggle__arrow']//*[@class = 'Icon Icon_size_small angle angle-down Arrow Arrow_expanded_bottom ']")
    case_display_switch.click()
    type_test_cases = driver.find_element('xpath', "//div[@class = 'tippy-content']//div[last()-1]")
    type_test_cases.click()

    sort_by_id = driver.find_element('xpath', "//div[text()='Id']")
    sort_by_id.click()

    def check_exists_sort_by_id():
        try:
            driver.find_element('xpath',
                                "//div[@class = 'LoadableTreeControlPanel__main']//div[last()-3]//*[@class = 'Icon Icon_size_tiny SorterIcon SorterIcon_enabled SorterIcon_rotate']")
        except NoSuchElementException:
            return False
        return True

    check_exists_sort_by_id()

    input('Press ENTER to exit')


activity03Function()
