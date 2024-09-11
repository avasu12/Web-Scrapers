from selenium import webdriver

driver = webdriver.Chrome()
print(driver)

driver.get("http://selenium.dev")

driver.quit()
