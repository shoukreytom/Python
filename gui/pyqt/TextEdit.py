import sys

from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Text Edit")
        self.setGeometry(50, 50, 500, 300)
        layout = QGridLayout()
        self.setLayout(layout)
        text = QTextEdit()
        html = "<h1>Header</h1><br/><b>Bold Text</b>"
        text.setPlaceholderText("Text Edit")
        text.insertHtml(html)
        layout.addWidget(text)


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
