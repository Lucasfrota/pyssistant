import speech_recognition as sr

def listen(name):
    audio = None
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening " + name)
        audio = r.listen(source, phrase_time_limit=4)
        print("thinking... " + name )
    return audio
