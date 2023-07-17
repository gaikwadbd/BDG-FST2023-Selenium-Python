# Handles Tabs and Multiple Windows
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


#Selenium 4 new fetaures
driver.get("https://admin-demo.nopcommerce.com/")
driver.switch_to.new_window('tab')  #Open new tab
driver.get("https://facebook.com")


driver.get("https://admin-demo.nopcommerce.com/")
driver.switch_to.new_window('window')  #Open new window
driver.get("https://facebook.com")