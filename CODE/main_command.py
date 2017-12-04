import datetime
import speech
import psutil
import os

def get_main_command(result):

    message = ""
    conversation_state = True

    if "hello" in result:
        message = "Hi, how can i help you? :)"
    elif "what time" in result:
        message = "Now it is: " + str(datetime.datetime.now().time())
    elif "who are you" in result:
        message = "Well actually I am a computer program, thus I'm no much more than logic being implemented over wire and some electricity, but I may help you if you like :)"
    elif "report" in result:
        message = "battery: " + str(psutil.sensors_battery().percent) + "%"
    elif "bye" in result:
        message = "See you later :)"
        conversation_state = False
    elif "shut down" in result:
        message = "shutting down"
        os.system('shutdown -s')
    elif "what can you do" in result:
        message = "currently I can tell you:\n-battery state\n-what time it is"
    else:
        message = "Sorry but '" + result + "', doesn't mean anything to me"

    print message
    #speech.say(message)
    return conversation_state
