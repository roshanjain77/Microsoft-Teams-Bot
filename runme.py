import os
import time

with open('/home/ubuntu/Microsoft-Teams-Bot/list','r') as f:
    time.sleep(120)
    profiles = f.readlines()
    for profile in profiles:
        data = profile[:-1].split(' ')
        if len(data) == 4:
            os.system(f'/home/ubuntu/anaconda3/bin/python /home/ubuntu/Microsoft-Teams-Bot/teams.py {data[0]} {data[1]} {data[2]} {data[3]} &')
time.sleep(15)
