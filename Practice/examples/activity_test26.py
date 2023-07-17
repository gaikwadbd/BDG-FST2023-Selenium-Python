# Read Values from tables
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

# 1) Count no of rows

rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))
print("Rows", rows)

# 2) Count no of columns

columns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[1]/th"))
print("Columns", columns)

#3) Read specific row and column data

data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(data)

#4) Read all the rows and columns data

for i in range(2,rows+1):
    for j in range(1,columns+1):
        ele = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
        print(ele, end="   ")
    print()

#5) Read data based on conditions (List book name whose author is mukesh

for i in range(2,rows+1):
    ele = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(i)+"]/td[2]").text

    if ele == "Mukesh":
        ele1 = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(i) + "]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(i) + "]/td[4]").text
        print(ele,"   ",ele1,"   ",price)

driver.close()