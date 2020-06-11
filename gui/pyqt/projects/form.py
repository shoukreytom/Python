import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form")
        self.setGeometry(50, 50, 300, 300)
        self.setMinimumSize(500, 300)
        main_layout = QGridLayout()
        layout = QFormLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        self.setLayout(main_layout)

        l_name = QLabel()
        l_name.setMinimumWidth(50)
        l_name.setMinimumHeight(40)
        pix_map = QPixmap("icons/user.png")
        l_name.setPixmap(pix_map)
        self.name_f = QLineEdit()
        self.name_f.setPlaceholderText("Type your name")
        self.name_f.setMaxLength(20)

        l_email = QLabel()
        self.email_f = QLineEdit()
        self.email_f.setPlaceholderText("Type your email")
        self.email_f.setMaxLength(30)

        l_password = QLabel()
        pix_map = QPixmap("icons/password.png")
        l_password.setPixmap(pix_map)
        l_password.setMinimumWidth(50)
        l_password.setMinimumHeight(40)
        self.password_f = QLineEdit()
        self.password_f.setEchoMode(QLineEdit.Password)
        self.password_f.setPlaceholderText("Type your password")
        self.password_f.setMaxLength(15)

        log = QPushButton("Log In")
        log.clicked.connect(self.submit)
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.exit_app)
        layout_c = QHBoxLayout()
        layout_c.addWidget(exit_button)
        layout_c.addWidget(log)

        rem = QCheckBox("Remember me")
        rem.setChecked(True)

        #   adding items to form layout
        layout.setSpacing(10)
        layout.addRow(l_name, self.name_f)
        layout.addRow(l_email, self.email_f)
        layout.addRow(l_password, self.password_f)
        layout.addWidget(rem)
        layout.addItem(layout_c)

        main_layout.addLayout(layout, 0, 0)
        layout.setObjectName("container")
        self.setObjectName("main")
        self.__stylesheet()

    def __stylesheet(self):
        css = """
            #main {
                background-color: #6781A4;
            }
            QLineEdit {
                background-color: #6781BF;
                border-radius: 2px;
                border-top: 0px;
                min-height: 40px;
                font: 16 bold large "MonoSpace";
                border-bottom: 2.5px solid #97ACFF;
            }
            QLineEdit:focus {
                border-bottom: 3.5px solid blue;
            }
            QFormLayout {
                border-top: 0px;
                background-color: red;
            }
        """
        self.setStyleSheet(css)

    def submit(self):
        name = self.name_f.text()
        email = self.email_f.text()
        password = self.password_f.text()
        print(f"Name: {name}\nEmail: {email}\nPassword: {password}")
    
    @staticmethod
    def exit_app():
        sys.exit(0)


app = QApplication(sys.argv)


def main():
    window = Form()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
