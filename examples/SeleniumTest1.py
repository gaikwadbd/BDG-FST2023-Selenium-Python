# Selenium Test Program FST-May2023
# Author:Bharat Gaikwad
# Created on :01/05/2023
# Modified on 01/05/2023
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# Set up the Firefox Driver with WebDriverManger
service = FirefoxService(GeckoDriverManager().install())
# Start the Driver
with webdriver.Firefox(service = service) as driver:

# Open the browser to the URL
    driver.get("https://training-support.net")

    # Perform testing and assertions

    print(driver.title)
    driver.close
    # Close the browser
    # Feel free to comment out the line below
    # so it doesn't close too quickly
    driver.quit