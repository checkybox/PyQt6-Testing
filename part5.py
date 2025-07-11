from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QInputDialog

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(400, 400)
        self.button = QPushButton("Open Dialog")
        self.setCentralWidget(self.button)

        self.button.clicked.connect(self.clickHandler)

    def clickHandler(self):
        dialog = QInputDialog()
        dialog.setLabelText("Enter your age: ")
        dialog.setInputMode(QInputDialog.InputMode.IntInput)

        clickedButton = dialog.exec()

        if clickedButton:
            print(dialog.intValue())
        else:
            print("nah")

        print(dialog.textValue())

app = QApplication([])
window = Window()

window.show()
app.exec()