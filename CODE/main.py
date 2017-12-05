from util.listen import listen
from util.get_audio import get_audio
from util.main_command import get_main_command
import thread
import threading
import time

def get_mic(name):
    conversation_state = True
    while conversation_state:
        audio = listen(name)
        result = get_audio(audio)
        conversation_state = get_main_command(result)

if __name__ == "__main__":

    #get_mic()

    try:
        threading.Thread(target=get_mic, args=("thread 1", ) ).start()
        time.sleep(3)
        threading.Thread(target=get_mic, args=("thread 2", ) ).start()
    except Exception:
        print "Error"
