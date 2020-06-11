import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Completer")
        self.setGeometry(50, 50, 500, 300)
        layout = QGridLayout()
        self.setLayout(layout)

        f = open("/home/shoukrey/words.txt", "r")
        suggestions = f.readlines()

        completer1 = QCompleter(suggestions)
        completer2 = QCompleter(suggestions)
        completer3 = QCompleter(suggestions)

        completer1.setCaseSensitivity(Qt.CaseInsensitive)
        completer1.setCompletionMode(QCompleter.InlineCompletion)

        completer2.setCaseSensitivity(Qt.CaseSensitive)
        completer2.setCompletionMode(QCompleter.PopupCompletion)

        completer3.setCompletionMode(QCompleter.UnfilteredPopupCompletion)

        line1 = QLineEdit()
        line1.setCompleter(completer1)
        line2 = QLineEdit()
        line2.setCompleter(completer2)
        line3 = QLineEdit()
        line3.setCompleter(completer3)

        layout.addWidget(line1, 0, 0)
        layout.addWidget(line2, 1, 0)
        layout.addWidget(line3, 2, 0)


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
