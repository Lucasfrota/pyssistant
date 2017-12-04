from listen import listen
from get_audio import get_audio
from main_command import get_main_command

if __name__ == "__main__":

    conversation_state = True
    while conversation_state:
        audio = listen()
        result = get_audio(audio)

        conversation_state = get_main_command(result)
