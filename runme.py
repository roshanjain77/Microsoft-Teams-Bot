import os
import time

os.system('sudo killall chrome')
os.system('sudo killall chromedriver')
os.system('sudo rm -fr /tmp/.com*')
with open('/home/ubuntu/Microsoft-Teams-Bot/cnt.log','a') as f:
    f.write('.')
with open('/home/ubuntu/Microsoft-Teams-Bot/list','r') as f:
    profiles = f.readlines()
    for profile in profiles:
        time.sleep(120)
        data = profile[:-1].split(' ')
        if len(data) == 4:
            os.system(f'/home/ubuntu/anaconda3/bin/python /home/ubuntu/Microsoft-Teams-Bot/teams.py {data[0]} {data[1]} {data[2]} {data[3]} &')
time.sleep(15)
