from get_features import get_features
from feature_functions import *
import os
import speech

features = get_features()

def get_main_command(result):

    message = ""
    conversation_state = True

    result = result.lower()

    for feature in features:
        if feature.command in result:
            if(feature.answer != None):
                message = feature.answer
            if(feature.function != None):
                function = feature.function()
                if(type(function) == str):
                    message = function
                elif(function != None):
                    conversation_state = function
    if(message == ""):
        message = "Sorry but '" + result + "', doesn't mean anything to me"

    #os.system('cls')
    print "\n" + message + "\n"
    #speech.say(message)
    return conversation_state
