# Handle Multiple Windows and Tabs
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://opensource-demo.orangehrmlive.com/ ")
driver.maximize_window()
print("Current",driver.current_window_handle)

time.sleep(7)
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
print("All", driver.window_handles)

windowId = driver.window_handles

# for winId in windowId:
#     driver.switch_to.window(winId)
#     print(driver.title)


#To close specific browser windows by using title
for winId in windowId:
    driver.switch_to.window(winId)
    if driver.title == "OrangeHRM" or driver.title=="Facebook.com":
        driver.close