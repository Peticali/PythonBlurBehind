#source: https://github.com/Opticos/GWSL-Source/blob/master/blur.py , https://www.cnblogs.com/zhiyiYo/p/14659981.html , https://github.com/ifwe/digsby/blob/master/digsby/src/gui/vista.py

from ctypes.wintypes import  DWORD, BOOL, HRGN
import ctypes

user32 = ctypes.windll.user32
dwm = ctypes.windll.dwmapi

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


class DWM_BLURBEHIND(ctypes.Structure):
    _fields_ = [
        ('dwFlags', DWORD), 
        ('fEnable', BOOL),  
        ('hRgnBlur', HRGN), 
        ('fTransitionOnMaximized', BOOL) 
    ]


class MARGINS(ctypes.Structure):
    _fields_ = [("cxLeftWidth", ctypes.c_int),
                ("cxRightWidth", ctypes.c_int),
                ("cyTopHeight", ctypes.c_int),
                ("cyBottomHeight", ctypes.c_int)
                ]


def Win7Blur(HWND):
    DWM_BB_ENABLE = 0x01
    bb = DWM_BLURBEHIND()
    bb.dwFlags = DWM_BB_ENABLE
    bb.fEnable = 1
    bb.hRgnBlur = 1
    dwm.DwmEnableBlurBehindWindow(HWND, ctypes.byref(bb))


def ExtendFrameIntoClientArea(HWND):
    margins = MARGINS(0, 0, 0, 0)
    dwm.DwmExtendFrameIntoClientArea(HWND, ctypes.byref(margins))


def HEXtoRGBAint(HEX:str):
    alpha = HEX[7:]
    blue = HEX[5:7]
    green = HEX[3:5]
    red = HEX[1:3]

    gradientColor = alpha + blue + green + red
    return int(gradientColor, base=16)


def blur(HWND,hexColor=False,Acrylic=False,Dark=False):
    accent = ACCENTPOLICY()
    accent.AccentState = 3 #Default window Blur #ACCENT_ENABLE_BLURBEHIND

    gradientColor = 0
    
    if hexColor != False:
        gradientColor = HEXtoRGBAint(hexColor)
        accent.AccentFlags = 2 #Window Blur With Accent Color #ACCENT_ENABLE_TRANSPARENTGRADIENT
    
    if Acrylic:
        accent.AccentState = 4 #UWP but LAG #ACCENT_ENABLE_ACRYLICBLURBEHIND
        if hexColor == False: #UWP without color is translucent
            gradientColor = HEXtoRGBAint('#12121240') #placeholder color
    
    accent.GradientColor = gradientColor
    
    data = WINDOWCOMPOSITIONATTRIBDATA()
    data.Attribute = 19 #WCA_ACCENT_POLICY
    data.SizeOfData = ctypes.sizeof(accent)
    data.Data = ctypes.cast(ctypes.pointer(accent), ctypes.POINTER(ctypes.c_int))
    
    user32.SetWindowCompositionAttribute(HWND, data)
    
    if Dark: 
        data.Attribute = 26 #WCA_USEDARKMODECOLORS
        user32.SetWindowCompositionAttribute(HWND, data)

def GlobalBlur(HWND,hexColor=False,Acrylic=False,Dark=False):
    import platform
    release = platform.release()
    
    if release == 'Vista': 
        Win7Blur(HWND)
    else:
        release = int(float(release))
        if release == 10 or release == 8 or release == 11: #idk what windows 8.1 spits, if is '8.1' int(float(release)) will work...
            blur(HWND,hexColor,Acrylic,Dark)
        else:
            Win7Blur(HWND)

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
            GlobalBlur(hWnd,Dark=True)

            self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")

    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()

    #blur(mw.winId())
    #ExtendFrameIntoClientArea(mw.winId())

    sys.exit(app.exec_())

