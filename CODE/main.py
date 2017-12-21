from util.dialog import Dialog
from util.models.feature import feature

if __name__ == "__main__":

    features = []
    features.append(feature("greetings", "hello", "Hi, how can i help you? :)", None))
    features.append(feature("give time", "what time", "time", None))

    dialog = Dialog(features)
    dialog.start_listening()
    #get_mic()
