from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


def activity04Function():
    chrome_options = Options()
    chrome_options.add_argument('ignore-certificate-errors')
    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://allure.x5.ru/project/123/test-cases?treeId=419')
    driver.implicitly_wait(10)
    login_field = driver.find_element('name', 'username')
    login_field.click()
    login_field.send_keys('Ariadna.Kraynova')
    password_field = driver.find_element('name', 'password')

    password_field.click()
    password_field.send_keys('Asdasd12345!')
    button = driver.find_element('xpath', '//button')
    button.click()

    case_filter = driver.find_element('xpath', "//*[@class = 'TestCaseTreeContainer__controls']//button")
    ActionChains(driver).move_to_element(case_filter).perform()

    def check_exists_icon_filter():
        try:
            driver.find_element('xpath', "//div[@class = 'tippy-popper']")
        except NoSuchElementException:
            return False
        return True

    check_exists_icon_filter()

    case_filter.click()

    new_filter = driver.find_element('xpath',
                                     "//div[@class = 'SavedFilters__title']//button[@class = 'Button Button_size_small Button_style_default Button_shape_round ']")
    new_filter.click()

    status_review = driver.find_element('xpath', "//span[text() = 'Review']")
    status_review.click()

    def check_review():
        try:
            driver.find_element('xpath',
                                "//ul[@class = 'list']//li[last()-2]//label[@class = 'Checkbox FilterChoice__checkbox']//*[@class = 'Icon Icon_size_tiny Checkbox__icon Checkbox__icon_highlighted']") and driver.find_element(
                'xpath',
                "//ul[@class = 'list']//li[last()-21]//label[@class = 'Checkbox FilterChoice__checkbox']//*[@class = 'Icon Icon_size_tiny Checkbox__icon']") and driver.find_element(
                'xpath',
                "//ul[@class = 'list']//li[last()-15]//label[@class = 'Checkbox FilterChoice__checkbox']//*[@class = 'Icon Icon_size_tiny Checkbox__icon']") and driver.find_element(
                'xpath',
                "//ul[@class = 'list']//li[last()-7]//label[@class = 'Checkbox FilterChoice__checkbox']//*[@class = 'Icon Icon_size_tiny Checkbox__icon']")
        except NoSuchElementException:
            return False
        return True

    check_review()

    input('Press ENTER to exit')


activity04Function()
