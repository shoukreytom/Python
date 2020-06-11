import sys
import datetime as dt

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("DateTime Edit")
        self.setGeometry(50, 50, 500, 300)
        layout = QGridLayout()
        self.setLayout(layout)
        calendar = QCalendarWidget()
        datetime = QDateTimeEdit()
        time = QTime()
        now = dt.datetime.now()
        time.setHMS(now.hour, now.minute, now.second)
        datetime.setDisplayFormat("yyyy-MM-dd: hh:mm:ss")
        datetime.setTime(time)
        datetime.setCalendarWidget(calendar)
        datetime.setCalendarPopup(True)
        layout.addWidget(datetime, 0, 0)


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
