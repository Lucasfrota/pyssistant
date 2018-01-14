from gtts import gTTS
from tempfile import TemporaryFile
from playsound import playsound
import datetime
import os

def get_time_str():
    time = str(datetime.datetime.now().time())
    #time = time[2] = "_"
    return time

def play_message(sentence):
    tts = gTTS(text=sentence, lang='en')
    filename = "/tmp/temp" + get_time_str() + ".mp3"
    tts.save(filename)

    playsound(filename)

    os.remove(filename)

class SentenceAnalysis:

    def __init__(self, dialog_list):
        self.dialog_list = dialog_list

    def get_main_command(self, result):

        message = ""
        conversation_state = True
        result = result.lower()

        message = self.__get_message(result)

        print "\n" + message + "\n"
        return conversation_state

    def __get_message(self, result):
        message = ""

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

        play_message(message)
        return message
