import cv2
import sys
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5 import QtGui
from PyQt5 import QtCore

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.running = False

        self.cap = cv2.VideoCapture(0)
        frmae_size = (int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                      int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        
        self.label = QLabel()
        
        btn1 = QPushButton('ON', self)
        btn2 = QPushButton('OFF', self)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)

        self.setLayout(vbox)
        self.setWindowTitle('PC_CAM')

        btn1.clicked.connect(self.CAM_ON)
        btn1.clicked.connect(self.CAM_OFF)

        self.move(300, 300)
        self.resize(400, 200)
        self.show()

    def CAM_ON(self):

        pass

    def CAM_OFF(self):
        pass

    
    

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())