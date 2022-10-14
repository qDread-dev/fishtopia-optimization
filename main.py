from selenium import webdriver

#always attempt to fish

driver = webdriver.Chrome()
currentUrl = driver.current_url
fishButton = driver.find_element("id", "button id")

while True:
    fishButton.click()