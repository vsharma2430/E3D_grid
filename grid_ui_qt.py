import os
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,QPushButton,QHBoxLayout,QVBoxLayout,
                             QWidget,QMessageBox,QDockWidget,QStatusBar)
from PyQt5.QtGui import QIcon, QTextCursor, QColor
from PyQt5.QtCore import Qt
from ui.common_helper import getHSeparator,getIconButton,getFont
from grid_base.grid import grid_data,getGridList
from grid_base.point import point
from grid_base.grid_base import build_macro
from misc.calc_time import calculate_time
from misc.clipboard import copy2clip
from misc.file_UI import saveFile_win_mac,readLineByLine
from ui.reference_stack import ReferenceWidget
from ui.output_stack import OutputWidget

saveLoc = os.getenv('LOCALAPPDATA') + r"\GridPy"
saveFile = saveLoc+ r"\db.dat"

#Create local app data folder for UI data save
if(not os.path.isdir(saveLoc)):
    os.mkdir(saveLoc)

class GridGenerator(QMainWindow):

    reference_widget : ReferenceWidget

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 1000, 800)
        self.setWindowTitle('Grid Generator 2.0')
        mainWidget = QWidget()
        mainDataStack = QVBoxLayout()

        self.reference_widget = ReferenceWidget()
        self.output_widget = OutputWidget()

        mainDataStack.addWidget(self.reference_widget)
        mainDataStack.addWidget(self.output_widget)

        mainWidget.setLayout(mainDataStack)
        self.setCentralWidget(mainWidget)

        self.statusBar:QStatusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.setFont(getFont(12))
        self.statusBar.showMessage('Grid Generator')
        self.show()

# Run program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GridGenerator()
    sys.exit(app.exec_())