Installation
------------

You can install it with pip::

    python -m pip install BlurWindow


Preview:

.. image:: https://i.imgur.com/sBNxXQE.png
    :width: 400


Parameters/Functions:

.. code-block:: python

    #HWND = PID
    #Acrylic = True/False #For Acrylic Design (lag WorkAround https://github.com/Peticali/PythonBlurBehind/blob/main/Examples%20MUST%20SEE/LagWorkAround.py)
    #hexColor = Background color, False for nothing
    #Dark = White icons
    #QWidget = Your parent (for Mac)
    #Material = https://developer.apple.com/documentation/appkit/nsvisualeffectmaterial

    blur(HWND,hexColor=False,Acrylic=False,Dark=False)

    #in windows 7 or older: (scroll down for image Acrylic True/False)
    Win7Blur(HWND,Acrylic)
    
    #in Linux (may not work for all distros, scroll down for image)
    BlurLinux(HWND)
    
    #in Mac (WIP):
    MacBlur(QWidget,Material)

    #NEW, Blur Windows Vista, 7, 8, 8.1, 10, 11, Linux, MacOS Auto
    GlobalBlur(HWND,hexColor=False,Acrylic=False,Dark=False,QWidget=QWidget)


Example:

.. code-block:: python

    import sys
    from PySide2.QtWidgets import *
    from PySide2.QtCore import *

    from BlurWindow.blurWindow import GlobalBlur


    class MainWindow(QWidget):
        def __init__(self):
            super(MainWindow, self).__init__()
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(500, 400)

            GlobalBlur(self.winId(),Dark=True,QWidget=self)

            self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")


    if __name__ == '__main__':
        app = QApplication(sys.argv)
        mw = MainWindow()
        mw.show()
        sys.exit(app.exec_())



Windows 7/Vista:

.. image:: https://i.imgur.com/CgFlbwt.png
    :width: 400
    
Linux (Deepin):

.. image:: https://i.imgur.com/h4TCByr.png
    :width: 400

MacOS (BigSur):

.. image:: https://i.imgur.com/qVSZnIw.png
    :width: 400
    