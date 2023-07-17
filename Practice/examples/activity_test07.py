# Read Cookies and Delete Cookies

from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://admin-demo.nopcommerce.com/")


#Print details of all cokkies
cookies = driver.get_cookies()
print("Cookies",len(cookies))  #3
#
# for c in cookies:
#     print(c.get("name"),":",c.get("value"))



#Add a new cookie
driver.add_cookie({"name":"myCookie", "value":"123456"})
cookies = driver.get_cookies()
print("length of Cookies after adding new cookie",len(cookies)) #4


#Delete a specific cookie from a browser
driver.delete_cookie("myCookie")
cookies = driver.get_cookies()
print("length of Cookies after deleting new cookie",len(cookies)) #3

#Delete all the cookie
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("length of Cookies after deleting all the cookies",len(cookies)) #0

driver.close()