from  selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html_tables.asp")
rows = len(driver.find_element(By.XPATH,"//*[@id='customers']/tbody/tr"))
cols = len(driver.find_element(By.XPATH,"//*[@id='customers']/tbody/tr[1]/th"))
print(rows)
print(cols)
for r in range(2,rows+1):
    for c in range(1, cols+1):
        datos=driver.find_element(By.XPATH,"//*[@id='customers']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(datos, end='                ')
    print()
    time.sleep(5)
driver.get_screenshot_as_file("..\\examples\\Screen\\home.png")
driver.close()