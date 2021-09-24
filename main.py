import data_handler as dh
from clipboard_handler import *
from keyboard_handler import Keyboard
from window_handler import Window

# Function on clipboard change event...
def onClipboardChange():
    # Getting clipboard data...
    currentCopy = getCopiedData()

    # Storing the data in array...
    dh.storeData(currentCopy)

    # Get all the titles...
    textTitles = dh.getAllTitles()

    # Change the frames in the window...
    window.updateWindow(textTitles)


# Function when entered a key to paste...
def onPressKey(key):

    # Converting char to integer...
    index = dh.convertCharInt(key.char)

    # Checking if char is converted...
    if index == None :
        print("[Error] Non integral key is pressed...")
        return
    
    # Checking if index present in array...
    if not dh.checkIndex(index-1) or dh.getData(index-1) == None:
        print("[Error] Index out of bound...")
        return

    # Putting selected data into clipboard....
    setClipboard(dh.getData(index-1))

    # Background the window...
    window.hideWindow(paste = True)

# Function on paste event...
def onPressPaste():
    window.showWindow()


if __name__ == "__main__":

    # Initializing objects for listeners...
    clipboardUpdate = Clipboard(onClipboardChange)
    keyboardUpdate = Keyboard(onPressPaste)

    # Creating window object to create window...
    window = Window(keyboardUpdate, clipboardUpdate)
    window.createWindow(onPressKey)