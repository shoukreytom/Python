import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Dial")
        self.setGeometry(50, 50, 500, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)
        dial = QDial()
        dial.setMinimum(0)
        dial.setMaximum(100)
        dial.setValue(30)
        dial.setNotchesVisible(True)
        layout.addWidget(dial)


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
