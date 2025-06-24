# import necessary things
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QLineEdit, QGridLayout
from PyQt6.QtCore import Qt

# this is needed
app = QApplication([])
window = QMainWindow()

window.setMinimumSize(400, 400)
window.setWindowTitle("Submission form")

parent_layout = QGridLayout()

login_label = QLabel("Login", alignment=Qt.AlignmentFlag.AlignCenter)
login_label.setMaximumHeight(100)
email_label = QLabel("Email: ")
email_input = QLineEdit()
password_label = QLabel("Password: ")
password_input = QLineEdit()
password_input.setEchoMode(QLineEdit.EchoMode.Password)
submit_button = QPushButton("Sumbit")

parent_layout.addWidget(login_label, 0, 0, 1, 2)
parent_layout.addWidget(email_label, 1, 0)
parent_layout.addWidget(email_input, 1, 1)
parent_layout.addWidget(password_label, 2, 0)
parent_layout.addWidget(password_input, 2, 1)
parent_layout.addWidget(submit_button, 3, 0, 1, 2)

# without this there will be nothing on display
central_widget = QWidget()
central_widget.setLayout(parent_layout)
window.setCentralWidget(central_widget)

# this is needed too
window.show()
app.exec()