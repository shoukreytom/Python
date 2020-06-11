import sys

from PyQt5.QtWidgets import *


class Window(QWidget):
	def __init__(self):
		super(Window, self).__init__()
		self.setWindowTitle("GroupBox")
		self.setGeometry(50, 50, 500, 300)
		layout = QGridLayout()
		self.setLayout(layout)
		group = QGroupBox("Gender")
		layout.addWidget(group)
		vbox = QVBoxLayout()
		group.setLayout(vbox)
		male = QRadioButton("Male")
		male.setChecked(True)
		vbox.addWidget(male)
		female = QRadioButton("Female")
		vbox.addWidget(female)


app = QApplication(sys.argv)



def main():
	window = Window()
	window.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
