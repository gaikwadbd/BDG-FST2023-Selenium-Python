# Finding Elements by CSSelector

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://facebook.com")

# #tag & id    -- tagname#valueOfId
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("ABC")
driver.find_element(By.CSS_SELECTOR,"#email").send_keys("ABC")    # Tag Name is optional

# #tag & class  -- tagname.valueOfClass
driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc@gmail.com")

#tag & attribute --  tagname[attribute=value]
driver.find_element(By.CSS_SELECTOR,"input[placeholder=Email address or phone number]").send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR,"[placeholder=Email address or phone number]").send_keys("abc@gmail.com")


#tag, class & attribute --  tagname.valueOfClass[attribute=value]
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_email]").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR,".inputtext[data-testid=royal_email]").send_keys("abc@gmail.com")

# driver.find_element(By.CSS_SELECTOR,".inputtext[data-testid=royal_pass]").send_keys("pass@123")


time.sleep(10)