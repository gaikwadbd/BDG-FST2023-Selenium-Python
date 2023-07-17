# Handle Checkbox and Radio Buttons
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# #1) Select Specific checkbox
# driver.find_element(By.XPATH, "//input[@id='monday']").click()

#2) Select all the checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))


# for i in range(len(checkboxes)):
#     checkboxes[i].click()

# for checkbox in checkboxes:
#     checkbox.click()


#3) Select Multiple checkboxes by choice

# for checkbox in checkboxes:
#    weekName = checkbox.get_attribute('id')
#
#    if weekName=='monday' or weekName=='tuesday':
#        checkbox.click()

#4) Select last 2 checkboxes
#
# for i in range(len(checkboxes)-2, len(checkboxes)):
#     checkboxes[i].click()

#5) Select first 2 checkboxes

# for i in range(len(checkboxes)):
#     if i < 2:
#         checkboxes[i].click()


#6) Clearing all the checkboxes

# for checkbox in checkboxes:
#     if checkbox.is_selected():
#         checkbox.click()