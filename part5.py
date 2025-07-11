from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFontDialog, QLabel, QVBoxLayout, QWidget

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(200, 200)

        parentLayout = QVBoxLayout()

        self.label = QLabel("This is a label")
        self.button = QPushButton("Open Dialog")
        parentLayout.addWidget(self.label)
        parentLayout.addWidget(self.button)

        centerWidget = QWidget()
        centerWidget.setLayout(parentLayout)
        self.setCentralWidget(centerWidget)

        self.button.clicked.connect(self.clickHandler)

    def clickHandler(self):
        dialog = QFontDialog()

        clickedOk = dialog.exec()
        if clickedOk:
            self.label.setFont(dialog.currentFont())
            print("Changed font!")
            print(dialog.currentFont().family())
        else:
            print("Discarded")


app = QApplication([])
window = Window()

window.show()
app.exec()