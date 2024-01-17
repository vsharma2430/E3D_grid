#import necessary modules 
from PyQt5.QtWidgets import (QWidget, QAction, QVBoxLayout,QHBoxLayout,QPushButton,QLineEdit,
    QMessageBox, QTextEdit, QFileDialog, QInputDialog, QFontDialog,QGroupBox,QGridLayout,QSpinBox)
from PyQt5.QtGui import QTextCursor, QColor
from PyQt5.QtCore import Qt
from ui.common_helper import getIconButton,getLabel,getEditText,getLineEdit,getComboBox

class ReferenceWidget(QWidget):

    old_new_grid:QSpinBox
    reference_name:QLineEdit
    reference_X:QLineEdit
    reference_Y:QLineEdit
    reference_Z:QLineEdit

    def __init__(self):
        super().__init__()
        self.initializeUI()
        self.createUI()
    
    def initializeUI(self):
        self.setMinimumHeight(50)
        self.setMaximumHeight(100)

        self.reference_name = getLineEdit(hintText='Grid name')
        self.reference_X = getLineEdit(hintText='X(mm)')
        self.reference_Y = getLineEdit(hintText='Y(mm)')
        self.reference_Z = getLineEdit(hintText='Z(mm)')
        self.old_new_grid = getComboBox(['New','Old'],frameHeight=30)

    def createUI(self):
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        groupBox = QGroupBox('Reference Point')
        self.layout.addWidget(groupBox)

        hbox = QHBoxLayout()
        groupBox.setLayout(hbox)
        hbox.addWidget(self.old_new_grid)
        hbox.addWidget(self.reference_name)
        hbox.addWidget(self.reference_X)
        hbox.addWidget(self.reference_Y)
        hbox.addWidget(self.reference_Z)