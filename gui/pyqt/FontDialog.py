import sys

from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Font Dialog")
        self.setGeometry(50, 50, 500, 300)
        layout = QGridLayout()
        self.setLayout(layout)
        button = QPushButton("Choose Font")
        button.clicked.connect(self.open)
        layout.addWidget(button, 0, 0)
        self.font = QFontDialog()

    def open(self):
        self.font.open()


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
