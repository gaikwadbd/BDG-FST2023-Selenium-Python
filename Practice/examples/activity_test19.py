# Handle Links
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

ele  = driver.find_elements(By.TAG_NAME,'a')

print(len(ele))

for link in ele:
    print(link.text)