from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time,os,sys

def calc_time_elapsed(sec):
  sec = int(sec)
  h,m,s = 0,0,0
  ret = ''
  s = sec % 60
  mn = sec // 60
  m = mn % 60
  h = mn // 60
  if h:
    ret += f'{h}h '
  if m:
    ret += f'{m}m '
  if s:
    ret += f'{s}s'
  return ret

def join():
  WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="roster-button"]'))).click()
  mx = 0
  start = os.popen('date --date="+5 hour 30 minutes" +"%a %d %b %Y %I:%M %p"').read().strip('\n')
  start_check = time.clock_gettime(0)
  meeting_name = driver.title[:-28]
  if not meeting_name:
      meeting_name = '(no title)'
  while True:
    time.sleep(10)
    try:
      current = int(WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-content-wrapper"]/div[1]/div/calling-screen/div/div[2]/meeting-panel-components/calling-roster/div/div[2]/div/div[1]/accordion/div/accordion-section[2]/div/calling-roster-section/div/div[1]/button/span[3]'))).text[1:-1])
      if(current < int(sys.argv[4])):
        break
    except:
      break
    time.sleep(50)
  end = os.popen('date --date="+5 hour 30 minutes" +"%a %d %b %Y %I:%M %p"').read().strip('\n')
  end_check = time.clock_gettime(0)
  lasted_for = end_check - start_check
  if lasted_for > 120:
    lasted_for = calc_time_elapsed(lasted_for)
    s = f'{start},{end},{meeting_name},{lasted_for}\n'
    with open(f'/home/ubuntu/Microsoft-Teams-Bot/{username}.log','a') as f:
      f.write(s)
  driver.refresh()
  time.sleep(15)
  driver.refresh()
  time.sleep(15)

username = sys.argv[1]
options = Options()
options.binary_location='/usr/bin/google-chrome-stable'
options.headless = True
options.add_argument('--start-maximized')
options.add_argument('disable-infobar')
options.add_argument('--disable-extensions')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2,     # 1:allow, 2:block 
    "profile.default_content_setting_values.media_stream_camera": 2,  # 1:allow, 2:block 
    "profile.default_content_setting_values.geolocation": 2,          # 1:allow, 2:block 
    "profile.default_content_setting_values.notifications": 2         # 1:allow, 2:block 
})
driver = webdriver.Chrome(options=options)
email = sys.argv[2]
password = sys.argv[3]
driver.get('https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346')
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="i0116"]'))).send_keys(email)
time.sleep(2)
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="idSIButton9"]'))).click()
time.sleep(2)
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="i0118"]'))).send_keys(password)
time.sleep(2)
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]'))).click()
time.sleep(2)
driver.get('https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346')
cal = True
#print("logged in")
while True:
  try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@class="app-svg icons-calendar"]'))).click()
    #print('Calendar Opened')
    cal = False
    x = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class,"node_modules--msteams-bridges-components-calendar-event-card-dist-es-src-renderers-event-card-renderer-event-card-renderer__eventCard--h5y4X node_modules--msteams-bridges-components-calendar-event-card-dist-es-src-renderers-event-card-renderer-event-card-renderer__activeCall--25Ch-")]')))[-1]
    x.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Join meeting"]'))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Join now"]'))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="hangup-button"]')))
    join()
  except:
    if cal:
      driver.get('https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346')
      time.sleep(120)
    else:
        time.sleep(60)
    
