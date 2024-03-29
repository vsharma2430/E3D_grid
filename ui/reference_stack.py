#import necessary modules 
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,QLineEdit,QGroupBox,QGridLayout,QSpinBox)
from ui.common_helper import getLineEdit,getComboBox

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
        return
    
    def initializeUI(self):
        self.setMinimumHeight(50)
        self.setMaximumHeight(100)

        self.reference_name = getLineEdit(hintText='Grid name')
        self.reference_X = getLineEdit(hintText='X(mm)')
        self.reference_Y = getLineEdit(hintText='Y(mm)')
        self.reference_Z = getLineEdit(hintText='Z(mm)')
        self.old_new_grid = getComboBox(['New','Old'],frameHeight=30)
        return

    def createUI(self):
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        groupBox = QGroupBox('Reference')
        self.layout.addWidget(groupBox)

        hbox = QHBoxLayout()
        groupBox.setLayout(hbox)
        hbox.addWidget(self.old_new_grid)
        hbox.addWidget(self.reference_name)
        hbox.addWidget(self.reference_X)
        hbox.addWidget(self.reference_Y)
        hbox.addWidget(self.reference_Z)
        return

    def clearUI(self):
        self.reference_name.clear()
        self.reference_X.clear()
        self.reference_Y.clear()
        self.reference_Z.clear()