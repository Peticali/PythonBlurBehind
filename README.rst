Installation
------------

You can install it with pip::

    python -m pip install BlurWindow


Preview:

.. image:: https://i.imgur.com/sBNxXQE.png
    :width: 400


Parameters:

.. code-block:: python

    #HWND = PID
    #Acrylic = True/False #For Acrylic Design (lags)
    #hexColor = Background color, False for nothing
    #Dark = White icons

    blur(HWND,hexColor=False,Acrylic=False,Dark=False)

    #in windows 7 or older: (scroll down for image)
    Win7Blur(HWND)



Example:

.. code-block:: python

    import sys
    from PySide2.QtWidgets import *
    from PySide2.QtCore import *

    from BlurWindow.blurWindow import blur


    class MainWindow(QWidget):
        def __init__(self):
            super(MainWindow, self).__init__()
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(500, 400)

            blur(self.winId(),Dark=True)

            self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")


    if __name__ == '__main__':
        app = QApplication(sys.argv)
        mw = MainWindow()
        mw.show()
        sys.exit(app.exec_())



Windows 7:

.. image:: https://i.imgur.com/ANA0gzF.png
    :width: 400