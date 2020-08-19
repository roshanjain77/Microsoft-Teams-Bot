#!/home/ubuntu/anaconda3/bin/python
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

username = "roshan"
options = Options()
options.headless = True
# options.add_argument(f"--user-data-dir=selenium_profiles/{username}")

options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2,     # 1:allow, 2:block 
    "profile.default_content_setting_values.media_stream_camera": 2,  # 1:allow, 2:block 
    "profile.default_content_setting_values.geolocation": 2,          # 1:allow, 2:block 
    "profile.default_content_setting_values.notifications": 2         # 1:allow, 2:block 
})
driver = webdriver.Chrome(options=options)
email = input()
password = input()
driver.get('https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346')
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="i0116"]'))).send_keys(email)
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="idSIButton9"]'))).click()
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="i0118"]'))).send_keys(password)
time.sleep(2)
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))).click()
time.sleep(2)
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))).click()
print("logged in")
while True:
  try:
    print("Calendar")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app-bar-ef56c0de-36fc-4ef8-b417-3d82ba9d073c"]'))).click()
    print("Finding joining")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@title="Join"]'))).click()
    print('joinned')
    # WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//button[@ng-click="getUserMedia.passWithoutMedia()"]'))).click()
    # driver.find_element_by_xpath('//span[text()="Audio off"]').click()
    time.sleep(10)
    driver.find_element_by_xpath('//button[text()="Join now"]').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="hangup-button"]')))
    print('joined meeting')
  except:
    print("Entering 60")
    time.sleep(60)
    print("Exiting 60")
