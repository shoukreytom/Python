import sys

from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("PushButton")
        button = QPushButton("Button")
        button.setToolTip("<b>This is <i>button</i></b>")
        button.clicked.connect(self.on_click)
        self.setCentralWidget(button)
        self.setGeometry(50, 50, 500, 300)

    def on_click(self):
        sender = self.sender()
        print(f"{sender.text()} is clicked")


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
