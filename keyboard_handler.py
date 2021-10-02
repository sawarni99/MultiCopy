from pynput import keyboard
from constants import HOT_KEY_PASTE


class Keyboard:

    # Constructor...
    def __init__(self, onPressPaste):
        self.listener = None
        self.onPressPaste = onPressPaste

    def getListener(self):
        return self.listener

    # Function to start keyboard Listener...
    def listen(self):
        with keyboard.GlobalHotKeys({HOT_KEY_PASTE : self.onPressPaste}) as listener:
                self.listener = listener
                self.listener.join()