import sys

from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Form Layout")
        self.setGeometry(50, 50, 300, 200)
        layout = QFormLayout()
        self.setLayout(layout)
        name_l = QLabel("Name")
        name = QLineEdit()
        layout.addRow(name_l, name)
        email = QLineEdit()
        layout.addRow("Email", email)
        password_l = QLabel("Password")
        password = QLineEdit()
        layout.addRow(password_l, password)


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
