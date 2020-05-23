import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QWidget):
	def __init__(self):
		super(Window, self).__init__()
		self.setWindowTitle("SizeGrip")
		self.setGeometry(50, 50, 500, 300)
		flags = Qt.WindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
		self.setWindowFlags(flags)
		size_grip = QSizeGrip(self)
		size_grip.setVisible(True)
		vBox = QVBoxLayout()
		vBox.addWidget(size_grip)
		self.setLayout(vBox)


app = QApplication(sys.argv)


def main():
	window = Window()
	window.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
