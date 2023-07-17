# Select Item in Dropdownlist
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

dropdownObj = Select(driver.find_element(By.XPATH, "//select[@id='input-country']"))

dropdownObj.select_by_visible_text("India")

all_options = dropdownObj.options
#
# print(len(all_options))
#
for option in all_options:
    print(option.text)


#Select option from dropdown without using built in method

for options in all_options:
    if options.text == "India":
        options.click()
        break