# Keyboard Actions

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://text-compare.com/")

driver.maximize_window()

# Ctrl+A
# ctrl + C
# Tab
# ctrl + V

input1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
input2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

input1.send_keys("Welcome to Selenium")
action = ActionChains(driver)
action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
action.key_down(Keys.TAB).perform()
action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
driver.quit()
