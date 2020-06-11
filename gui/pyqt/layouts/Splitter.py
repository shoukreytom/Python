import sys

from PyQt5.QtWidgets import *


class Window(QWidget):
	def __init__(self):
		super(Window, self).__init__()
		self.setWindowTitle("SplitterLayout")
		self.setGeometry(50, 50, 500, 300)
		splitter = QSplitter()
		text = QTextEdit()
		frame = QFrame()
		frame.setFrameShadow(QFrame.Raised)
		frame.setLineWidth(2)
		frame.setFrameShape(QFrame.StyledPanel)
		splitter.addWidget(text)
		splitter.addWidget(frame)
		hBox = QHBoxLayout()
		self.setLayout(hBox)
		hBox.addWidget(splitter)


app = QApplication(sys.argv)


def main():
	window = Window()
	window.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
