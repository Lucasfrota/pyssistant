import datetime
import psutil
import os

def get_time():
    return "Now it is: " + str(datetime.datetime.now().time())

def get_report():
    return "battery: " + str(psutil.sensors_battery().percent) + "%"

def get_shut_down():
    print "let's pretend it is shutting down, ok?"
    #os.system('shutdown -s')

def what_can_i_do():
    return "I can do things :)"

def open_android_studio():
    os.system('start notepad')
    return "Opening android studio good luck with java :)"
