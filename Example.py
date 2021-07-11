import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
li = ["item1", "item2"]

from BlurWindow.blurWindow import blur



class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(500, 400)

        self.label = QLabel("Noting to see here")

        self.tab1 = QLabel("You can't see me")
        self.tab1.setAlignment(Qt.AlignCenter)
        self.tab2 = QLabel("Now you can")
        self.tab2.setAlignment(Qt.AlignCenter)
        self.tab3 = QLabel("Now you don't")
        self.tab3.setAlignment(Qt.AlignCenter)

        self.tabWidget = QTabWidget()
        self.tabWidget.addTab(self.tab1, "t1")
        self.tabWidget.addTab(self.tab2, "t2")
        self.tabWidget.addTab(self.tab3, "t2")
        self.tabWidget.setTabPosition(QTabWidget.West)

        
        
        self.tabWidget.setStyleSheet("QTabWidget{background: none;"
                                     "border:  0px;"
                                     "margin: 0px;"
                                     "padding: 0px;}"
                                     "QTabBar:tab{background: rgba(0, 200, 220, 20);}"
                                     "QTabBar:tab:hover{background: rgba(200, 200, 200, 120);}"
                                     "QTabBar:tab:selected{background: rgb(0, 150, 220);}")

        self.sw = QStackedWidget()
        self.sw.addWidget(self.label)

        

        self.sw.addWidget(self.tabWidget)


        if li is None:
            self.sw.setCurrentWidget(self.label)
            
            
            

        else:
            self.sw.setCurrentWidget(self.tabWidget)
            
        
        hWnd = self.winId()
        print(hWnd)
        blur(hWnd)

        self.toolBar = QToolBar()
        self.toolBar.setFixedHeight(30)
    

        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setMargin(0)
        self.layout.addWidget(self.toolBar)
        self.layout.addWidget(self.sw)
        self.setLayout(self.layout)
   

        self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())