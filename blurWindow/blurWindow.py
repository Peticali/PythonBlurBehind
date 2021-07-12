#source: https://github.com/Opticos/GWSL-Source/blob/master/blur.py , https://www.cnblogs.com/zhiyiYo/p/14659981.html

import ctypes
user32 = ctypes.windll.user32


class ACCENTPOLICY(ctypes.Structure):
    _fields_ = [
        ("AccentState", ctypes.c_uint),
        ("AccentFlags", ctypes.c_uint),
        ("GradientColor", ctypes.c_uint),
        ("AnimationId", ctypes.c_uint)
    ]


class WINDOWCOMPOSITIONATTRIBDATA(ctypes.Structure):
    _fields_ = [
        ("Attribute", ctypes.c_int),
        ("Data", ctypes.POINTER(ctypes.c_int)),
        ("SizeOfData", ctypes.c_size_t)
    ]



def HEXtoRGBAint(HEX:str):
    alpha = HEX[7:]
    blue = HEX[5:7]
    green = HEX[3:5]
    red = HEX[1:3]

    gradientColor = alpha + blue + green + red
    return int(gradientColor, base=16)



def blur(HWND,hexColor=False,Acrylic=False):
    accent = ACCENTPOLICY()
    accent.AccentState = 3 #Default window Blur

    gradientColor = 0
    
    if hexColor != False:
        gradientColor = HEXtoRGBAint(hexColor)
        accent.AccentFlags = 2 #Window Blur With Accent Color
    
    if Acrylic:
        accent.AccentState = 4 #UWP but LAG
        if hexColor == False: #UWP without color is translucent
            gradientColor = HEXtoRGBAint('#12121240') #placeholder color
        
        
    accent.GradientColor = gradientColor
    
    data = WINDOWCOMPOSITIONATTRIBDATA()
    data.Attribute = 19 #WCA_ACCENT_POLICY
    data.SizeOfData = ctypes.sizeof(accent)
    data.Data = ctypes.cast(ctypes.pointer(accent), ctypes.POINTER(ctypes.c_int))
    
    user32.SetWindowCompositionAttribute(HWND, data)
    
    
    
if __name__ == '__main__':
    import sys
    from PySide2.QtWidgets import *
    from PySide2.QtCore import *

    class MainWindow(QWidget):
        def __init__(self):
            super(MainWindow, self).__init__()
            #self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(500, 400)

            hWnd = self.winId()
            #print(hWnd)
            #blur(hWnd)

            self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")



    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()

    blur(mw.winId())

    sys.exit(app.exec_())

