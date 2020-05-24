import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Date Edit")
        self.setGeometry(50, 50, 400, 300)
        layout = QGridLayout()
        self.setLayout(layout)
        date = QDate()
        date.setDate(2000, 5, 3)
        date_edit = QDateEdit()
        date_edit.setDisplayFormat("yyyy-MM-dd")
        date_edit.setMinimumDate(date)
        date_edit.setDate(date)
        layout.addWidget(date_edit, 0, 0)


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
