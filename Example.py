import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from BlurWindow.blurWindow import blur



class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(500, 400)

        hWnd = self.winId()
        print(hWnd)
        blur(hWnd)

        self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
