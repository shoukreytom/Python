import sys

from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("MessageBox")
        self.setGeometry(50, 50, 500, 300)
        layout = QGridLayout()
        self.setLayout(layout)
        button = QPushButton("Click me")
        button.clicked.connect(self.show_msg)
        layout.addWidget(button, 0, 0)
        self.msg = QMessageBox()
        self.msg.setText("Button Click")
        self.msg.setInformativeText("You've just clicked a button")
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setStandardButtons(QMessageBox.Close)

    def show_msg(self):
        self.msg.show()


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
