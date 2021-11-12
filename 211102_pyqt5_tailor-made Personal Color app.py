# importing libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QBasicTimer, pyqtSignal
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import sys



class Window1(QtWidgets.QMainWindow):
    def __init__(self, window2=None, window3=None):
        super(Window1, self).__init__()
        #setting title
        self.setWindowTitle('tailor-made Personal Color 앱')
        # setting geometry
        self.resize(450, 675)
        self.center()

        # setting geometry
        self.setGeometry(650, 250, 450, 675)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("main-widget")
        # Label Create
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 450, 675))
        self.label.setMinimumSize(QtCore.QSize(450, 675))
        self.label.setMaximumSize(QtCore.QSize(450, 675))
        self.label.setObjectName("lb1")
        self.setCentralWidget(self.centralwidget)

        # Loading the GIF
        self.movie = QMovie('tailer_made_Personal_color.gif')
        self.label.setMovie(self.movie)
        
        # calling method
        self.startAnimation()

        # setting start btn
        self.button = QtWidgets.QPushButton('', self)
        self.button.setGeometry(250,300,200,56)
        self.button.setStyleSheet("border-width: 0px; border-style: solid;background-image : url(start_btn.png);")
        self.button.clicked.connect(self.handleButton)
  
        # showing all the widgets
        self.show() 

        
        self._window2 = window2
    # Start Animation
    def startAnimation(self):
        self.movie.start()
  
    # Stop Animation(According to need)
    def stopAnimation(self):
        self.movie.stop()

    def handleButton(self):
        self.hide()
        if self._window2 is None:
            self._window2 = Window2(self)
        self._window2.show()

    def center(self):
        #centers the window on the screen
        
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())//2, 
            (screen.height()-size.height())//2)

class Window2(QtWidgets.QMainWindow):
    def __init__(self, window1=None, window3=None, GTTG=None, aboutmepage=None, howtopage=None):
        super(Window2, self).__init__()
        #setting title
        self.setWindowTitle('tailor-made Personal Color 앱')
        pal = QPalette()
        pal.setColor(QPalette.Background,QColor(253,253,150))
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        # setting geometry
        self.resize(278,291)

        self.open_btn = QtWidgets.QPushButton('Open Image',self)
        self.open_btn.clicked.connect(self.getImage)
        self.open_btn.setStyleSheet('color:white; background:rgb(0,150,136)')
        self.open_btn.setGeometry(174,110,100,30)

        self.click_btn = QtWidgets.QPushButton('Click Me',self)
        self.click_btn.clicked.connect(self.handleButton)
        self.click_btn.setStyleSheet('color:white; background:rgb(0,150,136)')
        self.click_btn.setGeometry(174,160,100,30)

        self.label = QtWidgets.QLabel('1. Open Image \n 2. Click Me',self)
        self.label.setGeometry(0,0,171,291)

        self.show()
        
        self._window3 = window3
    def getImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', r'C:\Users\Miracle11\211102Tailar-made Personal Color app\customer'
                                            , "Image files (*.jpeg *.gif)")
        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        self.label.setPixmap(QPixmap(pixmap))
        #self.resize(pixmap.width(), pixmap.height())

        print(imagePath)

    def handleButton(self):
        self.hide()
        if self._window3 is None:
            self._window3 = Window3(self)
        self._window3.show()
        
class Window3(QtWidgets.QMainWindow):
    def __init__(self, window1=None, window2=None, GTTG=None, aboutmepage=None, howtopage=None):
        super(Window3, self).__init__()
        #setting title
        
        self.setWindowTitle('tailor-made Personal Color 앱')

        # setting geometry
        self.resize(569, 416)
        
        # setting Combobox
        self.Combo1 = QtWidgets.QComboBox(self)
        self.Combo1.setEditable(True)
        
        self.Combo1_ledit = self.Combo1.lineEdit()
        self.Combo1_ledit.setAlignment(Qt.AlignCenter)
        self.Combo1_ledit.setReadOnly(True)
        self.Combo1.addItem('Daily')
        self.Combo1.addItem('Party look')
        self.Combo1.addItem('Suit')
        self.Combo1.resize(110,30)
        self.Combo1.move(440,250)

        #라벨 생성
        label1 = QLabel(self)
        label1.resize(171, 291)
        label1.move(30,30)
 
 
        #이미지 관련 클래스 생성 및 이미지 불러오기 
        pixmap = QPixmap('./image_woman/w (21).jpeg')

        #이미지 관련 클래스와 라벨 연결 
        label1.setPixmap(pixmap)

        #라벨 생성
        
        label1 = QLabel(self)
        label1.resize(171, 291)
        label1.move(230,30)
 
 
        #이미지 관련 클래스 생성 및 이미지 불러오기 
        
        pixmap = QPixmap('./customer/c (6).jpeg')
    
        #이미지 관련 클래스와 라벨 연결 
        label1.setPixmap(pixmap)

        # setting back btn
        self.back_button = QtWidgets.QPushButton('Back Button', self)
        self.back_button.clicked.connect(self.handleButton)
        self.back_button.setStyleSheet('color:white; background:rgb(251,204,209)')
        self.back_button.setGeometry(440,290,101,31)
        
        self.show()

        self._window2 = window2
    def handleButton(self):
        self.hide()
        if self._window2 is None:
            self._window2 = Window2(self)
        self._window2.show()
    
        
if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = Window1()
    window.show()
    sys.exit(app.exec_())

