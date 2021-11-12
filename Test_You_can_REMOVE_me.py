# importing libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QBasicTimer, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import numpy as np
import random
import time
import sys
class Window1(QtWidgets.QMainWindow):
    def __init__(self, window2=None, window3=None):
        super(Window1, self).__init__()
        #setting title
        self.setWindowTitle('tailor-made Personal Color 앱')
        # setting geometry
        self.resize(569, 416)
        self.center()
    # setting Combobox
        Combo1 = QComboBox(self)
        Combo1.addItem('Defualt')
        Combo1.addItem('Daily')
        Combo1.addItem('Dress')
        Combo1.addItem('Suit')
        Combo1.resize(110,30)
        Combo1.move(440,250)
        Combo1.activated[str].connect(self.onActivated)
        global labelDe
        global pixmap
        labelDe = QLabel(self)
        labelDe.resize(171, 291)
        labelDe.move(30,30)
        pixmap = QPixmap('./combobox/daily/da ('+str(1)+').jpeg')
        labelDe.setPixmap(pixmap)
        print('Defualt 눌렸음')
        self.show()
    def onActivated(self, text):
        global pixmap
        global labelDe
        if text == 'Daily':
            pixmap.load('./combobox/daily/da ('+str(2)+').jpeg')
            labelDe.setPixmap(pixmap)
            print('Daily 눌렸음')
        elif text == 'Dress':
            pixmap.load('./combobox/daily/da ('+str(3)+').jpeg')
            labelDe.setPixmap(pixmap)
            print('Dress 눌렸음')
        elif text == 'Suit':
            pixmap.load('./combobox/daily/da ('+str(4)+').jpeg')
            labelDe.setPixmap(pixmap)
            print('Suit 눌렸음')
        elif text == 'Defualt':
            pixmap.load('./combobox/daily/da ('+str(1)+').jpeg')
            labelDe.setPixmap(pixmap)
        self.show()
    def center(self):
        #centers the window on the screen
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())//2,
            (screen.height()-size.height())//2)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window1()
    window.show()
    sys.exit(app.exec_())
