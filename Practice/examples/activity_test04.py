# Mouse Actions


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")

driver.maximize_window()

min_slider = driver.find_element(By.XPATH, "//span[1]")
max_slider = driver.find_element(By.XPATH, "//span[2]")

print("Location of sliders before moving")
print(min_slider.location)
print(max_slider.location)

action = ActionChains(driver)

action.drag_and_drop_by_offset(min_slider,100,0).perform()  #Slider is horizontal so y axes value passed as 0
action.drag_and_drop_by_offset(max_slider,-39,0).perform()

print("Location of sliders after moving")
print(min_slider.location)
print(max_slider.location)
driver.quit()