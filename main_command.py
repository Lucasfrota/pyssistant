import datetime
import speech

def get_main_command(result):

    message = ""
    conversation_state = True

    if "hello" in result:
        message = "Hi, how can i help you? :)"
    elif "what time" in result:
        message = "Now it is: " + str(datetime.datetime.now().time())
    elif "who are you" in result:
        message = "Well actually I am a computer program, thus I'm no much more than logic being implemented over wire and some electricity, but I may help you if you like :)"
    elif "report" in result:
        message = ""
    elif "bye" in result:
        message = "See you later :)"
        conversation_state = False
    else:
        message = "Sorry, I didn't understand what you said"

    print message
    #speech.say(message)
    return conversation_state
