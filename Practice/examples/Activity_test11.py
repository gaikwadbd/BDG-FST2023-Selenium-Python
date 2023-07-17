

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")

driver.maximize_window()

# driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver.find_element(By.CLASS_NAME, "search-box-button").click

# driver.find_element(By.LINK_TEXT, "Register").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()

# sliders = driver.find_elements(By.CLASS_NAME, "nivo-imageLink")
# print(len(sliders)) #2
#
# ele1 = driver.find_elements(By.TAG_NAME, "a")
# print(len(ele1))  #90



time.sleep(10)
driver.close()