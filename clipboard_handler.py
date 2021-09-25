import ctypes
import threading
import win32api
import win32gui
from pynput.keyboard import Key, Controller
import clipboard


# Function to paste data from clipboard...
def pasteClipboard():
    print("Pasting from clipboard...")
    keyboard = Controller()

    # Trigger paste command by controlling keys ctrl+v...
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl)

# Function to return copied data from clipboard...
def getCopiedData():
    return clipboard.paste()

# Function to put data in clipboard....
def setClipboard(text):
    if text == None:
        print("[Error] No value given to set to clipboard")
        return
    
    clipboard.copy(text)
        


# Functions to detect if clipboard is updated in Windows...
class Clipboard:
    def __init__(self, doThis):
        self.onClipboardUpdate = doThis

    def _create_window(self) -> int:
        wc = win32gui.WNDCLASS()
        wc.lpfnWndProc = self._process_message
        wc.lpszClassName = self.__class__.__name__
        wc.hInstance = win32api.GetModuleHandle(None)
        class_atom = win32gui.RegisterClass(wc)
        return win32gui.CreateWindow(class_atom, self.__class__.__name__, 0, 0, 0, 0, 0, 0, 0, wc.hInstance, None)

    def _process_message(self, hwnd: int, msg: int, wparam: int, lparam: int):
        WM_CLIPBOARDUPDATE = 0x031D
        if msg == WM_CLIPBOARDUPDATE:
            # If Clipboard is updated...
            self.onClipboardUpdate()
        return 0

    def listen(self):
        print("Listening to clipboard....")
        def runner():
            hwnd = self._create_window()
            ctypes.windll.user32.AddClipboardFormatListener(hwnd)
            win32gui.PumpMessages()

        th = threading.Thread(target=runner, daemon=True)
        th.start()
