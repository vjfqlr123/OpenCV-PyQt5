import cv2
import numpy as np
from PyQt5 import QtGui
from cvFilter import Filter

class Video:
    def __init__(self, device=0):
        self.cap = cv2.VideoCapture(device)
        retval, self.frame = self.cap.read()
        self.filter = Filter()

    def updateFrame(self):
        retval, self.frame = self.cap.read()
        self.filteredImg = self.filter.applyFilter(self.frame)
        result = self.convertCVImgToQtPixmap(self.filteredImg)
        return result

    def convertCVImgToQtPixmap(self, cvImg):
        if type(cvImg[0][0]) == np.uint8:
            h, w = cvImg.shape
            qImg = QtGui.QImage(cvImg.data, w, h, w , QtGui.QImage.Format_Grayscale8)
        else:
            cvImg = cv2.cvtColor(cvImg, cv2.COLOR_BGR2RGB)
            h, w, c = cvImg.shape
            qImg = QtGui.QImage(cvImg.data, w, h, w * c, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qImg)

        return pixmap

    def saveImg(self):
        cv2.imwrite("c:\\cv\\image.jpg", self.filteredImg)
        print(234)

    def close(self):
        if self.cap.isOpened():
            self.cap.release()

        print("Finish Capture")



