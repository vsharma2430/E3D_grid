import os
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,QVBoxLayout,
                             QWidget,QMessageBox,QDockWidget,QStatusBar)
from PyQt5.QtCore import Qt,pyqtSlot
from PyQt5.QtGui import QClipboard
from ui.common_helper import getIconButton,getFont,getQIcon,getFloat,getHSeparator
from grid_base.grid import grid_data,getGridList
from grid_base.point import point
from grid_base.grid_base import build_macro
from misc.file_UI import saveFile_win_mac,selectFile,readLineByLine
from ui.reference_stack import ReferenceWidget
from ui.output_stack import OutputWidget
from ui.grid_stack import GridStack

save_directory = os.getenv('LOCALAPPDATA') + r"\GridPy"
save_file_location = save_directory+ r"\db.dat"

#Create local app data folder for UI data save
if(not os.path.isdir(save_directory)):
    os.mkdir(save_directory)

class GridGenerator(QMainWindow):

    clipboard : QClipboard 
    reference_widget : ReferenceWidget
    output_widget : OutputWidget
    grid_widget : GridStack

    def __init__(self,clipB:QClipboard):
        super().__init__()
        self.clipboard = clipB
        self.initializeUI()
        self.defineDock()

    def closeEvent(self, event):
        self.saveFile()
        reply = QMessageBox.question(self, 'Quit?',
                                     'Are you sure you want to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            if not type(event) == bool:
                event.accept()
            else:
                sys.exit()
        else:
            if not type(event) == bool:
                event.ignore()
 
    def saveFile(self,file_location:str=save_file_location):
        self.grid_widget.reference_up()
        save_data = []
        grid_ref_name = self.reference_widget.reference_name.text()
        grid_refX = self.reference_widget.reference_X.text()
        grid_refY =  self.reference_widget.reference_Y.text()
        grid_refZ = self.reference_widget.reference_Z.text()
        gridXName = self.grid_widget.x_grid_data.grid_names_editline.text()
        gridXVal = self.grid_widget.x_grid_data.grid_values_editline.text()
        gridYName = self.grid_widget.y_grid_data.grid_names_editline.text()
        gridYVal = self.grid_widget.y_grid_data.grid_values_editline.text()
        gridZName = self.grid_widget.z_grid_data.grid_names_editline.text()
        gridZVal = self.grid_widget.z_grid_data.grid_values_editline.text()
        save_data.append(grid_ref_name)
        save_data.append(grid_refX)
        save_data.append(grid_refY)
        save_data.append(grid_refZ)
        save_data.append(gridXName)
        save_data.append(gridXVal)
        save_data.append(gridYName)
        save_data.append(gridYVal)
        save_data.append(gridZName)
        save_data.append(gridZVal)

        print("Saving last input")
        f = open(file_location,'w')
        f.write('\n'.join(save_data))
        f.close()
        
        self.statusBar.showMessage('File saved : ' + file_location)
        return
    
    def loadFile(self,file_location:str=save_file_location):
        data = readLineByLine(fileLocation=file_location)
        if(len(data)>9):
            self.reference_widget.reference_name.setText(data[0])
            self.reference_widget.reference_X.setText(data[1])
            self.reference_widget.reference_Y.setText(data[2])
            self.reference_widget.reference_Z.setText(data[3])
            self.grid_widget.x_grid_data.grid_names_editline.setText(data[4])
            self.grid_widget.x_grid_data.grid_values_editline.setText(data[5])
            self.grid_widget.y_grid_data.grid_names_editline.setText(data[6])
            self.grid_widget.y_grid_data.grid_values_editline.setText(data[7])
            self.grid_widget.z_grid_data.grid_names_editline.setText(data[8])
            self.grid_widget.z_grid_data.grid_values_editline.setText(data[9])

            x_grid : list[grid_data] = getGridList(grid_names=self.grid_widget.x_grid_data.grid_names_editline.text(),grid_values=self.grid_widget.x_grid_data.grid_values_editline.text(),dir=1)
            y_grid : list[grid_data] = getGridList(grid_names=self.grid_widget.y_grid_data.grid_names_editline.text(),grid_values=self.grid_widget.y_grid_data.grid_values_editline.text(),dir=2)
            z_grid : list[grid_data] = getGridList(grid_names=self.grid_widget.z_grid_data.grid_names_editline.text(),grid_values=self.grid_widget.z_grid_data.grid_values_editline.text(),dir=3)

            self.grid_widget.x_grid_data.count_editline.setText(str(len(x_grid)))
            self.grid_widget.y_grid_data.count_editline.setText(str(len(y_grid)))
            self.grid_widget.z_grid_data.count_editline.setText(str(len(z_grid)))

            self.grid_widget.reference_down()
            self.statusBar.showMessage('File loaded : ' + file_location)
        return

    @pyqtSlot()
    def saveUI_command(self):
        save_file_path = saveFile_win_mac()
        self.saveFile(file_location=save_file_path)
        self.statusBar.showMessage('File saved : ' + save_file_path)
        return
    
    @pyqtSlot()
    def loadUI_command(self):
        load_file_path = selectFile()
        self.loadFile(file_location=load_file_path)
        self.statusBar.showMessage('File loaded : ' + load_file_path)
        return

    @pyqtSlot()
    def new_button_command(self):
        self.grid_widget.clearUI()
        self.reference_widget.clearUI()
        self.output_widget.clearUI()
        return

    def getRefGridData(self)->grid_data:
        return grid_data(label='/'+self.reference_widget.reference_name.text(),
                                         delta=point(x=getFloat(self.reference_widget.reference_X.text()),
                                                     y=getFloat(self.reference_widget.reference_Y.text()),
                                                     z=getFloat(self.reference_widget.reference_Z.text())
                                                     ))

    @pyqtSlot()
    def generate_button_command(self):
        self.grid_widget.reference_up()
        ref_grid : grid_data = self.getRefGridData()
        x_grid : list[grid_data] = getGridList(grid_names=self.grid_widget.x_grid_data.grid_names_editline.text(),grid_values=self.grid_widget.x_grid_data.grid_values_editline.text(),dir=1)
        y_grid : list[grid_data] = getGridList(grid_names=self.grid_widget.y_grid_data.grid_names_editline.text(),grid_values=self.grid_widget.y_grid_data.grid_values_editline.text(),dir=2)
        z_grid : list[grid_data] = getGridList(grid_names=self.grid_widget.z_grid_data.grid_names_editline.text(),grid_values=self.grid_widget.z_grid_data.grid_values_editline.text(),dir=3)
        new_old : bool = True if self.reference_widget.old_new_grid.currentIndex() == 0 else False
        pml_command : str = build_macro(ref_grid=ref_grid,x_grid=x_grid,y_grid=y_grid,z_grid=z_grid,new_old=new_old)
        self.output_widget.output.setText(pml_command)
        clipboard.setText(pml_command)
        self.statusBar.showMessage('Grid generated and macro copied to clipboard')
        return
    
    @pyqtSlot()
    def copy_button_command(self):
        clipboard.setText(self.output_widget.output.toPlainText())
        self.statusBar.showMessage('Macro copied to clipboard')
        return

    def initializeUI(self):
        #self.setGeometry(100, 100, 1000, 800)
        self.setWindowIcon(getQIcon('images/grid.png'))
        self.setMinimumHeight(890)
        self.setWindowTitle('Grid Generator 2.0')
        mainWidget = QWidget()
        mainDataStack = QVBoxLayout()

        self.reference_widget = ReferenceWidget()
        self.output_widget = OutputWidget()
        self.grid_widget = GridStack(self)

        mainDataStack.addWidget(self.reference_widget)
        mainDataStack.addWidget(self.grid_widget)
        mainDataStack.addWidget(self.output_widget)

        mainWidget.setLayout(mainDataStack)
        self.setCentralWidget(mainWidget)

        self.statusBar:QStatusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.setFont(getFont(12))
        self.statusBar.showMessage('Grid Generator')
        self.show()

    def defineDock(self):
        self.dock = QDockWidget()
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock)

        self.file_buttons = QWidget()
        vbox = QVBoxLayout()
        self.file_buttons.setMaximumHeight(350)
        self.dock.setMaximumWidth(60)
        self.new_button = getIconButton(clickFunction=self.new_button_command,imagePath='images/new.png',framewidth=50)
        self.open_button = getIconButton(clickFunction=self.loadUI_command,imagePath='images/import.png',framewidth=50)
        self.save_button = getIconButton(self.saveUI_command,imagePath='images/save.png',framewidth=50)
        self.create_button = getIconButton(clickFunction=self.generate_button_command,imagePath='images/create.png',framewidth=50)
        self.copy_button = getIconButton(clickFunction=self.copy_button_command,imagePath='images/copy.png',framewidth=50)
        self.eil_button = getIconButton(imagePath='images/logo.png',framewidth=50)
        vbox.addWidget(self.new_button)
        vbox.addWidget(self.open_button)
        vbox.addWidget(self.save_button)
        vbox.addWidget(getHSeparator())
        vbox.addWidget(self.create_button)
        vbox.addWidget(self.copy_button)
        vbox.addWidget(getHSeparator())
        vbox.addWidget(self.eil_button)
        self.file_buttons.setLayout(vbox)
        self.dock.setWidget(self.file_buttons)
    
# Run program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    clipboard = app.clipboard()
    window = GridGenerator(clipboard)
    window.setFont(getFont(fontSize=11))
    window.loadFile(save_file_location)
    sys.exit(app.exec_())