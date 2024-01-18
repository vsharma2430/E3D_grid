from PyQt5.QtGui import (QFont,QIcon)
from PyQt5.QtCore import (QSize)
from PyQt5.QtWidgets import (
    QLineEdit,
    QPushButton,
    QLabel,
    QFrame,
    QTextEdit,
    QSizePolicy,
    QRadioButton,
    QTableWidget,
    QTableWidgetItem,
    QComboBox
)
from tkinter import messagebox
import os

def getEditText(hintText:str="",minWidth:int=30,maxWidth:int=500,height:int=30,maxHeight:int=100,fontSize:int=12):
    editText = QTextEdit()
    editText.setMinimumWidth(minWidth)
    editText.setMaximumWidth(maxWidth)
    editText.setMinimumHeight(height)
    editText.setMaximumHeight(maxHeight)
    editText.setFont(getFont(fontSize))
    return editText    

def getLineEdit(hintText:str="",minWidth:int=30,maxWidth:int=500,height:int=30,maxHeight:int=100,fontSize:int=12,password_mode:bool=False):
    editText = QLineEdit()
    editText.setMinimumWidth(minWidth)
    editText.setMaximumWidth(maxWidth)
    editText.setMinimumHeight(height)
    editText.setMaximumHeight(maxHeight)
    editText.setFont(getFont(fontSize))
    editText.setPlaceholderText(hintText)
    if(password_mode):
        editText.setEchoMode(QLineEdit.Password)
    return editText    

def getLabel(text:str,minWidth:int=30,maxWidth:int=500,height:int=30,fontSize:int=12):
    label = QLabel(text)
    label.setMinimumWidth(minWidth)
    label.setMaximumWidth(maxWidth)
    label.setMinimumHeight(height)
    label.setFont(getFont(fontSize))
    return label    

def getButton(clickFunction,text:str="Button",fontSize:int=12,framewidth:int=100,frameHeight:int=40):
    button = QPushButton()
    button.setText(text)
    button.setMinimumWidth(framewidth)
    button.setMinimumHeight(frameHeight)
    button.setFont(getFont(fontSize))
    button.clicked.connect(clickFunction)
    return button

def getRadioButton(clickFunction,text:str="RadioButton",fontSize:int=12,maxWidth:int=500,framewidth:int=100,frameHeight:int=40):
    radioButton = QRadioButton()
    radioButton.setText(text)
    radioButton.setMaximumWidth(maxWidth)
    radioButton.setMinimumWidth(framewidth)
    radioButton.setMinimumHeight(frameHeight)
    radioButton.setFont(getFont(fontSize))
    radioButton.clicked.connect(clickFunction)
    return radioButton

def getTableWidget(fontSize:int=12,maxWidth:int=500,minWidth:int=100,frameHeight:int=40):
    tableWidget = QTableWidget()
    tableWidget.setMinimumWidth(minWidth)
    tableWidget.setMinimumHeight(frameHeight)
    tableWidget.setMaximumWidth(maxWidth)
    tableWidget.setFont(getFont(fontSize))
    return tableWidget

def getTableWidgetItem(data:str=''):
    tableWidgetItem = QTableWidgetItem(data)
    return tableWidgetItem

def getQIcon(imagename):
    imagename = os.path.basename(imagename)
    if(os.path.exists('./images')):
        return QIcon('./images/' + imagename)
    else:
        return QIcon('_internal/img/'+ imagename)

def getIconButton(clickFunction=None,imagePath:str='',framewidth:int=100,frameHeight:int=40,iconPadding:int=2,text:str="",fontSize:int=14):
    button = QPushButton()
    if(imagePath!=''):
        button.setIcon(getQIcon(imagePath))
    button.setFixedWidth(framewidth)
    button.setMinimumHeight(frameHeight)
    if(clickFunction!=None):
        button.clicked.connect(clickFunction)
    button.setIconSize(QSize(framewidth-iconPadding,frameHeight-iconPadding))
    if(text!=""):
        button.setText(text)
        button.setFont(getFont(fontSize))
    return button

def getFont(fontSize:int=12,fontname:str=''):
    font = QFont()
    if(fontname!=''):
        font.setFamily('Bahnschrift')
    font.setPointSize(fontSize)
    font.styleHint = QFont.Monospace
    return font

def getHSeparator():
    Separator = QFrame()
    Separator.setFrameShape(QFrame.HLine)
    Separator.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)
    Separator.setLineWidth(2)
    return Separator

def getVSeparator():
    Separator = QFrame()
    Separator.setFrameShape(QFrame.VLine)
    Separator.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Minimum)
    Separator.setLineWidth(2)
    return Separator


def getYesNoBox(header:str='Confirmation',message:str='Do you want to proceed?'):
    result = messagebox.askyesno(header, message)
    if result:
        return True
    else:
        return False
    
def getComboBox(data : list[str]=[],fontSize:int=12,maxWidth:int=500,minWidth:int=100,frameHeight:int=40):
    combo = QComboBox()
    combo.setMinimumWidth(minWidth)
    combo.setMinimumHeight(frameHeight)
    combo.setMaximumWidth(maxWidth)
    combo.setFont(getFont(fontSize))
    for dataX in data:
        combo.addItem(dataX)
    return combo

def getFloat(data:str)->float:
    return 0 if data=='' or data==None else float(data)
