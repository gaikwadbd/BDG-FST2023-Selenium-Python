# Dropdown Test

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/ ")

driver.maximize_window()

driver.find_element(By.XPATH, "//*[@id='select2-billing_country-container']").click()
optionsList = driver.find_elements(By.XPATH, "//span[@class='select2-results']/ul/li")

print(len(optionsList))

for ele in optionsList:
    if ele.text == "India":
        ele.click()
        break;


