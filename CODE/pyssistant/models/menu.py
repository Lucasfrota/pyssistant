from pyssistant.listen import listen
from pyssistant.get_audio import get_audio

class Menu:

    def __init__(self, question, positive_answer, negative_answer):
        self.question = question
        self.positive_answer = positive_answer
        self.negative_answer = negative_answer
        self.answer = None

    def show_menu(self):

        while self.answer == None:
            print "\n    " + str(self.answer) + "\n"
            print "\n    " + self.question
            print "    Say: " + self.positive_answer + " to DO it."
            print "    Say: " + self.negative_answer + " to DON'T it.\n"

            audio = listen("    ")
            result = get_audio(audio)
            if self.positive_answer in result:
                self.answer = True
            elif self.negative_answer in result:
                self.answer = False
            else:
                print "    Sorry but '" + result + "', doesn't mean anything to me"

        return self.answer
