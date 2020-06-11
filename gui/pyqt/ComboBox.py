import sys

from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("ComboBox")
        self.setGeometry(50, 50, 500, 300)
        layout = QGridLayout()
        self.setLayout(layout)
        self.combo = QComboBox()
        items = ["Sudan", "USA", "UK", "India", "Egypt", "Russia"]
        line = QLineEdit()
        self.combo.setEditable(True)
        self.combo.setLineEdit(line)
        self.combo.addItems(items)
        self.combo.setWhatsThis("<b>This is <i>comboBox</i></b>")
        self.combo.currentTextChanged.connect(self.text_changed)
        layout.addWidget(self.combo, 0, 0)

    def text_changed(self):
        text = self.combo.currentText()
        print(f"Your Country: {text}")


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
