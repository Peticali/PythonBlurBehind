from tkinter import *
from BlurWindow.blurWindow import GlobalBlur
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from threading import Thread

class BlurBG(QWidget):
    def __init__(self):
        super(BlurBG, self).__init__()
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.resize(500, 400)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")

def configure(e:Event):
    janela.tkraise()
    mw.move(e.x,e.y)
    mw.resize(janela.winfo_width(),janela.winfo_height())
    
def showTk(e):
    mw.show()
    janela.tkraise()

janela = Tk()
janela.configure(bg='SystemTransparent')
janela.attributes("-transparent", True)
janela.geometry('200x200')

app = QApplication(sys.argv)
mw = BlurBG()
mw.show()
GlobalBlur(QWidget=mw,HWND=mw.winId())
app.processEvents()

janela.bind('<Configure>',configure)
janela.bind('<Unmap>', lambda e: mw.hide())
janela.bind('<Map>', showTk)


janela.mainloop()




