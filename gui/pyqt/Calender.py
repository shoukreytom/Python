import sys

from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Calender")
        self.setGeometry(50, 50, 500, 300)
        layout = QGridLayout()
        self.setLayout(layout)
        self.calender = QCalendarWidget()
        self.calender.setGridVisible(True)
        self.calender.setNavigationBarVisible(True)
        self.calender.selectionChanged.connect(self.handle_selection)
        layout.addWidget(self.calender, 0, 0)

    def handle_selection(self):
        selected = self.calender.selectedDate()
        print(selected.toString("yyyy-MM-dd"))


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
