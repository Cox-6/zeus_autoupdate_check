import requests
import colorama
import time
import os
from os import environ
colorama.init(convert=True)
os.system('cls')
currentversion = "0.3.5"
while True:
    os.system('cls')
    named_tuple = time.localtime()
    time_string = time.strftime("%H:%M:%S, %m/%d/%Y", named_tuple)
    r = requests.get(environ['PASTEBIN'])
    version = r.text
    if version !=  currentversion:
        content = "Zeus has updated to version " + str(r.text) + " at " + str(time_string)
        data = {
                'username': 'Zeus Update Checker',
                'avatar_url': 'https://rblxexploits.com/assets/images/zeuspicnew-320x180.png',
                'content': content
                }
        r = requests.post(environ['WEBHOOK'], data=data)
        currentversion = version
    else:
        pass
        time.sleep(10)