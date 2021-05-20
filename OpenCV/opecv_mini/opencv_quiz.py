import cv2
import threading
import time
import sys
from PyQtVideo import MyVideoUI
from cvVideo import Video
from PyQt5 import QtWidgets


app = QtWidgets.QApplication(sys.argv)
ex = MyVideoUI()
ex.AddComboBoxItem("original")
ex.AddComboBoxItem("blur")
ex.AddComboBoxItem("medianBlur")
ex.AddComboBoxItem("Gaussianbur")
ex.AddComboBoxItem("threshold")
ex.AddComboBoxItem("Sobel")
ex.AddComboBoxItem("Laplacian")
ex.AddComboBoxItem("reverse")

v = Video()

def run():
    t = 0
    while t < 2000:
        ex.label.setPixmap(v.updateFrame())
        time.sleep(0.01)
        t += 1

    v.close()

def selectedFilter(text):
    v.filter.setFilter(text)

ex.comboBox.currentTextChanged.connect(selectedFilter)
ex.saveBtn.clicked.connect(v.saveImg)

th = threading.Thread(target=run)
th.start()

sys.exit(app.exec_())
