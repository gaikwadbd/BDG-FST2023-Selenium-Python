# Find Elements by XPATH

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")

time.sleep(3)

driver.find_element(By.XPATH, "//*[text()='Login']").click()

driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")

driver.find_element(By.XPATH, "//input[@name='password' and @placeholder='Password']").send_keys("admin123")

driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

time.sleep(3)

driver.find_element(By.XPATH, "//ul[contains(@class,'oxd-main-menu')]/child::li[2]").click()

time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Add']")

time.sleep(5)
driver.find_element(By.XPATH, "//button[contains(@class,'orangehrm-left-space') or normalize-space()='Save']")


#and , or , starts-with(), contains(), text(), normalize-space()