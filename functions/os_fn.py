#Here we will create various fn to interact with the os
import os                   #for interacting with os
import subprocess as sp     

path = {
    'discord':"C:\\Users\\ASUS\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calc':"C:\\Windows\\System32\\calc.exe"
}

#To open apps that are given in path
def open_calc():
    sp.call(path['calc'])

def open_discord():
    sp.call(path['discord'])

#Open Camera
def open_camera():
    sp.run('start microsoft.windows.camera:',shell=True)

#Open cmd
def open_cmd():
    sp.call('cmd.exe',shell=True)
