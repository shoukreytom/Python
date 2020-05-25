import sys

from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Wizard")
        self.setGeometry(50, 50, 500, 300)
        layout = QGridLayout()
        self.setLayout(layout)
        button = QPushButton("Lunch")
        button.clicked.connect(self.open)
        layout.addWidget(button, 0, 0)
        self.wizard = QWizard()
        self.wizard.setWindowTitle("Wizard")
        page1 = QWizardPage()
        form = QFormLayout()
        form.addRow("Name", QLineEdit())
        page1.setLayout(form)

        page2 = QWizardPage()
        grid = QGridLayout()
        grid.addWidget(QPushButton("1"), 0, 0)
        grid.addWidget(QPushButton("2"), 0, 1)
        grid.addWidget(QPushButton("3"), 1, 0)
        grid.addWidget(QPushButton("4"), 1, 1)
        page2.setLayout(grid)

        page3 = QWizardPage()
        vbox = QVBoxLayout()
        vbox.addWidget(QPushButton("Button 1"))
        vbox.addWidget(QPushButton("Button 2"))
        vbox.addWidget(QPushButton("Button 3"))
        vbox.addWidget(QPushButton("Button 4"))
        page3.setLayout(vbox)

        self.wizard.setPage(1, page1)
        self.wizard.setPage(2, page2)
        self.wizard.setPage(3, page3)

    def open(self):
        self.wizard.open()


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
