#https://github.com/negated-py/qtacrylic idea
import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import time
from BlurWindow.blurWindow import GlobalBlur



class MainWindow(QWidget):
    def moveEvent(self, event) -> None:
        time.sleep(0.02)  # sleep for 20ms

    def resizeEvent(self, event) -> None:
        time.sleep(0.02)  # sleep for 20ms
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(500, 400)

        GlobalBlur(self.winId(),Dark=True,Acrylic=True)

        self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())