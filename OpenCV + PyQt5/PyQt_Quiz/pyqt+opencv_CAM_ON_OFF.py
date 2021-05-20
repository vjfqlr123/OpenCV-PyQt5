import cv2
import sys
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox
from PyQt5 import QtGui
from PyQt5 import QtCore

running = False

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.cap = cv2.VideoCapture(0)
        frmae_size = (int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                      int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

        self.label = QLabel()
        self.label.resize(frmae_size[0], frmae_size[1])

        self.start_cam_btn = QPushButton('CAM ON', self)
        self.start_cam_btn.clicked.connect(self.CAM_ON)
        self.start_cam_btn.setEnabled(True)

        self.stop_cam_btn = QPushButton('CAM OFF', self)
        self.stop_cam_btn.clicked.connect(self.CAM_OFF)
        self.stop_cam_btn.setEnabled(False)

        app.aboutToQuit.connect(self.onExit)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.start_cam_btn)
        vbox.addWidget(self.stop_cam_btn)

        self.setLayout(vbox)
        self.setWindowTitle('PC_CAM')

        self.resize(600, 480)
        self.show()

    def RUN(self):
        global running

        while running:
            ret, img = self.cap.read()
            if ret:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                h,w,c = img.shape
                qimg = QtGui.QImage(img.data, w, h, w*c, QtGui.QImage.Format_RGB888)
                pixmap = QtGui.QPixmap.fromImage(qimg)
                self.label.setPixmap(pixmap)
            else:
                QMessageBox.about(win, "Error", "Cannot read frame.")
                print("error")
                break
        self.cap.release()
        print('Thread end.')

    def CAM_ON(self):
        global running
        running = True
        th = threading.Thread(target=self.RUN)
        th.start()
        print("start")
        self.start_cam_btn.setEnabled(False)
        self.stop_cam_btn.setEnabled(True)

    def CAM_OFF(self):
        global running
        running = False
        print("stop")
        self.start_cam_btn.setEnabled(True)
        self.stop_cam_btn.setEnabled(False)

    def onExit(self):
        global running
        running = False
        print("exit")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())