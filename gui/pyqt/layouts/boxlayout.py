import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(layout)
        label = QPushButton("Label 1")
        layout.addWidget(label, 0)
        label = QPushButton("Label 2")
        layout.addWidget(label, 0)
        layout2 = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addLayout(layout2)
        label = QLabel("Label 3")
        layout2.addWidget(label, 1)
        label = QLabel("Label 4")
        layout2.addWidget(label, 1)
        self.setWindowTitle("BoxLayout")
        self.setGeometry(50, 50, 400, 200)


app = QApplication(sys.argv)

window = Window()
window.show()
sys.exit(app.exec_())
