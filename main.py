from selenium import webdriver
from selenium.webdriver.common.by import By
import webbrowser
import time

#todo:
#Add option to pause loop
#alert when bait empty



gameCode = ""
gameUrl = "https://www.gimkit.com/join?gc="
gameCode = input('Enter game code here: ')
gameUrl = gameUrl + str(gameCode)

driver = webdriver.Chrome()

driver.get(gameUrl)

buttonFish = driver.find_elements(By.ID, "insert Button ID here")

while True:
    buttonFish.click()