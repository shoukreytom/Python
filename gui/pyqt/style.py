import sys
import parser

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Style")
        self.setStyleSheet("QPushButton {min-width: 5em;min-height: 2em}")
        layout = QGridLayout()
        screen_font = QFont()
        buttons_font = QFont()
        screen_font.setFamily("MonoSpace")
        screen_font.setPointSize(18)
        screen_font.setBold(True)
        buttons_font.setFamily("MonoSpace")
        buttons_font.setPointSize(16)
        buttons_font.setBold(True)
        self.screen = QLineEdit()
        self.screen.setFont(screen_font)
        self.screen.setReadOnly(True)
        self.screen.setMaxLength(40)
        self.screen.setStyleSheet("min-height: 3em")

        one = QPushButton("1")
        tow = QPushButton("2")
        three = QPushButton("3")
        multi = QPushButton("*")
        undo = QPushButton("X")
        one.clicked.connect(self.get_text)
        tow.clicked.connect(self.get_text)
        three.clicked.connect(self.get_text)
        multi.clicked.connect(self.get_text)
        undo.clicked.connect(self.undo)
        one.setFont(buttons_font)
        tow.setFont(buttons_font)
        three.setFont(buttons_font)
        multi.setFont(buttons_font)
        undo.setFont(buttons_font)

        four = QPushButton("4")
        five = QPushButton("5")
        six = QPushButton("6")
        minus = QPushButton("-")
        power = QPushButton("^")
        four.clicked.connect(self.get_text)
        five.clicked.connect(self.get_text)
        six.clicked.connect(self.get_text)
        minus.clicked.connect(self.get_text)
        power.clicked.connect(self.get_text)
        four.setFont(buttons_font)
        five.setFont(buttons_font)
        six.setFont(buttons_font)
        minus.setFont(buttons_font)
        power.setFont(buttons_font)

        seven = QPushButton("7")
        eight = QPushButton("8")
        nine = QPushButton("9")
        div = QPushButton("/")
        fac = QPushButton("!")
        seven.clicked.connect(self.get_text)
        eight.clicked.connect(self.get_text)
        nine.clicked.connect(self.get_text)
        div.clicked.connect(self.get_text)
        # fac.clicked.connect(self.get_text)
        seven.setFont(buttons_font)
        eight.setFont(buttons_font)
        nine.setFont(buttons_font)
        div.setFont(buttons_font)
        fac.setFont(buttons_font)

        decimal = QPushButton(".")
        zero = QPushButton("0")
        equal = QPushButton("=")
        plus = QPushButton("+")
        clear = QPushButton("C")
        decimal.clicked.connect(self.get_text)
        zero.clicked.connect(self.get_text)
        equal.clicked.connect(self.equal)
        plus.clicked.connect(self.get_text)
        clear.clicked.connect(self.clear)
        decimal.setFont(buttons_font)
        zero.setFont(buttons_font)
        equal.setFont(buttons_font)
        plus.setFont(buttons_font)
        clear.setFont(buttons_font)

        # first row
        layout.addWidget(self.screen, 0, 0, 1, 5)

        # second row
        layout.addWidget(one, 1, 0)
        layout.addWidget(tow, 1, 1)
        layout.addWidget(three, 1, 2)
        layout.addWidget(multi, 1, 3)
        layout.addWidget(undo, 1, 4)

        # third row
        layout.addWidget(four, 2, 0)
        layout.addWidget(five, 2, 1)
        layout.addWidget(six, 2, 2)
        layout.addWidget(minus, 2, 3)
        layout.addWidget(power, 2, 4)

        # fourth row
        layout.addWidget(seven, 3, 0)
        layout.addWidget(eight, 3, 1)
        layout.addWidget(nine, 3, 2)
        layout.addWidget(div, 3, 3)
        layout.addWidget(fac, 3, 4)

        # fifth row
        layout.addWidget(decimal, 4, 0)
        layout.addWidget(zero, 4, 1)
        layout.addWidget(equal, 4, 2)
        layout.addWidget(plus, 4, 3)
        layout.addWidget(clear, 4, 4)

        layout.setVerticalSpacing(10)
        self.setLayout(layout)
        self.setGeometry(50, 50, 400, 200)

    def get_text(self):
        text = self.screen.text()
        sender = self.sender()
        self.screen.setText(text + sender.text())

    def clear(self):
        self.screen.clear()

    def undo(self):
        text = self.screen.text()
        self.screen.setText(text[:-1])

    def equal(self):
        text = self.screen.text()
        try:
            p = parser.expr(text).compile()
            r = eval(p)
            self.screen.setText(str(r))
        except parser.ParserError:
            self.screen.setText("Error")


""" window styles on QT:
        1- Fusion
        2- Windows
        3- Adwaita-Dark
        4- Adwaita
    this is for linux(fedora)
"""


app = QApplication(sys.argv)
app.setStyle('Windows')


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
