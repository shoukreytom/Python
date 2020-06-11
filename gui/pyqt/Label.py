import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        label = QLabel("This is label")
        label.setAlignment(Qt.AlignCenter)
        self.setWindowTitle("Label")
        self.setCentralWidget(label)
        self.setGeometry(50, 50, 500, 300)


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
