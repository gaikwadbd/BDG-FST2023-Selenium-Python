# Find Broken Links in Applications

#install requests package

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

all_links  = driver.find_elements(By.TAG_NAME,'a')

print(len(all_links))

count = 0

for link in all_links:
    url = link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None

    if (res.status_code>=400):
        print(url, "  is broken link")
    else:
        print(url, "  is valid link")

print("Total no of broken links are ", count)