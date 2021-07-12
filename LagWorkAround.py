#WorkAround source: https://github.com/negated-py/qtacrylic (lol i didn't know that exist a project that did the same as mine)

import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import time
from BlurWindow.blurWindow import blur



class MainWindow(QWidget):
    def moveEvent(self, event) -> None:#here
        time.sleep(0.02)  

    def resizeEvent(self, event) -> None:#here
        time.sleep(0.02) 
        
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(500, 400)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    blur(mw.winId(),Acrylic=True)
    sys.exit(app.exec_())
