# Handles Frames
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()

mainFrame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(mainFrame)

childFrame = driver.find_element(By.XPATH, "iframe[src='SingleFrame.html']")
driver.switch_to.frame(childFrame)

driver.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys("Hello")

driver.switch_to.parent_frame()  # Switch to parent frame (Outer i frame)