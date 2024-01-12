from PyQt5.QtGui import (QFont,QIcon)
from PyQt5.QtCore import (QSize)
from PyQt5.QtWidgets import (
    QLineEdit,
    QPushButton,
    QLabel,
    QFrame,
    QTextEdit,
    QSizePolicy
)
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

def getQIcon(imagename):
    imagename = os.path.basename(imagename)
    if(os.path.exists('./images')):
        return QIcon('./images/' + imagename)
    else:
        return QIcon('_internal/img/'+ imagename)

def getIconButton(clickFunction,imagePath:str,framewidth:int=100,frameHeight:int=40,iconPadding:int=2,text:str="",fontSize:int=14):
    button = QPushButton()
    button.setIcon(getQIcon(imagePath))
    button.setMinimumWidth(framewidth)
    button.setMinimumHeight(frameHeight)
    button.clicked.connect(clickFunction)
    button.setIconSize(QSize(framewidth-iconPadding,frameHeight-iconPadding))
    if(text!=""):
        button.setText(text)
        button.setFont(getFont(fontSize))
    return button

def getFont(fontSize):
    font = QFont("Arial")
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