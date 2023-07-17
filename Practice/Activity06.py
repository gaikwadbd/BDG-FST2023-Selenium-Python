from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


def activity06Function():
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
    driver.implicitly_wait(10)

    ermolow_ed = driver.find_element('xpath', "//*[text()='Ермолов Эд']")
    ermolow_ed.click()

    name_test_case = driver.find_element('xpath',
                                         "//*[@class = 'LoadableTreeGroupView__children']//*[@class = 'TreeNodeName']")
    name_test_case.click()

    def check_name_and_id_testcase():
        try:
            driver.find_element('xpath', "//*[text()='88531']") and driver.find_element('xpath',
                                                                                        "//*[text()='02 Столбцы с модулем']")
        except NoSuchElementException:
            return False
        return True

    check_name_and_id_testcase()

    test_case_02 = driver.find_element('xpath', "//*[text()='02 Столбцы с модулем']")
    test_case_02.click()

    def check_blocks_in_testcase():
        try:
            driver.find_element('xpath', "//*[text()='Description']") and driver.find_element('xpath',
                                                                                              "//*[text()='Precondition']") and driver.find_element(
                'xpath', "//*[text()='Scenario']") and driver.find_element('xpath',
                                                                           "//*[text()='Expected result']") and driver.find_element(
                'xpath', "//*[text()='Comments']")
        except NoSuchElementException:
            return False
        return True

    check_blocks_in_testcase()

    def check_images_in_scenario():
        try:
            driver.find_element('xpath', "//*[text()='image/png']")
        except NoSuchElementException:
            return False
        return True

    check_images_in_scenario()

    attachment = driver.find_element('xpath', "//*[text()='Attachments']")
    attachment.click()

    def check_images_in_attachment():
        try:
            driver.find_element('xpath', "//*[text()='________.png']")
        except NoSuchElementException:
            return False
        return True

    check_images_in_attachment()

    overview = driver.find_element('xpath', "//*[text()='Overview']")
    overview.click()

    def ckeck_tag_regress():
        try:
            driver.find_element('xpath', "//*[text()='regress']")
        except NoSuchElementException:
            return False
        return True

    ckeck_tag_regress()

    def ckeck_tag_no_regress():
        try:
            driver.find_element('xpath', "//*[text()='maria_tag']") and driver.find_element('xpath',
                                                                                            "//*[text()='smoke']")
        except NoSuchElementException:
            return True
        return False

    ckeck_tag_no_regress()

    def field_feature_and_field_story():
        try:
            driver.find_element('xpath',
                                "//*[@class = 'CustomFieldValueGroupedList__value']//*[text()='Экран `Рассчитанные цены`']") and (
                'xpath', "//*[@class = 'CustomFieldValueGroupedList__value']//*[text()='Ермолов Эд']")
        except NoSuchElementException:
            driver.get('https://allure.x5.ru/project/123/dashboards')
        return True

    field_feature_and_field_story()

    input('Press ENTER to exit')


activity06Function()
