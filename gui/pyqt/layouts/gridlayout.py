import sys

from PyQt5.QtWidgets import *


class Window(QWidget):
	def __init__(self):
		super(Window, self).__init__()
		self.setWindowTitle("GridLayout")
		layout = QGridLayout()
		self.setLayout(layout)

		button00 = QPushButton("button(0, 0)")
		button01 = QPushButton("button(0, 1)")
		button10 = QPushButton("button(1, 0)")
		button11 = QPushButton("button(1, 1)")
		button02 = QPushButton("bigButton")

		button00.setFixedHeight(90)
		button01.setFixedHeight(90)
		button10.setFixedHeight(90)
		button11.setFixedHeight(90)
		button02.setFixedHeight(200)

		layout.addWidget(button00, 0, 0)
		layout.addWidget(button01, 0, 1)
		layout.addWidget(button10, 1, 0)
		layout.addWidget(button11, 1, 1)
		layout.addWidget(button02, 0, 2, 2, 1)


app = QApplication(sys.argv)


def main():
	window = Window()
	window.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()

