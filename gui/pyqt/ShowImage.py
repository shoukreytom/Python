import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Show Image")
        self.setGeometry(50, 50, 500, 300)
        self.counter = 1
        layout = QGridLayout()
        self.setLayout(layout)
        self.pix_map1 = QPixmap("images/37556.jpg")
        self.pix_map2 = QPixmap("images/37563.jpg")
        self.pix_map3 = QPixmap("images/37601.jpg")
        self.pix_map4 = QPixmap("images/37616.jpg")
        self.image = QLabel()
        self.image.setFixedSize(500, 300)
        self.image.setScaledContents(True)
        self.image.setPixmap(self.pix_map1)
        next = QPushButton(">>")
        next.clicked.connect(self.next)
        previous = QPushButton("<<")
        previous.clicked.connect(self.previous)
        layout2 = QHBoxLayout()
        layout2.addWidget(previous)
        layout2.addWidget(next)
        layout2.setSpacing(30)
        layout.addWidget(self.image, 0, 0)
        layout.addLayout(layout2, 1, 0)

    def next(self):
        if self.counter == 1:
            self.image.setPixmap(self.pix_map2)
            self.counter += 1
        elif self.counter == 2:
            self.image.setPixmap(self.pix_map3)
            self.counter += 1
        elif self.counter == 3:
            self.image.setPixmap(self.pix_map4)
            self.counter += 1
        else:
            self.image.setPixmap(self.pix_map1)
            self.counter = 1

    def previous(self):
        if self.counter == 4:
            self.image.setPixmap(self.pix_map3)
            self.counter -= 1
        elif self.counter == 3:
            self.image.setPixmap(self.pix_map2)
            self.counter -= 1
        elif self.counter == 2:
            self.image.setPixmap(self.pix_map1)
            self.counter -= 1
        else:
            self.image.setPixmap(self.pix_map4)
            self.counter = 4


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
