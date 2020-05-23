import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(5)
        slider.setMaximum(225)
        slider.setValue(25)
        slider.setTracking(True)
        slider.setTickInterval(5)
        slider.setTickPosition(QSlider.TicksBelow)
        layout.addWidget(slider)

        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Slider")


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
