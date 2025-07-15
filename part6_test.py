from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGridLayout, QLabel, QFontDialog, QColorDialog # core
from PyQt6.QtCore import Qt # for text alignment
from PyQt6.QtGui import QIcon # for Niko app icon
import os

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(400, 400)
        self.setWindowTitle("I wrote this myself trust me")
        self.setWindowIcon(QIcon(f"{os.getcwd()}/assets/niko_on_a_vacuum.jpg"))

        parentLayout = QGridLayout()

        self.fontLabel = QLabel("Font preview", alignment=Qt.AlignmentFlag.AlignCenter)
        self.fontDialogButton = QPushButton("Change font")
        self.fontDialogButton.clicked.connect(self.fontDialogHandler)
        self.colorDialogButton = QPushButton("Pick a color")
        self.colorDialogButton.clicked.connect(self.colorDialogHandler)

        parentLayout.addWidget(self.fontLabel, 0, 0, 1, 0) # last pair of 1, 0 makes it centered for whatever reason
        parentLayout.addWidget(self.fontDialogButton, 1, 0)
        parentLayout.addWidget(self.colorDialogButton, 1, 1)

        centerWidget = QWidget()
        centerWidget.setLayout(parentLayout)
        self.setCentralWidget(centerWidget)


    def fontDialogHandler(self):
        fontDialog = QFontDialog()

        fontDialogState = fontDialog.exec()
        if fontDialogState:
            print("clicked ok!")
            print(f"changing font to {fontDialog.currentFont().toString()}")
            self.fontLabel.setFont(fontDialog.currentFont())
        else:
            print("cancelled")


    def colorDialogHandler(self):
        colorDialog = QColorDialog()

        colorDialogState = colorDialog.exec()
        if colorDialogState:
            print("clicked ok!")
            print(f"picked color with hex", colorDialog.currentColor().name())
        else:
            print("cancelled")


app = QApplication([])
window = mainWindow()

window.show()
app.exec()
