import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QObject

img_path = 'lena.jpg'

class Myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.bt1 = QPushButton('1', self)
        self.bt1.setEnabled(False)
        self.bt2 = QPushButton('2', self)
        self.bt2.setEnabled(True)

        self.pixmap = QPixmap(img_path)
        self.lbl_img = QLabel()
        self.lbl_img.setPixmap(self.pixmap)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.bt1)
        self.vbox.addWidget(self.bt2)
        self.vbox.addWidget(self.lbl_img)

        self.setLayout(self.vbox)
        self.setWindowTitle('Quiz')
        self.move(500, 500)
        self.show()

        self.bt1.clicked.connect(self.BT1)
        self.bt2.clicked.connect(self.BT2)

    def BT1(self):
        global img_path
        if img_path == "0205.png":
            img_path = "lena.jpg"
            self.pixmap = QPixmap(img_path)
            self.lbl_img.setPixmap(self.pixmap)

        self.bt1.setEnabled(False)
        self.bt2.setEnabled(True)


    def BT2(self):
        global img_path
        if img_path == "lena.jpg":
            img_path = "0205.png"
            self.pixmap = QPixmap(img_path)
            self.lbl_img.setPixmap(self.pixmap)

        self.bt1.setEnabled(True)
        self.bt2.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Myapp()
    sys.exit(app.exec_())