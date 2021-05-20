import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        add_btn = QPushButton('더하기', self)
        cancel_btn = QPushButton('cancle', self)
        sub_btn = QPushButton('빼기', self)
        mul_btn = QPushButton('곱하기', self)
        div_btn = QPushButton('나누기', self)
        add_btn.clicked.connect(self.Add)
        sub_btn.clicked.connect(self.Subtract)
        mul_btn.clicked.connect(self.Multiply)
        div_btn.clicked.connect(self.Division)
        cancel_btn.clicked.connect(QCoreApplication.instance().quit)

        self.edit1 = QLineEdit('5')
        self.edit2 = QLineEdit('8')
        lblequl = QLabel('=')
        self.editresult = QLineEdit('결과')

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.edit1)
        hbox1.addWidget(self.edit2)
        hbox1.addWidget(lblequl)
        hbox1.addWidget(self.editresult)
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(add_btn)
        hbox2.addWidget(sub_btn)
        hbox2.addWidget(mul_btn)
        hbox2.addWidget(div_btn)
        hbox2.addWidget(cancel_btn)
        hbox2.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)

        self.setLayout(vbox)
        self.setWindowTitle('계산기')
        self.resize(400, 300)
        self.show()

    def Add(self):
        result = int(self.edit1.text()) + int(self.edit2.text())
        self.editresult.setText(str(result))

    def Subtract(self):
        result = int(self.edit1.text()) - int(self.edit2.text())
        self.editresult.setText(str(result))

    def Multiply(self):
        result = int(self.edit1.text()) * int(self.edit2.text())
        self.editresult.setText(str(result))

    def Division(self):
        result = int(self.edit1.text()) / int(self.edit2.text())
        self.editresult.setText(str(result))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())