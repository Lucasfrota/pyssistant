from pyssistant.models.menu import Menu
import datetime
import psutil
import os

def get_time():
    return "Now it is: " + str(datetime.datetime.now().time())

def get_report():
    return "battery: " + str(psutil.sensors_battery().percent) + "%"

def get_bye():
    return False

def get_shut_down():
    print "let's pretend it is shutting down, ok?"
    #os.system('shutdown -s')

def what_can_i_do():
    return "I can do things :)"

def open_android_studio():
    os.system('start notepad')
    return "Opening android studio good luck with java :)"

def get_clean_screen():
    menu = Menu("Do you really want to do this?", "ok", "no")
    answer = menu.show_menu()

    if answer == True:
        os.system('cls')

    return None

def open_firefox():
    os.system('start firefox')
    return "Opening firefox :)"

def run_program():
    #os.system("python run_test.py")
    execfile("python run_test.py")
    return None
