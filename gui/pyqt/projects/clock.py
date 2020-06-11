import sys

from PyQt5.QtWidgets import *
import datetime
import _thread


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Clock")
        self.setGeometry(50, 50, 500, 300)
        time = datetime.datetime.now()
        full_time = "{0}:{1}:{2}".format(time.hour, time.minute, time.second)
        self.clock = QLCDNumber()
        self.clock.display(full_time)
        self.clock.setDigitCount(8)
        self.clock.setSmallDecimalPoint(True)
        self.setCentralWidget(self.clock)
        try:
            _thread.start_new_thread(self.loop, ())
        except TypeError:
            print("Something went wrong")

    def loop(self):
        while True:
            time = datetime.datetime.now()
            full_time = "{0}:{1}:{2}".format(time.hour, time.minute, time.second)
            self.clock.display(full_time)


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
