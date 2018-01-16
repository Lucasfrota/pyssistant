"""
Dialog class
"""
from pyssistant.listen import listen, lsiten_silently
from pyssistant.get_audio import get_audio, get_audio_silently
from pyssistant.models.feature import feature
from pyssistant.sentence_analysis_module import SentenceAnalysis

import threading
import time

class Dialog:
    """
    This class create a loop to stay listeaning at commands, it also defines all
    the commands and its answers
    """
    def __init__(self, dialog_list=[]):#pylint: disable=dangerous-default-value
        self.dialog_list = dialog_list
        self.sentence_analyzer = SentenceAnalysis(self.dialog_list)
        self.__has_said_the_key_word = False

    def __from_speach_to_text(self, key_word):
        #self.__has_said_the_key_word = False
        while not self.__has_said_the_key_word:
            audio = lsiten_silently()
            result = get_audio_silently(audio)
            if key_word in result:
                if not self.__has_said_the_key_word:
                    self.listen_once()
                self.__has_said_the_key_word = True

    def start_listening(self):
        """start a loop to listen to commands"""
        while True:
            self.listen_once()

    def listen_once(self):
        """listen only to one command"""
        audio = listen()
        result = get_audio(audio)
        self.sentence_analyzer.get_main_command(result)

    def wait_call(self, key_word):
        try:
            threading.Thread(target=self.__from_speach_to_text, args=(key_word, ) ).start()
            time.sleep(1)
            threading.Thread(target=self.__from_speach_to_text, args=(key_word, ) ).start()
            time.sleep(1)
            threading.Thread(target=self.__from_speach_to_text, args=(key_word, ) ).start()

        except Exception as e:
            print "Error: " + str(e)

    def add_dialog(self, command, answer="", function=None):
        """add a command and its features to the list of commands"""
        self.dialog_list.append(feature(command, answer=answer, function=None))
