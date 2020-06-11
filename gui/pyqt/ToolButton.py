import sys

from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("ToolButton")
        self.setGeometry(50, 50, 500, 300)
        layout = QGridLayout()
        self.setLayout(layout)
        tool_bar = QToolBar()
        button1 = QToolButton()
        button1.setCheckable(True)
        button1.setText("Button1")
        button1.setAutoExclusive(True)
        button2 = QToolButton()
        button2.setCheckable(True)
        button2.setText("Button2")
        button2.setAutoExclusive(True)
        button3 = QToolButton()
        button3.setCheckable(True)
        button3.setText("Button3")
        button3.setAutoExclusive(True)
        tool_bar.addWidget(button1)
        tool_bar.addWidget(button2)
        tool_bar.addWidget(button3)
        layout.addWidget(tool_bar)


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
