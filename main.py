from design import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.clickHandler)
    
    def clickHandler(self):
        print("Clicked!")
        entered_task = self.lineEdit.text() # Get text from lineEdit
        if entered_task.strip() != "": # Check if lineEdit is not empty
            self.listWidget.addItem(entered_task) # Submits a task
            self.lineEdit.setText("") # Clears the lineEdit widget after submitting a task

app = QApplication([])
window = Window()

window.show()
app.exec()