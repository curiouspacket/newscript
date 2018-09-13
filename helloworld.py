
import os
import subprocess

hostname = "8.8.8.8"
response = subprocess.call(['ping', '-c', '5', '-W', '3', hostname], stdout=open(os.devnull, 'w') )





def sayhello():
    if response == 0:
        return hostname + " is up!"
    else: 
        return hostname + " is down!"

