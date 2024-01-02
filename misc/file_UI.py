import tkinter as tk 
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile

def selectFile():
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    Tk().withdraw()
    filename = askopenfilename()
    return (filename)

def saveFile_win_mac():
    f = asksaveasfile(initialfile = 'Untitled.mac',
            defaultextension=".mac",filetypes=[("All Files","*.*"),("Macro Files","*.mac")])
    tk.Tk().withdraw()
    return f.name

def readLineByLine (fileLocation) : 
    file1 = open(fileLocation, 'r')
    Lines = file1.readlines()
    readLines = []
    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        readLines.append(line.strip())
        #print("Line{}: {}".format(count, line.strip()))
    return readLines