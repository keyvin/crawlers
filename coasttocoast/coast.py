import time
import datetime
import os
from selenium import webdriver
import auth_tokens

chrome = webdriver.Chrome()
date = datetime.date.today()
date = date - datetime.timedelta(days=6)
month = str(date.month)
day = str(date.day)

if len(month) == 1:
    month = '0' + month
if len(day) == 1:
    day = '0' + day
    
chrome.get(f'https://www.coasttocoastam.com/show/{date.year}/{month}/{day}')

chrome.execute_script('showLoginPopup()')
time.sleep(2)
v = chrome.find_element_by_id('username')
v.send_keys(auth_tokens.coast_username)
v = chrome.find_element_by_id('password')
v.send_keys(auth_tokens.coast_password)
time.sleep(2)
v = chrome.find_element_by_class_name('btn-login')
v.click()
time.sleep(1)
chrome.get(f'https://www.coasttocoastam.com/show/{date.year}/{month}/{day}')
time.sleep(5)

v = chrome.find_elements_by_class_name('streamlink-dynamic')
mp3s = []

for i in v:
    if 'Hour' in i.text:
        try:
            print("fetching - " + str(i.get_attribute('href')))
            mp3s.append(i.get_attribute('href'))
        except:
            print("failure")

os.system(f'mkdir -p ~/coast/{date.year}{date.month}{date.day}/')
time.sleep(1)
os.chdir(f'/home/keyvin/coast/{date.year}{date.month}{date.day}/')


description = open('description.html', 'w')
description.write(chrome.page_source)
description.close()

chrome.close()
os.system('killall chromium')
count = 1

for i in mp3s:
    os.system(f'wget {i} -O {count}.mp3')
    count = count + 1
    


            

#os.system('wget ' + v.get_atribute('href'))
#time.sleep(5)
#v = v[6]
#v.send_keys('\n')
#v.click()









