import tkinter as tk
import threading
from constants import WINDOW_TITLE, MAX_SIZE, ICON, THIS_WINDOW_NAME
from pystray import MenuItem as item
import pystray
from PIL import Image
import clipboard_handler as ch
import win32gui, win32com.client
import window_style as style


class Window:

    frames = []
    
    def __init__(self, keyboard, clipboard, database):
        self.window, self.background = style.makeWindow()
        self.keyboard = keyboard
        self.clipboard = clipboard
        self.database = database
        self.icon = None
        self.shell = win32com.client.Dispatch("WScript.Shell")


    # Function to create frame...
    def createFrame(self, index, text):

        # Create a frame...
        frame = style.makeFrame(self.background)

        # Create labels...
        label_index = style.makeLabel(frame, index, 'LEFT')
        label_text = style.makeLabel(frame, text, 'RIGHT')

        # putting frame, label_index and label_text into dictionary...
        dic = {'frame' : frame, 'index' : index, 'text' : label_text}
        self.frames.append(dic)


    # Function to create the window...
    def createWindow(self, onPressKey):

        # Binding key press...
        self.window.bind('<Key>', onPressKey)

        # Creating frames...
        for index in range(MAX_SIZE):
            self.createFrame(str(index+1), "")

        # Creating threads...
        keyboardThread = threading.Thread(target=self.keyboard.listen)
        clipboardThread = threading.Thread(target=self.clipboard.listen)

        # Starting all the threads..
        self.window.after(0, keyboardThread.start())
        self.window.after(0, clipboardThread.start())

        # Make windows to be always on top...
        # self.window.attributes('-topmost',True)

        # Protocol to close window...
        self.window.protocol("WM_DELETE_WINDOW", self.hideWindow)

        # Show the window
        self.window.mainloop()
        

    # Function to destroy the window...
    def closeWindow(self):
        if self.icon != None:
            self.icon.stop()
        print("Closing the window...")
        self.window.destroy()
        print("Stopping all the threads...")
        self.keyboard.getListener().stop()


    # Function to update the window...
    def updateWindow(self, titles):
        if(titles == None):
            return

        # Iterating through all the frames...
        for index in range(len(titles)):
            # Changing titles of all the labels
            self.frames[index]['text'].config(text = titles[index])


    # Function to hide window...
    def hideWindow(self, paste=False):

        self.window.withdraw()
        menu = pystray.Menu(item('Show', self.showWindow), item('Quit', self.closeWindow))
        image = Image.open(ICON)
        self.icon = pystray.Icon("name", image, WINDOW_TITLE, menu)
        if paste:
            ch.pasteClipboard()
        self.icon.run()


    # Function to show window...
    def showWindow(self):
        if self.icon != None:
            self.icon.stop()
        self.window.after(0, self.window.deiconify())
        self.showOnTop()


    # Function to make this window foreground...
    def showOnTop(self):
        openWindows = []
        this_hwnd = None

        # Getting all the opened windows in to the array...
        def winEnumHandler( hwnd, ctx ):
            if win32gui.IsWindowVisible( hwnd ):
                openWindows.append(hwnd)

        # Getting all the open windows...
        win32gui.EnumWindows( winEnumHandler, None )

        # Getting this window...
        for hwnd in openWindows:
            if win32gui.GetWindowText(hwnd) == THIS_WINDOW_NAME:
                this_hwnd = hwnd
                break

        # Getting current foreground window...
        current_hwnd = win32gui.GetForegroundWindow()

        # Setting foreground window as Clipboard window is it is in background...
        if this_hwnd != None and current_hwnd != None:
            if openWindows.index(this_hwnd) > openWindows.index(current_hwnd):
                self.shell.SendKeys('%')
                win32gui.SetForegroundWindow(this_hwnd)


    # # Function to show previous open window...
    # def showPreviousWindow(self):
    #     openWindows = []
    #     prev_window_hwnd = None

    #     def winEnumHandler( hwnd, ctx ):
    #         if win32gui.IsWindowVisible( hwnd ):
    #             openWindows.append(hwnd)

    #     win32gui.EnumWindows( winEnumHandler, None )
    #     hwnd_current = win32gui.GetForegroundWindow()

    #     for i in range(len(openWindows)):
    #         if(hwnd_current == openWindows[i]):
    #             prev_window_hwnd = openWindows[i+1]

    #     win32gui.SetForegroundWindow(prev_window_hwnd)