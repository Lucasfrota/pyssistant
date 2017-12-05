import speech_recognition as sr
import urllib

def is_connected():
    status = None
    try:
        url = "https://www.google.com"
        urllib.urlopen(url)
        status = True
    except:
        status = False

    return status

def get_audio(audio):
    command = ""
    r = sr.Recognizer()
    try:
        if(is_connected() == True):
            command = r.recognize_google(audio)
        else:
            command = r.recognize_sphinx(audio)
    except sr.UnknownValueError:
        print "I couldn't understand, sorry :("
    except sr.RequestError as e:
        print("something went wrong: {0}".format(e))

    return command
