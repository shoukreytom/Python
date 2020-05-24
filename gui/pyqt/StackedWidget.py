import sys

from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("StackedWidget")
        self.setMinimumSize(500, 300)
        self.setGeometry(50, 50, 500, 300)
        layout = QGridLayout()
        self.setLayout(layout)
        self.stacked = QStackedWidget()
        layout.addWidget(self.stacked, 0, 0)
        for i in range(1, 5):
            label = QLabel(f"Label {i}")
            self.stacked.addWidget(label)
            button = QPushButton(f"Button {i}")
            button.clicked.connect(self.connect)
            button.page = i
            layout.addWidget(button, i, 0)

    def connect(self):
        sender = self.sender()
        self.stacked.setCurrentIndex(sender.page - 1)


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
