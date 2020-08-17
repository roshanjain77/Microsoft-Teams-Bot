from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

url = 'https://meet.google.com/the-meet-cde' #meet code

fp =  webdriver.FirefoxProfile('/path/to/your/firefox/profile')

driver = webdriver.Firefox(fp)

driver.get(url)

login_button = WebDriverWait(driver,40).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/span/span')))

time.sleep(10)


for i in range(0,7):
	if i == 5:
		pyautogui.hotkey('enter')#Mute Mic
	if i == 4:
		pyautogui.hotkey('enter')#Mute Camera
	pyautogui.press('tab')

pyautogui.press('enter')

print("Asked permission")

time.sleep(30)

driver.quit()