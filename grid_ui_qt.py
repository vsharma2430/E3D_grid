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

saveLoc = os.getenv('LOCALAPPDATA') + r"\GridPy"
saveFile = saveLoc+ r"\db.dat"

#Create local app data folder for UI data save
if(not os.path.isdir(saveLoc)):
    os.mkdir(saveLoc)

class GridGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 1000, 800)
        self.setWindowTitle('Grid Generator 2.0')
        mainWidget = QWidget()
        mainDataStack = QVBoxLayout()

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