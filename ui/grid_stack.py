import os
import sys
import time
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from ui.common_helper import getIconButton,getLineEdit,getTableWidget,getTableWidgetItem

def separate_grid_name(grid_names:str)->list[str]:
    if(grid_names!=''):
        grid_name_split = grid_names.split(' ')
        grid_name_split_1 = []
        for x in grid_name_split:
            grid_name_split_1.extend(x.split(','))
        return grid_name_split_1
    return []

def separate_grid_value(grid_values:str)->list[str]:
    if(grid_values!=''):
        grid_val_split = grid_values.split(' ')
        grid_val_split_1 = []
        for x in grid_val_split:
            grid_val_split_1.extend(x.split(','))
        
        grid_vals = []
        for valX in grid_val_split_1:
            if(str(valX).find('*')>0):
                grid_valX_split = str(valX).split('*')
                rep = int(grid_valX_split[0].strip())
                valX = float(grid_valX_split[1].strip())
                for i in range(rep):
                    grid_vals.append(str(valX))
            else:
                grid_vals.append(str(valX))
        return grid_vals
    return []

class GridDataWidget(QWidget):

    grid_type : str
    add_button : QPushButton
    save_button : QPushButton
    delete_button : QPushButton
    sync_down_button : QPushButton
    sync_up_button : QPushButton
    input_type_row : QWidget
    sync_row : QWidget
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
        #self.show()

    @pyqtSlot()
    def add_button_command(self):
        data = self.count_editline.text()
        count = (0 if data == '' else int(data)) + 1
        self.count_editline.setText(str(count))
        self.refresh_view_down()
        return
    
    @pyqtSlot()
    def sync_down_command(self):
        self.refresh_view_down()
        return
    
    @pyqtSlot()
    def sync_up_command(self):
        self.refresh_view_up()
        return
    
    @pyqtSlot()
    def delete_button_command(self):
        self.grid_names.clear()
        self.grid_values.clear()
        self.count_editline.setText('0')
        self.refresh_view_down()
        return

    @pyqtSlot()
    def abs_coordinates_radio_command(self):
        return
    
    @pyqtSlot()
    def rel_coordinates_radio_command(self):
        return
    
    @pyqtSlot()
    def delete_click_command(self):
        button = self.sender()
        if button:
            data = self.count_editline.text()
            count = (0 if data == '' else int(data)) - 1
            self.count_editline.setText(str(count))
            row = self.grid_table.indexAt(button.pos()).row()
            self.grid_table.removeRow(row)

    def formTable(self):
        self.grid_table.setColumnCount(3)
        self.grid_table.setColumnWidth(0, 75)
        self.grid_table.setColumnWidth(1, 75)
        self.grid_table.setColumnWidth(2, 50)

        headerNames = []
        headerNames.append("Name")
        headerNames.append("Distance")
        headerNames.append("Delete")
        self.grid_table.setHorizontalHeaderLabels(headerNames)

    def refresh_view_down(self):
        self.grid_names = separate_grid_name(self.grid_names_editline.text())
        self.grid_values = separate_grid_value(self.grid_values_editline.text())
       
        row_count = self.grid_table.rowCount()
        reqd_count = int(self.count_editline.text())
        count = max(0,reqd_count-row_count)
        len_name = len(self.grid_names)
        len_val = len(self.grid_values)

        for i in range(count):
            index = row_count+i
            self.grid_table.insertRow(index)
            self.grid_table.setItem(index,0,getTableWidgetItem('A' if index>=len_name else self.grid_names[index]))
            self.grid_table.setItem(index,1,getTableWidgetItem('1000' if index>=len_val else self.grid_values[index]))
            deleteButton = getIconButton(self.delete_click_command,imagePath='images/delete.png',framewidth=50,frameHeight=30)
            #print('Added @ ' + str(index))
            self.grid_table.setCellWidget(index, 2, deleteButton)
        
        if(row_count>reqd_count):
            for i in reversed(range(reqd_count,row_count)):
                index = i
                #print('Removed @ ' + str(index))
                self.grid_table.removeRow(index)

        return

    def refresh_view_up(self):
        self.grid_names.clear()
        self.grid_values.clear()
        row_count = self.grid_table.rowCount()
        data = []
        for row in range(row_count):
            item_name :QTableWidgetItem = self.grid_table.item(row,0)
            item_val :QTableWidgetItem = self.grid_table.item(row,1)
            if item_name == None or item_val == None:
                continue
            else:
                self.grid_names.append(item_name.text())
                self.grid_values.append(float(item_val.text()))

        self.count_editline.setText(str(row_count))
        self.grid_names_editline.setText(" ".join(self.grid_names))
        grid_vals= map(lambda x :str(x),self.grid_values)
        self.grid_values_editline.setText(" ".join(grid_vals))

        return

    def initializeUI(self):
        self.setMinimumHeight(250)
        self.setMinimumWidth(200)
        self.input_type_row = QWidget()
        self.sync_row = QWidget()
        self.input_type_row.setMinimumWidth(175)
        self.sync_row.setMinimumWidth(175)
        self.count_editline = getLineEdit('Count',minWidth=175,maxWidth=400,fontSize=12)
        self.grid_names_editline = getLineEdit('Grid names',minWidth=175,maxWidth=400,fontSize=12)
        self.grid_values_editline = getLineEdit('Grid values (mm)',minWidth=175,maxWidth=400,fontSize=12)
        self.grid_table = getTableWidget(fontSize=12,minWidth=175,frameHeight=175,maxWidth=400)
        self.formTable()
        self.add_button = getIconButton(clickFunction=self.add_button_command,imagePath='images/add.png',framewidth=50,frameHeight=30)
        self.save_button = getIconButton(clickFunction=self.sync_up_command,imagePath='images/save.png',framewidth=50,frameHeight=30)
        self.delete_button = getIconButton(clickFunction=self.delete_button_command,imagePath='images/delete.png',framewidth=50,frameHeight=30)
        self.sync_up_button = getIconButton(clickFunction=self.sync_up_command,imagePath='images/up-arrow.png',framewidth=50,frameHeight=30)
        self.sync_down_button = getIconButton(clickFunction=self.sync_down_command,imagePath='images/down-arrow.png',framewidth=50,frameHeight=30)
        return

    def createUI(self):
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        groupBox = QGroupBox('Grid ' + self.grid_type)
        self.layout.addWidget(groupBox)
        vbox_main = QVBoxLayout()
        vbox_main.addWidget(self.input_type_row)
        hbox_input = QHBoxLayout()
        hbox_sync = QHBoxLayout()
        self.input_type_row.setLayout(hbox_input)
        self.sync_row.setLayout(hbox_sync)
        hbox_input.addWidget(self.add_button)
        hbox_input.addWidget(self.save_button)
        hbox_input.addWidget(self.delete_button)
        hbox_sync.addWidget(self.sync_down_button)
        hbox_sync.addWidget(self.sync_up_button)
        vbox_main.addWidget(self.count_editline)
        vbox_main.addWidget(self.grid_names_editline)
        vbox_main.addWidget(self.grid_values_editline)
        vbox_main.addWidget(self.sync_row)
        vbox_main.addWidget(self.grid_table)
        groupBox.setLayout(vbox_main)
        return

    def clearUI(self):
        self.grid_names.clear()
        self.grid_values.clear()
        self.count_editline.setText('0')
        self.grid_names_editline.setText('')
        self.grid_values_editline.setText('')
        self.refresh_view_down()
    
