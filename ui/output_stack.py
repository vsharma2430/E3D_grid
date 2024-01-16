#import necessary modules 
from PyQt5.QtWidgets import (QWidget, QAction, QVBoxLayout,QHBoxLayout,QPushButton,QLineEdit,
    QMessageBox, QTextEdit, QFileDialog, QInputDialog, QFontDialog,QGroupBox,QGridLayout)
from PyQt5.QtGui import QTextCursor, QColor
from PyQt5.QtCore import Qt
from ui.common_helper import getIconButton,getLabel,getEditText

class OutputWidget(QWidget):

    output:QTextEdit
    copy_button:QPushButton
    save_button:QPushButton
    clear_button:QPushButton

    def __init__(self):
        super().__init__()
        self.initializeUI()
        self.createUI()

    def save_command(self):
        return
    def copy_command(self):
        return
    def clear_command(self):
        return
    
    def initializeUI(self):
        self.setMinimumHeight(250)
        self.setMaximumHeight(350)

        self.output = getEditText('Output command',maxWidth=1000,minWidth=300,maxHeight=350)
        self.save_button = getIconButton(clickFunction=self.save_command,imagePath='images/save.png',framewidth=50)
        self.copy_button = getIconButton(clickFunction=self.copy_command,imagePath='images/copy.png',framewidth=50)
        self.clear_button = getIconButton(clickFunction=self.clear_command,imagePath='images/delete.png',framewidth=50)

    def createUI(self):
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        groupBox = QGroupBox('Command')
        self.layout.addWidget(groupBox)

        button_widget = QWidget()
        vbox_buttons = QVBoxLayout()
        button_widget.setLayout(vbox_buttons)

        vbox_buttons.addWidget(self.copy_button,0, Qt.AlignHCenter)
        vbox_buttons.addWidget(self.save_button,0, Qt.AlignHCenter)
        vbox_buttons.addWidget(self.clear_button,0, Qt.AlignHCenter)

        hbox_main = QHBoxLayout()
        hbox_main.addWidget(button_widget,stretch= 1,alignment=Qt.AlignVCenter)
        hbox_main.addWidget(self.output,stretch= 5,alignment=Qt.AlignVCenter)
        groupBox.setLayout(hbox_main)

        
