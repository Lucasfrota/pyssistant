"""
Dialog class
"""
from pyssistant.listen import listen
from pyssistant.get_audio import get_audio
from pyssistant.models.feature import feature
from pyssistant.sentence_analysis_module import SentenceAnalysis

class Dialog:
    """
    This class create a loop to stay listeaning at commands, it also defines all
    the commands and its answers
    """
    def __init__(self, dialog_list=[]):#pylint: disable=dangerous-default-value
        self.dialog_list = dialog_list
        self.sentence_analyzer = SentenceAnalysis(self.dialog_list)

    def start_listening(self):
        """start a loop to listen to commands"""
        while True:
            self.listen_once()

    def listen_once(self):
        """listen only to one command"""
        audio = listen()
        result = get_audio(audio)
        self.sentence_analyzer.get_main_command(result)

    def add_dialog(self, command, answer="", function=None):
        """add a command and its features to the list of commands"""
        self.dialog_list.append(feature(command, answer=answer, function=None))
