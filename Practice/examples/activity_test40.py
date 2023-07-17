from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.drivers.chrome import ChromeDriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Register.html")
driver.implicitly_wait(10)
assert "Register" in driver.title
print(driver.title)
name = driver.find_element(By.XPATH,"//input[@placeholder='First Name']")
lastname = driver.find_element(By.XPATH,"//input[@placeholder='Last Name']")
driver.get_screenshot_as_file("..\\examples\\Screen\\home.png")
name.send_keys("luis")
lastname.send_keys("chavez")
