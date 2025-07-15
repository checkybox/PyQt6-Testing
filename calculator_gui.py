import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QPushButton, QLineEdit, QLabel
from PyQt6.QtGui import QIcon, QIntValidator
from PyQt6.QtCore import Qt

from calculator_base import sum, diff, mul, div

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator 2")
        self.setWindowIcon(QIcon(f"{os.getcwd()}/assets/niko_on_a_vacuum.jpg"))
        self.setMinimumSize(350, 350)

        parentLayout = QGridLayout()
        
        self.firstLine = QLineEdit()
        self.firstLine.setPlaceholderText("First number: ")
        self.firstLine.setValidator(QIntValidator())
        self.secondLine = QLineEdit()
        self.secondLine.setPlaceholderText("Second number: ")
        self.secondLine.setValidator(QIntValidator())
        self.result = QLabel("Result: ")

        self.button = QPushButton("Click me and see")
        self.button.clicked.connect(self.calculateClickHandler)

        parentLayout.addWidget(self.firstLine, 0, 0)
        parentLayout.addWidget(self.secondLine, 0, 1)
        parentLayout.addWidget(self.result, 1, 0, 1, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
        parentLayout.addWidget(self.button, 2, 0, 1, 0)

        centralWidget = QWidget()
        centralWidget.setLayout(parentLayout)
        self.setCentralWidget(centralWidget)

    def calculateClickHandler(self):
        self.firstNumber = int(self.firstLine.text())
        self.secondNumber = int(self.secondLine.text())
        result = sum(self.firstNumber, self.secondNumber)
        self.result.setText(f"Result: {result}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()