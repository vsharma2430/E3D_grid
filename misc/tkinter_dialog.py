from tkinter.filedialog import asksaveasfile,askopenfilename

#DEFUNCT -USE pyqtopendialogbox
def selectFile():
    filename = askopenfilename()
    return (filename)

#DEFUNCT -USE pyqtsavedialogbox
def saveFile_win_mac():
    f = asksaveasfile(initialfile = 'Untitled.dat',
            defaultextension=".dat",filetypes=[("All Files","*.*"),("Grid Database File","*.dat")])
    return f.name
