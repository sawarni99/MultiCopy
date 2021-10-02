from constants import MAX_SIZE, MAX_SIZE_TEXT_TITLE

# Initializations...
storedTexts = [None]*MAX_SIZE

# Function to check data format...
def filterData(text):
    filteredText = ""

    # iterate through the text...
    for char in text:
        if ord(char) >= 0 and ord(char) <= 127:
            filteredText += char
    
    return filteredText


# Function to store data...
def storeData(text):
    # Checking if text is None or empty...
    if text == None or text == "":
        return

    # Filtering text...
    text = filterData(text)

    # Checking if same text is being entered into the array...
    if text in storedTexts:
        return

    # Iterating through the array to shift every text...
    for index in range(MAX_SIZE-1, 0, -1):
        storedTexts[index] = storedTexts[index-1]
    
    # Adding data to first index...
    storedTexts[0] = text


# Function to get data...
def getData(index):
    return storedTexts[index]

# Function to get all datas...
def getAllData():
    return storedTexts

# Function to get heading for the data...
def getTitle(index):
    text = storedTexts[index]

    # Checking if text is Null...
    if text == None:
        return ""

    # Checking if length of text is greater than max size of title...
    if len(text) <= MAX_SIZE_TEXT_TITLE:
        return text

    return text[0:MAX_SIZE_TEXT_TITLE+1]

# Function to get all the titles...
def getAllTitles():
    titles = []
    for index in range(MAX_SIZE):
        titles.append(getTitle(index))
    return titles

# Function to check if given char is numerical....
def checkInteger(char):
    if char == None or len(char) <= 0:
        return False

    if ord(char) > 47 and ord(char) < 58:
        return True
    return False

# Checking if integer index is present...
def checkIndex(index):
    if index >= MAX_SIZE:
        return False
    return True

def convertCharInt(char):
    if checkInteger(char):
        return ord(char) - 48
    return None
