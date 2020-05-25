import sys

from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("File Dialog")
        self.setGeometry(50, 50, 500, 300)
        layout = QGridLayout()
        self.setLayout(layout)

        button = QPushButton("Open")
        button.clicked.connect(self.open)
        layout.addWidget(button, 0, 0)
        self.file = QFileDialog()
        self.file.setViewMode(QFileDialog.Detail)
        self.file.setWindowTitle("Selecting file")
        self.file.setAcceptMode(QFileDialog.AcceptOpen)

    def open(self):
        self.file.open()


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
