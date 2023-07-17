# Handle Multiple Windows
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//*[@id='Wikipedia1_wikipedia-search-input']").send_keys("Selenium")
driver.find_element(By.XPATH, "(//input[@type='submit'])[1]").click()

searchedElements = driver.find_elements(By.XPATH, "//div[@id='Wikipedia1_wikipedia-search-results']/child::div/a")

print(searchedElements)

for ele in searchedElements:
    ele.click()

all_handles = driver.window_handles

for handles in all_handles:
    driver.switch_to.window(handles)
    print(driver.title)

driver.quit()