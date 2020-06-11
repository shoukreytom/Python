import sys

from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Tab Bar")
        self.setGeometry(50, 50, 500, 300)
        layout = QGridLayout()
        self.setLayout(layout)
        tab_bar = QTabBar()
        tab_bar.addTab("Tab 1")
        tab_bar.addTab("Tab 2")
        tab_bar.addTab("Tab 3")
        tab_bar.addTab("Tab 4")
        layout.addWidget(tab_bar, 0, 0)


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
