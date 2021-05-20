import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QObject

class Myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.cler1 = True
        self.cler2 = True

        bt1 = QPushButton('1', self)
        bt2 = QPushButton('2', self)

        self.img1 = QPixmap('lena.png')
        self.pixmap1 = QLabel()
        self.pixmap1.setPixmap(self.img1)

        self.img2 = QPixmap('0205.png')
        self.pixmap2 = QLabel()
        self.pixmap2.setPixmap(self.img2)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(bt1)
        self.vbox.addWidget(bt2)
        
        bt1.clicked.connect(self.BT1)
        bt2.clicked.connect(self.BT2)

        self.setLayout(self.vbox)
        self.setWindowTitle('Quiz')
        self.move(500, 500)
        self.show()

    def BT1(self):
        if self.cler2 == True:
            self.pixmap2.clear()
            self.cler2 = False
        
            self.vbox.addWidget(self.pixmap1)
        
        

    def BT2(self):
        if self.cler1 == True:
            self.pixmap1.clear()
            self.cler1 = False
        
            self.vbox.addWidget(self.pixmap2)
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Myapp()
    sys.exit(app.exec_())
    


