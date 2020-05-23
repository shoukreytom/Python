import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("ScrollArea")
        self.setGeometry(50, 50, 500, 300)
        layout = QHBoxLayout()
        scroll = QScrollArea()
        self.setLayout(layout)
        layout.addWidget(scroll)
        # not implemented yet


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
