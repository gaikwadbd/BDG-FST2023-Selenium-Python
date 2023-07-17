# Read Dynamic Web Table values
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/ ")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "(//input[@placeholder='Password'])[1]").send_keys("admin123")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

