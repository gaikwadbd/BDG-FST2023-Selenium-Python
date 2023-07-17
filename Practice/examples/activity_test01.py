from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/")

driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")
driver.find_element(By.CLASS_NAME, "login-button").click()

act_title = driver.title
exp_title = "Dashboard / nopCommerce administration"
if act_title == exp_title:
    print("Test Case Pass")
else:
    print("Test Case Fail")
assert act_title in exp_title
driver.close()