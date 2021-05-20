## Ex 5-17. QTimeEdit.

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, QTime

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.stop_btn = QPushButton('멈춤', self)
        self.stop_btn.clicked.connect(self.TimeStop)

        self.start_btn = QPushButton('시작', self)
        self.start_btn.clicked.connect(self.TimeStart)

        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)

        self.lcd = QLCDNumber(self)
        self.lcd.setDigitCount(8)

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.ShowTime)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addWidget(self.start_btn)
        vbox.addWidget(self.stop_btn)

        self.setLayout(vbox)
        self.setWindowTitle('전자시계')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def ShowTime(self):
        sender = self.sender()  # 이벤트 객체에 접근자
        cur = QTime.currentTime().toString("hh:mm:ss")
        if id(sender) == id(self.timer):  # 접근자와 timer가 같으면 화면에 표시
            self.lcd.display(cur)

    def TimeStop(self):
        self.timer.stop()
        self.stop_btn.setEnabled(False)
        self.start_btn.setEnabled(True)

    def TimeStart(self):
        self.timer.start()
        self.stop_btn.setEnabled(True)
        self.start_btn.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.ShowTime()
    sys.exit(app.exec_())