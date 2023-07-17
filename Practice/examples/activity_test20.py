# Handle Alerts and Popups
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()