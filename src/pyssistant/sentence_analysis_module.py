from gtts import gTTS
from tempfile import TemporaryFile

def play_message(sentence, mp3_name):
    tts = gTTS(text=sentence, lang="en")
    f = TemporaryFile()
    tts.write_to_fp(f)
    f.close()

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

        play_message(message, "text")
        return message
