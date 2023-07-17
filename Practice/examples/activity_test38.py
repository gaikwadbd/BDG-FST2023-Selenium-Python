import xlsUtils
from  selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time
driver = webdriver.Chrome()
#driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_SDET\\Drivers\\chromedriver.exe")
driver.get("https://sandbox.chazki.com/#/login")
driver.maximize_window()
path = "C:\\Users\\01979D744\\Documents\\FST2023\\BHARAT-FST2023LMS-Selenium-Python\\Practice\\examples\\Login.xlsx"

rows = xlsUtils.getRowCount(path,'sheet1')

for r in range (2, rows+1):
    username=xlsUtils.readData(path, "sheet1",r,1)
    password=xlsUtils.readData(path,"sheet1",r,2)

    driver.find_element_by_xpath("/html/body/app-root/app-login/div/div[1]/div/form/div/div[1]/span/input").clear()
    driver.find_element_by_xpath("/html/body/app-root/app-login/div/div[1]/div/form/div/div[1]/span/input").send_keys(username)
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/app-root/app-login/div/div[1]/div/form/div/div[2]/span/input").send_keys(password)
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/app-root/app-login/div/div[1]/div/form/div/div[3]/button").click()
    time.sleep(5)
    driver.find_element_by_xpath("//a[@id='menu-button']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//i[@class='material-icons'][contains(text(),'keyboard_arrow_down')]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//span[contains(text(),'Salir')]").click()
    if driver.title=="Ataribox":
        print("test is passed")
        xlsUtils.writeData(path, "sheet1", r,3, "test passed")
    else:
        print("test failed")
        xlsUtils.writeData(path, "sheet1", r, 3, "test failed")