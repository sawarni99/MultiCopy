import data_handler as dh
from clipboard_handler import *
from keyboard_handler import Keyboard
from window_handler import Window
from db_handler import Database

# Function on clipboard change event...
def onClipboardChange():
    # Getting clipboard data...
    currentCopy = getCopiedData()

    # Storing the data in array...
    dh.storeData(currentCopy)

    # Showing data on window...
    show_data_window()


# Function when entered a key to paste...
def onPressKey(key):

    # Checking if S button is press...
    if(key.char == 's'):
        # Saving all copied text in db...
        save_in_db()
        return

    # Checking if P is pressed...
    if(key.char == 'p'):
        # get datas from db...
        get_from_db()
        return

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


# Function to save texts in database...
def save_in_db():
    texts = dh.getAllData()
    db.update(texts)


# Function to get texts from databse...
def get_from_db():
    texts = db.get_data()

    # storing all the data into the array...
    for text in texts:
        dh.storeData(text)

    # Showing data on the window...
    show_data_window()


# Function to show data into window...
def show_data_window():

    # Get all the titles...
    textTitles = dh.getAllTitles()

    # Change the frames in the window...
    window.updateWindow(textTitles)


# Function on paste event...
def onPressPaste():
    window.showWindow()


if __name__ == "__main__":

    # Initializing database....
    db = Database()
    db.initialize()

    # Initializing objects for listeners...
    clipboardUpdate = Clipboard(onClipboardChange)
    keyboardUpdate = Keyboard(onPressPaste)

    # Creating window object to create window...
    window = Window(keyboardUpdate, clipboardUpdate, db)
    window.createWindow(onPressKey)