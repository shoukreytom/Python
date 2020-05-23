import sys

from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("HBoxLayout")
        self.setGeometry(50, 50, 500, 300)
        layout = QHBoxLayout()
        self.setLayout(layout)
        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")
        button3 = QPushButton("Button3")
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
