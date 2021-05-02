import requests
import colorama
import time
import os
from os import environ
colorama.init(convert=True)
os.system('cls')
currentversion = "0.3.5"
datatest = {
                'username': 'Zeus Update Checker',
                'avatar_url': 'https://rblxexploits.com/assets/images/zeuspicnew-320x180.png',
                'content': "I'm online!"
                }
test = requests.post(environ['WEBHOOK'], data=currentversion)
print(" Checking if Zeus has updated!")
while True:
    os.system('cls')
    named_tuple = time.localtime()
    time_string = time.strftime("%H:%M:%S, %m/%d/%Y", named_tuple)
    r = requests.get(environ['PASTEBIN'])
    version = r.text
    if version !=  currentversion:
        print(colorama.Fore.RED + "["  + str(time_string)  + "]" + colorama.Fore.WHITE + " Zeus updated to version " + str(r.text) + " at " + str(time_string))
        content = "Zeus has updated to version " + str(r.text) + " at " + str(time_string)
        data = {
                'username': 'Zeus Update Checker',
                'avatar_url': 'https://rblxexploits.com/assets/images/zeuspicnew-320x180.png',
                'content': content
                }
        r = requests.post(environ['WEBHOOK'], data=data)
        currentversion = version
    else:
        print(colorama.Fore.GREEN + "["  + str(time_string)  + "]" + colorama.Fore.WHITE + " Checking if Zeus has updated!")
        time.sleep(10)