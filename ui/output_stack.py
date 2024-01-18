#import necessary modules 
from PyQt5.QtWidgets import (QWidget, QAction, QVBoxLayout,QHBoxLayout,QPushButton,QLineEdit,
    QMessageBox, QTextEdit, QFileDialog, QInputDialog, QFontDialog,QGroupBox,QGridLayout)
from PyQt5.QtCore import Qt
from ui.common_helper import getIconButton,getEditText

class OutputWidget(QWidget):

    output:QTextEdit

    def __init__(self):
        super().__init__()
        self.initializeUI()
        self.createUI()

    def initializeUI(self):
        self.setMinimumHeight(250)
        self.setMaximumHeight(350)
        self.output = getEditText('Output command',maxWidth=1000,minWidth=300,maxHeight=350)
        self.output.setReadOnly(True)
        return

    def createUI(self):
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        groupBox = QGroupBox('Command')
        self.layout.addWidget(groupBox)
        hbox_main = QHBoxLayout()
        hbox_main.addWidget(self.output,stretch= 5,alignment=Qt.AlignVCenter)
        groupBox.setLayout(hbox_main)
        return

    def clearUI(self):
        self.output.clear()
        return
        
