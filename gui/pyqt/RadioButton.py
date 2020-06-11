import sys

from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("PushButton")
        layout = QBoxLayout(QBoxLayout.LeftToRight)
        layout2 = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(layout)
        submit = QPushButton("Submit")
        submit.clicked.connect(self.submit)
        gender_l = QLabel("Gender:")
        male = QRadioButton("Male")
        male.setChecked(True)
        male.gender = "Male"
        female = QRadioButton("Female")
        female.gender = "Female"
        male.toggled.connect(self.get_checked)
        female.toggled.connect(self.get_checked)
        layout.addWidget(gender_l)
        layout2.addWidget(male)
        layout2.addWidget(female)
        layout2.addWidget(submit)
        layout.addLayout(layout2)
        self.setGeometry(50, 50, 500, 300)

    def get_checked(self):
        sender = self.sender()
        if sender.isChecked():
            print(f"{sender.text()} is checked")

    @staticmethod
    def submit():
        print("Ok")


app = QApplication(sys.argv)


def main():
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
