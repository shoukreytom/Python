import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("ProgressDialog")
        self.setGeometry(50, 50, 500, 300)
        layout = QGridLayout()
        self.setLayout(layout)
        progress = QProgressDialog()
        line = QTextEdit()
        cancel = QPushButton("Cancel")
        progress.setValue(30)
        progress.setMinimum(1)
        progress.setMaximum(101)
        progress.setCancelButton(cancel)
        layout.addWidget(line, 0, 0)
        layout.addWidget(progress, 1, 0)


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
