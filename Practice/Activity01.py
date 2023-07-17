from selenium import webdriver


def activity01Function():
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    driver = webdriver.Chrome(chrome_options=options)

    driver.get('https://allure.x5.ru/project/123/dashboards')
    driver.implicitly_wait(10)
    login_field = driver.find_element('name', 'username')
    login_field.click()
    login_field.send_keys('Ariadna.Kraynova')
    password_field = driver.find_element('name', 'password')
    password_field.click()
    password_field.send_keys('Qwerty12345!')
    button = driver.find_element('xpath', '//button')
    button.click()

    testcases_icon = driver.find_element('name', 'test-cases-icon')
    testcases_icon.click()

    url = driver.current_url
    assert '/test-cases' in url

    driver.execute_script("window.history.go(-1)")

    input('Press ENTER to exit')


activity01Function()