class GridStack(QWidget):

    x_grid_data : GridDataWidget
    y_grid_data : GridDataWidget
    z_grid_data : GridDataWidget

    def __init__(self):
        super().__init__()
        self.initializeUI()
        self.createUI()

    def initializeUI(self): 
        self.x_grid_data = GridDataWidget(grid_type='X')
        self.y_grid_data = GridDataWidget(grid_type='Y')
        self.z_grid_data = GridDataWidget(grid_type='Z')
        return
    
    def createUI(self):
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.x_grid_data)
        self.hbox.addWidget(self.y_grid_data)
        self.hbox.addWidget(self.z_grid_data)
        self.setLayout(self.hbox)
        return
    
    def clearUI(self):
        self.x_grid_data.clearUI()
        self.y_grid_data.clearUI()
        self.z_grid_data.clearUI()
        return

    def reference_up(self):
        self.x_grid_data.refresh_view_up()
        self.y_grid_data.refresh_view_up()
        self.z_grid_data.refresh_view_up()
        return

    def reference_down(self):
        self.x_grid_data.refresh_view_down()
        self.y_grid_data.refresh_view_down()
        self.z_grid_data.refresh_view_down()
        return


# Run program
"""
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GridWidget(grid_type='X')
    sys.exit(app.exec_())
"""