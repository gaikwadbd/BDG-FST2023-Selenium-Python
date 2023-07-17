import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

searchBox = driver.find_element(By.XPATH, "//input[contains(@placeholder,'Search store')]")
print("Display Status:",searchBox.is_displayed()) #Display Status: True
print("Enabled Status:",searchBox.is_enabled()) #Enabled Status: True

checkBox = driver.find_element(By.ID, "gender-male")
print("Selected Status:",checkBox.is_selected()) #Selected Status: False

checkBox.click()
print("Selected Status:",checkBox.is_selected()) #Selected Status: True

#Browser commands
# driver.close()
# driver.quit()

driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a").click()
ele = driver.find_element(By.XPATH, "/html/body/div[6]/div[4]/div[2]/div[2]/a").click()

time.sleep(10)
ele1 = driver.find_element(By.XPATH,"//h3[normalize-space()='12 years of experience']")
print("NEW",ele1.is_displayed())

time.sleep(10)

driver.close()