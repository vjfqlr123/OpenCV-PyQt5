import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox, QVBoxLayout, QPushButton


class MyVideoUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel()

        self.comboBox = QComboBox()

        self.saveBtn = QPushButton("&Save")

        self.vBox = QVBoxLayout()
        self.vBox.addWidget(self.comboBox)
        self.vBox.addWidget(self.saveBtn)

        self.hBox = QHBoxLayout()
        self.hBox.addWidget(self.label)
        self.hBox.addLayout(self.vBox)


        self.wrapLayout = QHBoxLayout()
        self.wrapLayout.addLayout(self.hBox)
        self.wrapLayout.addLayout(self.vBox)

        self.setLayout(self.wrapLayout)
        self.resize(1200, 800)
        self.show()

    def AddComboBoxItem(self, itemStr):
        self.comboBox.addItem(itemStr)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = MyVideoUI()
    sys.exit(app.exec_())
