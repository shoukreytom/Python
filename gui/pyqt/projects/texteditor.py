import sys

from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Text Editor")
        self.setGeometry(50, 50, 500, 300)
        self.text = QTextEdit()
        menu_bar = QMenuBar()
        file = menu_bar.addMenu("File")
        file.addAction("New")
        file.addAction("Open")
        file.addAction("Save")
        file.addAction("Save As")
        file.addSeparator()
        exit_m = file.addAction("Exit")
        exit_m.triggered.connect(self.exit_app)
        edit = menu_bar.addMenu("Edit")
        edit.addAction("Undo")
        edit.addAction("Redo")
        edit.addAction("Copy")
        edit.addAction("Cut")
        edit.addAction("Paste")
        edit.addSeparator()
        edit.addAction("Select All")
        tools = menu_bar.addMenu("Tools")
        tools.addAction("Preference")
        window = menu_bar.addMenu("Window")
        window.addAction("New Window")
        show = window.addMenu("Show")
        show.addAction("Tool Bar")
        help_m = menu_bar.addMenu("Help")
        help_m.addAction("Help")
        help_m.addAction("About us")
        self.setMenuBar(menu_bar)
        self.setCentralWidget(self.text)

    def exit_app(self):
        print("close")
        self.close()


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
