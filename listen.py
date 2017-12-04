import speech_recognition as sr

def listen():
    audio = None
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        audio = r.listen(source, phrase_time_limit=5)
        print("thinking...")
    return audio
