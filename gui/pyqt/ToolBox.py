import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("ToolBox")
        self.setGeometry(50, 50, 500, 300)
        layout = QGridLayout()
        self.setLayout(layout)
        tool_box = QToolBox()
        label = QLabel()
        tool_box.addItem(label, "Honda")
        label = QLabel()
        tool_box.addItem(label, "Kya")
        label = QLabel()
        tool_box.addItem(label, "Land")
        layout.addWidget(tool_box, 0, 0)


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
