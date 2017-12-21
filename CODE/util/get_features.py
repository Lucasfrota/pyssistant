from models.feature import feature
from feature_functions import *

def get_features():
    features = []
    features.append(feature("greetings", "hello", "Hi, how can i help you? :)", None))
    features.append(feature("give time", "what time", None, get_time ))
    features.append(feature("explanation", "who are you", "Well actually I am a computer program, thus I'm no much more than logic being implemented over wire and some electricity, but I may help you if you like :)", None))
    features.append(feature("report", "report", None, get_report ))
    features.append(feature("quit", "bye", "See you later :)", get_bye))
    features.append(feature("shut down", "shut down", "shutting down", get_shut_down ))
    features.append(feature("what can you do", "what can you do", None, what_can_i_do ))
    features.append(feature("open android studio", "studio", None, open_android_studio))
    features.append(feature("love question", "you love me", "I am a computer, I don't have feelings but if I had im pretty sure i'd love to love you", None))
    features.append(feature("what do you think about python?", "what do you think about python", "I love python, I am literally built of python :)", None))
    features.append(feature("clear", "clear", "ok cleaning screen now", get_clean_screen))
    features.append(feature("open firefox", "open firefox", None, open_firefox))
    features.append(feature("run program", "run", None, run_program))
    return features
