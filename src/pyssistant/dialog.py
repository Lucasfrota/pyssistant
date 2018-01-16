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
        self.__list_threads = []
        self.__has_said_the_key_word = False

    def __from_speach_to_text(self, key_word):
        while not self.__has_said_the_key_word:
            audio = lsiten_silently()
            result = get_audio_silently(audio)
            #print result
            if key_word in result:
                if not self.__has_said_the_key_word:
                    print "you said the word: " + key_word
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
            t1 = threading.Thread(target=self.__from_speach_to_text, args=(key_word, ) )
            t1.start()
            time.sleep(1)

            t2 = threading.Thread(target=self.__from_speach_to_text, args=(key_word, ) )
            t2.start()
            time.sleep(1)

            t3 = threading.Thread(target=self.__from_speach_to_text, args=(key_word, ) )
            t3.start()
            time.sleep(1)

            t4 =threading.Thread(target=self.__from_speach_to_text, args=(key_word, ) )
            t4.start()

            self.__list_threads.append(t1)
            self.__list_threads.append(t2)
            self.__list_threads.append(t3)
            self.__list_threads.append(t4)

        except Exception as e:
            print "Error: " + str(e)

    def add_dialog(self, command, answer="", function=None):
        """add a command and its features to the list of commands"""
        self.dialog_list.append(feature(command, answer=answer, function=None))
