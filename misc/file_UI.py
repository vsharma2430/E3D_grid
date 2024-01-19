import tkinter as tk 
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile
import os 

def selectFile():
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    Tk().withdraw()
    filename = askopenfilename()
    return (filename)

def saveFile_win_mac():
    f = asksaveasfile(initialfile = 'Untitled.dat',
            defaultextension=".dat",filetypes=[("All Files","*.*"),("Grid Database File","*.dat")])
    tk.Tk().withdraw()
    return f.name

def readLineByLine (fileLocation) : 
    readLines = []
    if(fileLocation!=None and fileLocation!='' and os.path.exists(fileLocation)):
        file1 = open(fileLocation, 'r')
        Lines = file1.readlines()
        count = 0
        # Strips the newline character
        for line in Lines:
            count += 1
            readLines.append(line.strip())
            #print("Line{}: {}".format(count, line.strip()))
        file1.close()
    return readLines