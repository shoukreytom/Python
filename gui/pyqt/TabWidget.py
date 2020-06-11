import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("TabWidget")
        self.setGeometry(50, 50, 500, 300)
        layout = QGridLayout()
        self.setLayout(layout)
        tab_pane = QTabWidget()
        button = QPushButton("Hello")
        label = QLabel("Label")
        tab_pane.addTab(button, "Tab 1")
        tab_pane.addTab(label, "Tab 2")
        layout.addWidget(tab_pane, 0, 0)


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
