from pyssistant.dialog import Dialog
from pyssistant.models.feature import feature
from pyssistant.feature_functions import *

features = []
features.append(feature("what time", function = get_time ))
features.append(feature("who are you", answer = "Well actually I am a computer program, thus I'm no much more than logic being implemented over wire and some electricity, but I may help you if you like :)"))
features.append(feature("report", function = get_report ))
features.append(feature("bye", answer = "See you later :)", function = get_bye))
features.append(feature("shut down", answer = "shutting down", function = get_shut_down ))
features.append(feature("what can you do", what_can_i_do ))
features.append(feature("studio", open_android_studio))
features.append(feature("you love me", answer = "I am a computer, I don't have feelings but if I had im pretty sure i'd love to love you"))
features.append(feature("what do you think about python", answer = "I love python, I am literally built of python :)"))
features.append(feature("clear", answer = "ok cleaning screen now", function = get_clean_screen))
features.append(feature("open firefox", function = open_firefox))
features.append(feature("run", function = run_program))

if __name__ == "__main__":

    dialog = Dialog(features)
    dialog.add_dialog("hello", answer = "Hi, how can i help you? :)")
    dialog.start_listening()
