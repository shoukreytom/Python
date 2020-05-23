import sys

from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("ComboBox")
        combo = QComboBox()
        combo.setWhatsThis("<b>This is <i>comboBox</i></b>")
        self.setCentralWidget(combo)
        self.setGeometry(50, 50, 500, 300)

    def on_click(self):
        sender = self.sender()
        print(f"{sender.text()} is clicked")


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
