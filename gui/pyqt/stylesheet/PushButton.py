import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Styled PushButton")
        self.setGeometry(50, 50, 500, 300)
        layout = QGridLayout()
        self.setLayout(layout)

        default = QPushButton("Default")
        flat = QPushButton("Flat")
        flat.setFlat(True)
        styled = QPushButton("Styled")
        styled.setObjectName("styled")

        layout.addWidget(default, 0, 0)
        layout.addWidget(flat, 0, 1)
        layout.addWidget(styled, 1, 0)
        self.stylesheet()

    def stylesheet(self):
    	css = """
    		QPushButton {
    			min-height: 2em;
    			font: bold 18px;
    		}
    		QPushButton#styled {
    			background-color: #32e1e3;
    			color: black;
    			border-style: outset;
    			border-width: 1px;
    			border-color: #43e2e4;
    			border-radius: 20px;
    			padding: 6px;
    		}
    		QPushButton#styled:hover {
    			background-color:#4455e8;
    			color: white;
    		}
    		QPushButton#styled:pressed {
    			background-color:#99e5e8;
    			color: white;
    		}
    	"""
    	self.setStyleSheet(css)


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
