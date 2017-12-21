from listen import listen
from get_audio import get_audio
from sentence_analysis_module import SentenceAnalysis

class Dialog:

    def __init__(self, dialog_list):
        self.dialog_list = dialog_list
        self.sentence_analyzer = SentenceAnalysis(self.dialog_list)

    def start_listening(self):
        while True:
            self.listen_once()

    def listen_once(self):
        audio = listen()
        result = get_audio(audio)
        self.sentence_analyzer.get_main_command(result)
