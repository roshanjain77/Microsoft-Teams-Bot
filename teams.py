# !/home/ubuntu/anaconda3/bin/python
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


def join(driver):
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="roster-button"]'))).click()
  while True:
    time.sleep(10)
    print('Watching Participants')
    try:
      try:
        others = int(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-content-wrapper"]/div[1]/div/calling-screen/div/div[2]/meeting-panel-components/calling-roster/div/div[2]/div/div[1]/accordion/div/accordion-section[4]/div/calling-roster-section/div/div[1]/button/span[3]'))).text[1:-1])
      except:
        others = 0
      current = int(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-content-wrapper"]/div[1]/div/calling-screen/div/div[2]/meeting-panel-components/calling-roster/div/div[2]/div/div[1]/accordion/div/accordion-section[2]/div/calling-roster-section/div/div[1]/button/span[3]'))).text[1:-1])
      percent = (current/(others + current))*100
      print(percent)
      if(percent < 20 or current == 1):
        break
    except:
      break
    time.sleep(110)
  try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="hangup-button"]'))).click()
  except:
    pass
  

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
driver.get('https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346')
email = input()
password = input()
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="i0116"]'))).send_keys(email)
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="idSIButton9"]'))).click()
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="i0118"]'))).send_keys(password)
time.sleep(2)
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))).click()
time.sleep(2)
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))).click()
print("logged in")
refresh_time = time.clock_gettime(0)
while True:
  try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app-bar-ef56c0de-36fc-4ef8-b417-3d82ba9d073c"]'))).click()
    print("Calendar")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@title="Join"]'))).click()
    print('Found a event')
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//button[@ng-click="getUserMedia.passWithoutMedia()"]'))).click()
    driver.find_element_by_xpath('//span[text()="Audio off"]').click()
    # time.sleep(10)
    # driver.find_element_by_xpath('//button[text()="Join now"]').click()
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="hangup-button"]')))
    print('joined meeting')
    join(driver)
  except:
    print("Entering 60")
    time.sleep(60)
    print("Exiting 60")
  if time.clock_gettime(0) - refresh_time > 60*5:
    driver.refresh()
    refresh_time = time.clock_gettime(0)
