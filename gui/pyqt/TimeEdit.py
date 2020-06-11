import sys
import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Time Edit")
        self.setGeometry(50, 50, 500, 300)
        layout = QGridLayout()
        self.setLayout(layout)
        time = QTime()
        now = datetime.datetime.now()
        time.setHMS(now.hour, now.minute, now.second)
        time_edit = QTimeEdit()
        time_edit.setTime(time)
        layout.addWidget(time_edit, 0, 0)


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
