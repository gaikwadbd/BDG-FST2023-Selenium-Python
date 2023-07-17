from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='dob']").click()

month = driver.find_element(By.XPATH, "(//select[@aria-label='Select month'])[1]")
all_months = Select(month)
all_months.select_by_visible_text("Nov")

year = driver.find_element(By.XPATH, "(//select[@aria-label='Select year'])[1]")
all_years = Select(year)
all_years .select_by_visible_text("2021")

all_dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in all_dates:
    if ele.text == "21":
        ele.click()
        break;