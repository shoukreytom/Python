import sys


from PyQt5.QtWidgets import *


class Window(QWidget):
	def __init__(self):
		super(Window, self).__init__()
		self.setWindowTitle("ButtonGroup")
		self.setGeometry(50, 50, 500, 300)
		layout = QGridLayout()
		self.setLayout(layout)
		button_group = QButtonGroup()
		button_group.setExclusive(True)
		button1 = QPushButton("Button1")
		button_group.addButton(button1, 0)
		layout.addWidget(button1, 0, 0)
		button2 = QPushButton("Button2")
		button_group.addButton(button2, 1)
		layout.addWidget(button2, 0, 1)


app = QApplication(sys.argv)


def main():
	window = Window()
	window.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
