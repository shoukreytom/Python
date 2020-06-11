import sys

from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("LCDNumber")
        self.setGeometry(50, 50, 500, 300)
        layout = QGridLayout()
        self.setLayout(layout)
        lcd = QLCDNumber()
        lcd.display("11:44")
        # lcd.display(4.32221)
        # lcd.setDecMode()
        # lcd.setSmallDecimalPoint(True)
        layout.addWidget(lcd, 0, 0)


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
