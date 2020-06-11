import sys

from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("MenuBar")
        self.setGeometry(50, 50, 500, 300)
        menu_bar = QMenuBar()
        file = menu_bar.addMenu("File")
        file.addAction("New")
        file.addAction("Open")
        file.addSeparator()
        file.addAction("Exit")
        menu_bar.addMenu("Edit")
        menu_bar.addMenu("View")
        menu_bar.addMenu("Settings")
        menu_bar.addMenu("Help")
        self.setMenuBar(menu_bar)


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
