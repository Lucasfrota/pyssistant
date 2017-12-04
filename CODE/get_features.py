from feature_model import feature
from feature_functions import *

def get_features():
    features = []
    features.append(feature("greetings", "hello", "Hi, how can i help you? :)", None))
    features.append(feature("give time", "what time", None, get_time ))
    features.append(feature("explanation", "who are you", "Well actually I am a computer program, thus I'm no much more than logic being implemented over wire and some electricity, but I may help you if you like :)", None))
    features.append(feature("report", "report", None, get_report ))
    features.append(feature("quit", "bye", "See you later :)", None))
    features.append(feature("shut down", "shut down", "shutting down", get_shut_down ))
    features.append(feature("what can you do", "what can you do", None, what_can_i_do ))
    return features
