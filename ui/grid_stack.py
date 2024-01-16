import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from common_helper import getIconButton,getLineEdit,getTableWidget,getTableWidgetItem

class GridWidget(QWidget):

    grid_type : str
    add_button : QPushButton
    refresh_button : QPushButton
    delete_button : QPushButton
    input_type_row : QWidget
    count_editline : QLineEdit
    absolute_coordinates_radio : QRadioButton
    relative_coordinates_radio : QRadioButton
    grid_names_editline : QLineEdit
    grid_values_editline : QLineEdit
    grid_table : QTableWidget

    grid_names : list[str] = []
    grid_values : list[float] = []
        
    def __init__(self,grid_type:str):
        super().__init__()
        self.grid_type = grid_type
        self.initializeUI()
        self.createUI()
        self.show()

    def add_button_command(self):
        data = self.count_editline.text()
        count = (0 if data == '' else int(data)) + 1
        self.count_editline.setText(str(count))
        self.refresh_view()
        return
    
    def refresh_button_command(self):
        self.refresh_view()

        return
    def delete_button_command(self):
        return
    def abs_coordinates_radio_command(self):
        return
    def rel_coordinates_radio_command(self):
        return
    def formTable(self):
        self.grid_table.setColumnCount(3)
        self.grid_table.setColumnWidth(0, 75)
        self.grid_table.setColumnWidth(1, 75)
        self.grid_table.setColumnWidth(2, 30)

    @pyqtSlot()
    def deleteClicked(self):
        button = self.sender()
        if button:
            data = self.count_editline.text()
            count = (0 if data == '' else int(data)) - 1
            self.count_editline.setText(str(count))
            row = self.grid_table.indexAt(button.pos()).row()
            self.grid_table.removeRow(row)

    def refresh_view(self):
        row_count = self.grid_table.rowCount()
        reqd_count = int(self.count_editline.text())
        count = max(0,reqd_count-row_count)
        len_name = len(self.grid_names)
        len_val = len(self.grid_values)
        for i in range(count):
            index = row_count+i
            self.grid_table.insertRow(index)
            self.grid_table.setItem(index,0,getTableWidgetItem('A' if i>=len_name else self.grid_names[index]))
            self.grid_table.setItem(index,1,getTableWidgetItem('1000' if i>=len_val else self.grid_values[index]))
            deleteButton = getIconButton(self.deleteClicked,imagePath='images/delete.png',framewidth=30,frameHeight=30)
            self.grid_table.setCellWidget(index, 2, deleteButton)
        

    def initializeUI(self):
        self.setMinimumHeight(400)
        self.setMinimumWidth(200)
        self.input_type_row = QWidget()
        self.input_type_row.setMinimumWidth(175)
        self.count_editline = getLineEdit('Count',minWidth=175,maxWidth=400,fontSize=12)
        self.grid_names_editline = getLineEdit('Grid names',minWidth=175,maxWidth=400,fontSize=12)
        self.grid_values_editline = getLineEdit('Grid values (mm)',minWidth=175,maxWidth=400,fontSize=12)
        self.grid_table = getTableWidget(fontSize=12,minWidth=175,frameHeight=275,maxWidth=400)
        self.formTable()
        self.add_button = getIconButton(clickFunction=self.add_button_command,imagePath='images/add.png',framewidth=30,frameHeight=30)
        self.refresh_button = getIconButton(clickFunction=self.refresh_button_command,imagePath='images/refresh.png',framewidth=30,frameHeight=30)
        self.delete_button = getIconButton(clickFunction=self.delete_button_command,imagePath='images/delete.png',framewidth=30,frameHeight=30)
        return

    def createUI(self):
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        groupBox = QGroupBox('Grid ' + self.grid_type)
        self.layout.addWidget(groupBox)
        vbox_main = QVBoxLayout()
        vbox_main.addWidget(self.input_type_row)
        hbox_input = QHBoxLayout()
        self.input_type_row.setLayout(hbox_input)
        hbox_input.addWidget(self.add_button)
        hbox_input.addWidget(self.refresh_button)
        hbox_input.addWidget(self.delete_button)
        vbox_main.addWidget(self.count_editline)
        vbox_main.addWidget(self.grid_names_editline)
        vbox_main.addWidget(self.grid_values_editline)
        vbox_main.addWidget(self.grid_table)
        groupBox.setLayout(vbox_main)
        return

# Run program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GridWidget(grid_type='X')
    sys.exit(app.exec_())