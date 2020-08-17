from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyautogui as gui
import time


def until(x):
  while True:
    try:
      driver.find_element_by_xpath(x)
      return driver.find_element_by_xpath(x)
    except:
      time.sleep(1)

driver = webdriver.Firefox()
driver.get('https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346')
driver.find_element_by_xpath('//*[@id="i0116"]').send_keys('***')
driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
driver.find_element_by_xpath('//*[@id="i0118"]').send_keys('***')
time.sleep(2)
gui.press('enter')
time.sleep(2)
until('//*[@id="idBtn_Back"]').click()
until('/html/body/div[2]/div[2]/div[1]/app-bar/nav/ul/li[5]/button/ng-include/svg').click()
