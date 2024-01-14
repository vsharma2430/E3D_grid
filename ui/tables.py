from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget       

class gridWidget(QtWidgets.QWidget):
        def __init__(self, parent: QWidget) -> QWidget:
                super().__init__(parent)
                

        def initialize_widget(self):
                return



"""
headerH = ['Name' , 'Distance']
        self.tableWidget_X = QtWidgets.QTableWidget(self.widget_5)
        self.tableWidget_X.setObjectName("tableWidget_X")
        self.tableWidget_X.setColumnCount(2)
        self.tableWidget_X.setRowCount(2)
        self.horizontalLayout_2.addWidget(self.tableWidget_X)
        self.tableWidget_Y = QtWidgets.QTableWidget(self.widget_5)
        self.tableWidget_Y.setObjectName("tableWidget_Y")
        self.tableWidget_Y.setColumnCount(2)
        self.tableWidget_Y.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.tableWidget_Y)
        self.tableWidget_Z = QtWidgets.QTableWidget(self.widget_5)
        self.tableWidget_Z.setObjectName("tableWidget_Z")
        self.tableWidget_Z.setColumnCount(2)
        self.tableWidget_Z.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.tableWidget_Z)
        self.tableWidget_X.setHorizontalHeaderLabels(headerH)
        self.tableWidget_Y.setHorizontalHeaderLabels(headerH)
        self.tableWidget_Z.setHorizontalHeaderLabels(headerH)
        self.tableWidget_X.setItem(0 , 0 , QtWidgets.QTableWidgetItem('1'))
        self.tableWidget_X.setItem(1 , 0 , QtWidgets.QTableWidgetItem('2'))
"""
