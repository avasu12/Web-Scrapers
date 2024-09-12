from selenium import webdriver
from selenium.webdriver.common.by import By

# Start a driver session
driver = webdriver.Chrome()
print(driver)
print(type(driver))

# Navigate to webpage
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Get information about the browser
title = driver.title
print(title)

# A waiting strategy
driver.implicitly_wait(0.5)

# Find an element
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# Do something to the elements
text_box.send_keys("Selenium")
submit_button.click()

# Request element information
message = driver.find_element(by=By.ID, value="message")
print(message)

# End session
driver.quit()
