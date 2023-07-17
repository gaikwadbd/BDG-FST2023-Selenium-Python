
# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Start the driver
with webdriver.Firefox() as driver:

    # Define a wait variable
    wait = WebDriverWait(driver, 10)

    # Navigate to url
    driver.get("https://www.training-support.net/selenium/tab-opener")

    # Store the current window/tab handle
    original_window = driver.current_window_handle

    # Click the button that opens a new window/tab
    driver.find_element(By.ID, "launcher").click()

    # Wait for the other window/tab to open
    wait.until(expected_conditions.number_of_windows_to_be(2))

    # Switch to the new tab that opened
    driver.switch_to.window(driver.window_handles[1])

    # Wait for the new tab to finish loading content
    wait.until(expected_conditions.title_is("Newtab"))
