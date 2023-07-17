import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://money.rediff.com/gainers/bse/daily/groupa/")

driver.maximize_window()
print(driver.title) #Daily Gainers: BSE, NSE, Stock quotes, share market, stock market, stock tips: Rediff Stocks
print(driver.current_url) #https://money.rediff.com/gainers/bse/daily/groupa/