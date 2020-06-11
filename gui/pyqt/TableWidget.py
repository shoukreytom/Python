import sys

from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Table Widget")
        self.setGeometry(50, 50, 500, 300)
        layout = QGridLayout()
        self.setLayout(layout)
        self.table = QTableWidget()
        self.table.setRowCount(5)
        self.table.setColumnCount(4)
        item = QTableWidgetItem("Shoukrey")
        self.table.setItem(0, 0, item)
        layout.addWidget(self.table)


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

