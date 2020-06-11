import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Window(QWidget):
	def __init__(self):
		super(Window, self).__init__()
		self.setWindowTitle("Styled LineEdit")
		self.setGeometry(50, 50, 500, 300)
		layout = QFormLayout()
		self.setLayout(layout)
		font = QFont()
		font.setFamily("MonoSpace")
		font.setPointSize(20)
		font.setBold(True)
		default = QLineEdit()
		styled = QLineEdit()
		dynamic = QLineEdit()

		default.setText("Hello, World!")
		styled.setText("Hello, World!")
		dynamic.setText("Hello, World!")

		default.setFont(font)
		styled.setFont(font)
		dynamic.setFont(font)

		default.setReadOnly(True)
		styled.setReadOnly(True)
		dynamic.setReadOnly(True)

		styled.setObjectName("styled")
		dynamic.setProperty("mandatoryField", True)

		layout.addRow("default:", default)
		layout.addRow("styled:", styled)
		layout.addRow("dynamic:", dynamic)
		self.stylesheet()

	def stylesheet(self):
		css = """ 
			QLineEdit#styled {
				background-color: black;
				color: green;
				selection-color: blue;
				selection-background-color: white;
			}
			QLineEdit {
				min-height: 2em;
			}
			*[mandatoryField="true"] {
				background-color: black;
				color: gray;
				selection-color: yellow;
				selection-background-color: green;
			}
			"""
		self.setStyleSheet(css)


app = QApplication(sys.argv)
app.setStyle("Windows")


def main():
	window = Window()
	window.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
