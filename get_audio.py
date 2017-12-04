import speech_recognition as sr

def get_audio(audio):
    command = ""
    r = sr.Recognizer()
    try:
        command = r.recognize_sphinx(audio)
    except sr.UnknownValueError:
        print "I couldn't understand, sorry :("
    except sr.RequestError as e:
        print("something went wrong: {0}".format(e))

    return command
