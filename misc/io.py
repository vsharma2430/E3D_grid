import webbrowser
from PyQt5.QtWidgets import QFileDialog
from pathlib import Path

def selectFile ():
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    Tk().withdraw()
    filename = askopenfilename()
    return (filename)

def open_url(url):
   webbrowser.open_new_tab(url)

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
    file1.close()
    return readLines

#not working right now,needs a parent Qwidget
def get_multiple_files():
    filenames, _ = QFileDialog.getOpenFileNames("Select Files")
    file_list:list(str) = []
    if filenames:
        file_list.addItems([str(Path(filename))
                                    for filename in filenames])
    return file_list
