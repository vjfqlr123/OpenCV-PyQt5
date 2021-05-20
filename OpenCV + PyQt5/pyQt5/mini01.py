import cv2
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        img = cv2.imread('./lena.png')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
        w, h, c = img.shape
        lbl_img = QLabel()

        qimg = QtGui.QImage(img.data, w, h, img.strides[0], QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qimg)
        lbl_img.setPixmap(pixmap)
        

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_img)
        
        self.setLayout(vbox)

        self.setWindowTitle('QPixmap')
        self.move(300, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())