import sys

from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("ListWidget")
        self.setGeometry(50, 50, 500, 300)
        layout = QGridLayout()
        self.setLayout(layout)
        self.list_widget = QListWidget()
        items = ["Sudan", "India", "China", "Japan", "Russia", "US", "UK"]
        self.list_widget.addItems(items)
        self.list_widget.setCurrentRow(0)
        self.list_widget.clicked.connect(self.clicked)
        layout.addWidget(self.list_widget, 0, 0)

    def clicked(self):
        item = self.list_widget.currentItem()
        print(item.text())


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
