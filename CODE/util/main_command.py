from get_features import get_features
from feature_functions import *
import os
import speech

features = get_features()

def get_main_command(result):

    message = ""
    conversation_state = True

    for feature in features:
        if feature.command in result:
            if(feature.answer != None):
                message = feature.answer
            if(feature.function != None):
                message = feature.function()
    if(message == ""):
        message = "Sorry but '" + result + "', doesn't mean anything to me"

    #os.system('cls')
    print message
    #speech.say(message)
    return conversation_state
