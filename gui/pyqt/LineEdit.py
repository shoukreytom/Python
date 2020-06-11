import sys

from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("PushButton")
        line = QLineEdit()
        line.setPlaceholderText("This is placeholder")
        line.returnPressed.connect(self.on_click)
        self.setCentralWidget(line)
        self.setGeometry(50, 50, 500, 300)

    def on_click(self):
        print(f"Return key is pressed")


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
