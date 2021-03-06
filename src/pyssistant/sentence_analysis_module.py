from gtts import gTTS
from tempfile import TemporaryFile
from playsound import playsound
from pyssistant.models.semaphore_of_speaking import SemaphoreOfSpeaking
import datetime
import os

def get_time_str():
    time = str(datetime.datetime.now().time())
    time = time.replace(":", "_")
    return time

def play_message(sentence):
    if sentence != '' or sentence != '\n':
        SemaphoreOfSpeaking().get_instance().set_speaking_state(True)

        tts = gTTS(text=sentence, lang='en')
        filename = "/tmp/temp" + get_time_str() + ".mp3"
        tts.save(filename)

        playsound(filename)

        os.remove(filename)

        SemaphoreOfSpeaking().get_instance().set_speaking_state(False)

class SentenceAnalysis:

    def __init__(self, dialog_list):
        self.dialog_list = dialog_list
        self.__state_inatance = SemaphoreOfSpeaking().get_instance()

    def get_command(self, result):

        message = ""
        conversation_state = True
        result = result.lower()

        message = self.__get_message(result)

        print "\n" + message + "\n"
        play_message(message)
        return conversation_state

    def get_command_in_background(self, result):
        if self.__state_inatance.get_speaking_state() == False:
            result = result.lower()

            if result != '':
                message = self.__get_message_background(result)

                if message != "":
                    print "\n" + message + "\n"

                try:
                    play_message(message)
                except Exception as e:
                    pass

    def __get_message_background(self, result):
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

        return message

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

        return message
