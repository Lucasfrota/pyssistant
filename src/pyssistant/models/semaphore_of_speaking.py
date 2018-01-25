class SemaphoreOfSpeaking():
    class __Singleton():

        def __init__(self):
            self._is_instantiated = False
            self._instance = None
            self.is_speaking = False

        def get_instance(self):
            if(self._is_instantiated == False):
                self._instance = SemaphoreOfSpeaking()
                self._is_instantiated = True
                return self._instance
            else:
                return self._instance

    singleton = __Singleton()

    def set_speaking_state(self, state):
        self.singleton.is_speaking = state

    def get_speaking_state(self):
        return self.singleton.is_speaking

    def get_instance(self):
        return self.singleton.get_instance()
