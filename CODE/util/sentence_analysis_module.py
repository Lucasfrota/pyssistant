from get_features import get_features
from feature_functions import *

class SentenceAnalysis:

    def __init__(self, dialog_list):
        self.dialog_list = dialog_list

    def get_main_command(self, result):

        message = ""
        conversation_state = True
        result = result.lower()

        for feature in self.dialog_list:
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

        print "\n" + message + "\n"
