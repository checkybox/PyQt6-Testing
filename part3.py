from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QVBoxLayout, QLineEdit, QComboBox
from PyQt6.QtGui import QIcon
import os

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(400,150)

        parentLayout = QVBoxLayout()

        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("Enter your third name")
        self.lineEdit.setMaxLength(13)
        self.lineEdit.textChanged.connect(self.textChangedHandler)

        self.button = QPushButton("Click me")
        self.button.clicked.connect(self.clickHandler)

        self.comboBox = QComboBox()
        self.comboBox.addItem("Red")
        self.comboBox.addItem("Yellow")
        self.comboBox.addItem("Blue")
        self.comboBox.addItem(QIcon(f"{os.getcwd()}/assets/qt_icon.png"), "PyQt6")
        self.comboBox.currentTextChanged.connect(self.comboBoxHandler)

        parentLayout.addWidget(self.lineEdit)
        parentLayout.addWidget(self.comboBox)
        parentLayout.addWidget(self.button)

        centerWidget = QWidget()
        centerWidget.setLayout(parentLayout)
        self.setCentralWidget(centerWidget)

    def clickHandler(self):
        print("Button clicked!")
        #self.label.setText("FUCK YOU")
        print(self.lineEdit.text())
        #comboBox handler (old)
        #print(self.comboBox.currentText())

    def textChangedHandler(self):
        print(self.lineEdit.text())

    def comboBoxHandler(self, currentText):
        print(currentText)


app = QApplication([])
window = Window()

window.show()
app.exec()