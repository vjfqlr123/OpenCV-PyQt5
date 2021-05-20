## Ex 5-7. QProgressBar.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar, QLineEdit
from PyQt5.QtCore import QBasicTimer


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setMaximum(9)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.result = QLineEdit(self)
        self.result.resize(80, 25)
        self.result.move(150, 80)


        self.timer = QBasicTimer()
        self.step = 0

        self.setWindowTitle('QProgressBar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def timerEvent(self, e):
        if self.step >= 9:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        #print(self.step)
        self.Multi(self.step)
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(1000, self)
            self.btn.setText('Stop')

    def Multi(self, step):
        for i in range(1, 10, 1):
            if step+1 == 10:
                break
            #print('{n+1} * {i} + = {(step+1)*i}')
            print('{} * {} = {}'.format((step+1), i, (step+1)*i))
            self.result.setText(str((step+1)*i))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())