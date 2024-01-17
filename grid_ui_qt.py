import os
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,QPushButton,QHBoxLayout,QVBoxLayout,
                             QWidget,QMessageBox,QDockWidget,QStatusBar)
from PyQt5.QtGui import QIcon, QTextCursor, QColor
from PyQt5.QtCore import Qt
from ui.common_helper import getIconButton,getFont,getQIcon
from grid_base.grid import grid_data,getGridList
from grid_base.point import point
from grid_base.grid_base import build_macro
from misc.calc_time import calculate_time
from misc.clipboard import copy2clip
from misc.file_UI import saveFile_win_mac,readLineByLine
from ui.reference_stack import ReferenceWidget
from ui.output_stack import OutputWidget
from ui.grid_stack import GridStack

saveLoc = os.getenv('LOCALAPPDATA') + r"\GridPy"
saveFile = saveLoc+ r"\db.dat"

#Create local app data folder for UI data save
if(not os.path.isdir(saveLoc)):
    os.mkdir(saveLoc)

class GridGenerator(QMainWindow):

    reference_widget : ReferenceWidget
    output_widget : OutputWidget
    grid_widget : GridStack

    def __init__(self):
        super().__init__()
        self.initializeUI()
        self.defineDock()

    def initializeUI(self):
        #self.setGeometry(100, 100, 1000, 800)
        self.setWindowIcon(getQIcon('images/grid.png'))
        self.setMinimumHeight(875)
        self.setWindowTitle('Grid Generator 2.0')
        mainWidget = QWidget()
        mainDataStack = QVBoxLayout()

        self.reference_widget = ReferenceWidget()
        self.output_widget = OutputWidget()
        self.grid_widget = GridStack()

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
        self.file_buttons.setMaximumHeight(250)
        self.dock.setMaximumWidth(60)
        self.new_button = getIconButton(clickFunction=None,imagePath='images/new.png',framewidth=50)
        self.open_button = getIconButton(clickFunction=None,imagePath='images/open.png',framewidth=50)
        self.save_button = getIconButton(clickFunction=None,imagePath='images/save.png',framewidth=50)
        self.create_button = getIconButton(clickFunction=None,imagePath='images/create.png',framewidth=50)
        vbox.addWidget(self.new_button)
        vbox.addWidget(self.open_button)
        vbox.addWidget(self.save_button)
        vbox.addWidget(self.create_button)
        self.file_buttons.setLayout(vbox)
        self.dock.setWidget(self.file_buttons)

# Run program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GridGenerator()
    sys.exit(app.exec_())