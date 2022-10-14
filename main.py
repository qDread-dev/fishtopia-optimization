from selenium import webdriver
from selenium.webdriver.common.by import By
import webbrowser
import time


gameCode = ""
gameUrl = "https://www.gimkit.com/join?gc="
gameCode = input('Enter game code here: ')
gameUrl = gameUrl + str(gameCode)

driver = webdriver.Chrome()

driver.get(gameUrl)

buttonFish = driver.find_elements(By.ID, "insert Button ID here")

buttonFish.click()