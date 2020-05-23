import sys

from PyQt5.QtWidgets import *


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form")
        self.setGeometry(50, 50, 300, 300)
        self.setMinimumSize(200, 200)
        self.setMaximumSize(300, 300)
        layout = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(layout)

        name_box = QBoxLayout(QBoxLayout.LeftToRight)
        email_box = QBoxLayout(QBoxLayout.LeftToRight)
        password_box = QBoxLayout(QBoxLayout.LeftToRight)
        sex_box = QBoxLayout(QBoxLayout.LeftToRight)
        control_box = QBoxLayout(QBoxLayout.LeftToRight)

        l_name = QLabel("Name:    ")
        self.name_f = QLineEdit()
        self.name_f.setPlaceholderText("Type your name")
        self.name_f.setMaxLength(20)

        l_email = QLabel("Email:   ")
        self.email_f = QLineEdit()
        self.email_f.setPlaceholderText("Type your email")
        self.email_f.setMaxLength(30)

        l_password = QLabel("Password:")
        self.password_f = QLineEdit()
        self.password_f.setEchoMode(QLineEdit.Password)
        self.password_f.setPlaceholderText("Type your password")
        self.password_f.setMaxLength(15)

        male = QRadioButton("Male")
        male.gender = "Male"
        male.setChecked(True)
        female = QRadioButton("Female")
        female.gender = "Female"

        log = QPushButton("Log In")
        log.clicked.connect(self.submit)
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.exit_app)

        name_box.addWidget(l_name, 0)
        name_box.addWidget(self.name_f, 0)

        email_box.addWidget(l_email, 0)
        email_box.addWidget(self.email_f, 0)

        password_box.addWidget(l_password, 0)
        password_box.addWidget(self.password_f, 0)

        sex_box.addWidget(male, 0)
        sex_box.addWidget(female, 0)

        control_box.addWidget(log, 0)
        control_box.addWidget(exit_button, 0)

        remember = QBoxLayout(QBoxLayout.LeftToRight)
        rem = QCheckBox("Remember me")
        rem.setChecked(True)
        remember.addWidget(rem, 0)

        layout.addLayout(name_box)
        layout.addLayout(email_box)
        layout.addLayout(password_box)
        layout.addLayout(sex_box)
        layout.addLayout(remember)
        layout.addLayout(control_box)

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
