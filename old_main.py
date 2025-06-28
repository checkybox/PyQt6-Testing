from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
import os

app = QApplication([])
window = QMainWindow()

# Setting up window properties

window.setMinimumSize(400,300)
window.setWindowTitle("Welcome to Qt!")
#window.setWindowIcon(QIcon(f"{os.getcwd()}/assets/qt_icon.png"))

# Adding widgets

# label = QLabel("Some text here", alignment=Qt.AlignmentFlag.AlignCenter)
# font = window.font() # get a font object
# font.setPointSize(18) # change font size
# font.setBold(True) # make font bold
# label.setFont(font) # assign font to a label

# button = QPushButton("Click Me")
# font = window.font()
# font.setPointSize(36)
# font.setBold(True)
# button.setFont(font)
# window.setCentralWidget(button) # make button centered

# parentLayout = QVBoxLayout()

# buttonLayout = QHBoxLayout()

# button1 = QPushButton("Click Me!")
# button2 = QPushButton("Don't click...")
# buttonLayout.addWidget(button1)
# buttonLayout.addWidget(button2)

# parentLayout.addLayout(buttonLayout)

# label = QLabel("Sample Text")
# parentLayout.addWidget(label)

# centerWidget = QWidget()
# centerWidget.setLayout(parentLayout)

# window.setCentralWidget(centerWidget)

parentLayout = QGridLayout()

label1 = QLabel("This is button 1.", alignment=Qt.AlignmentFlag.AlignCenter)
# label2 = QLabel("This is button 2.", alignment=Qt.AlignmentFlag.AlignCenter)
parentLayout.addWidget(label1, 0, 0, 1, 2)
# parentLayout.addWidget(label2,0,1)

button1 = QPushButton("Button 1")
button2 = QPushButton("Button 2")
parentLayout.addWidget(button1, 1, 0)
parentLayout.addWidget(button2, 1, 1)
parentLayout.setRowMinimumHeight(1, 50)

centerWidget = QWidget()
centerWidget.setLayout(parentLayout)

window.setCentralWidget(centerWidget)

window.show()
app.exec()