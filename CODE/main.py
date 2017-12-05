from util.listen import listen
from util.get_audio import get_audio
from util.main_command import get_main_command
import threading
import time

def get_mic():
    conversation_state = True
    while conversation_state:
        audio = listen()
        result = get_audio(audio)
        conversation_state = get_main_command(result)

if __name__ == "__main__":

    #get_mic()

    try:
        threading.Thread(target=get_mic, args=() ).start()
        time.sleep(4)
        threading.Thread(target=get_mic, args=() ).start()
    except Exception:
        print "Error"
