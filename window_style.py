import tkinter as tk
from tkinter.constants import BOTH
from constants import WINDOW_TITLE, FRAME_BG, WINDOW_BG

# Function to make window...
def makeWindow():

    # Creating window...
    window = tk.Tk()

    # Changing Windows Title...
    window.title(WINDOW_TITLE)

    # Changing background color...
    background = tk.Frame(window, relief='flat', bg=WINDOW_BG)
    background.pack()

    return (window, background)

# function to make Frame...
def makeFrame(window):

    # Creating a frame...
    frame = tk.Frame(window)
    frame.pack(fill= BOTH, expand=True, padx=12, pady=6)

    return frame

# function to create labels
def makeLabel(window, text, side):
    label = None

    # Creating a label...
    if side == 'LEFT':
        label = tk.Label(window, text=text, width=10, height=4, bg=FRAME_BG)
        label.grid(column=1, row=0)

    if side == 'RIGHT':
        label = tk.Label(window, text=text, width=35, height=4, bg=FRAME_BG)
        label.grid(column=2, row=0)

    return label