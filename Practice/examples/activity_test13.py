# Find Elements By Parents , Ancetors and Child

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://money.rediff.com/gainers/bse/daily/groupa/")

driver.maximize_window()


#self
# msg = driver.find_element(By.XPATH,"//a[contains(text(),'Brigade Enterprises')]/self::a").text
# print(msg)   #Brigade Enterprises

#parent
# msg = driver.find_element(By.XPATH,"//a[contains(text(),'Brigade Enterprises')]/parent::td").text
# print(msg)   #Brigade Enterprises

#child
# childs = driver.find_elements(By.XPATH, "//a[contains(text(),'Brigade Enterprises')]/ancestor::tr/child::td")
# print(len(childs))  #5

#ancestor
# ele = driver.find_element(By.XPATH, "//a[contains(text(),'Brigade Enterprises')]/ancestor::tr").text
# print(ele)  # only one element Brigade Enterprises A 453.85 472.60 + 4.13
#print(len(ele))  #1

#descendant
# ele = driver.find_elements(By.XPATH, "//a[contains(text(),'Brigade Enterprises')]/ancestor::tr/descendant::*")
# print("no of descendant",len(ele))  #7 inclues child,grandchild and so on of the current tag only

#following
# ele = driver.find_elements(By.XPATH, "//a[contains(text(),'Brigade Enterprises')]/ancestor::tr/following::*")
# print("no of following",len(ele))  #315 find all siblings,childs,grandchilds that comes after current tag

#following-sibling
# ele = driver.find_elements(By.XPATH, "//a[contains(text(),'Brigade Enterprises')]/ancestor::tr/following-sibling::*")
# print("no of following-sibling",len(ele))  #19 find all siblings only that comes after current tag

#preceding
ele = driver.find_elements(By.XPATH, "//a[contains(text(),'Brigade Enterprises')]/ancestor::tr/preceding::*")
print("no of preceding",len(ele))  # 216 find all siblings,parents,grandparents that comes before current tag

#preceding-sibling
ele = driver.find_elements(By.XPATH, "//a[contains(text(),'Brigade Enterprises')]/ancestor::tr/preceding-sibling::*")
print("no of preceding-sibling",len(ele))  #5  find all siblings only that comes before current tag

# ancestor-or-self
# descendant-or-self