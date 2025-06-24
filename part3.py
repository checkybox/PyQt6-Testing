from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, \
                            QPushButton, QVBoxLayout, QLineEdit, QComboBox, \
                            QSpinBox, QDoubleSpinBox, QRadioButton, QButtonGroup
from PyQt6.QtGui import QIcon
import os

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(400,150)

        parentLayout = QVBoxLayout()
        self.buttonGroup = QButtonGroup()

        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("Enter your third name")
        self.lineEdit.setMaxLength(13)
        ## Uncomment the line below to see live changes to the text field
        #self.lineEdit.textChanged.connect(self.liveTextChangedHandler)

        # QPushButton (just a button)
        self.button = QPushButton("Click me")
        self.button.clicked.connect(self.clickHandler)

        # QRadioButton (on/off circle)
        self.radioButtonRed = QRadioButton("Red")
        self.radioButtonYellow = QRadioButton("Yellow")
        self.radioButtonBlue = QRadioButton("Blue")

        # Adding QRadioButton instances to QButtonGroup
        self.buttonGroup.addButton(self.radioButtonRed)
        self.buttonGroup.addButton(self.radioButtonYellow)
        self.buttonGroup.addButton(self.radioButtonBlue)
        self.buttonGroup.objectNameChanged.connect(self.buttonGroupHandler)

        # QSpinBox (integers)
        self.spinBox = QSpinBox()
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(99)
        self.spinBox.setSingleStep(2)

        # QDoubleSpinBox (floating point numbers)
        self.doubleSpinBox = QDoubleSpinBox()
        self.doubleSpinBox.setMinimum(0.71)
        self.doubleSpinBox.setMaximum(5.56)
        self.doubleSpinBox.setSingleStep(0.37)

        # QComboBox (drop-down menu of choices)
        self.comboBox = QComboBox()
        self.comboBox.addItem("Red")
        self.comboBox.addItem("Yellow")
        self.comboBox.addItem("Blue")
        self.comboBox.addItem(QIcon(f"{os.getcwd()}/assets/qt_icon.png"), "PyQt6")
        self.comboBox.currentTextChanged.connect(self.comboBoxHandler)

        parentLayout.addWidget(self.lineEdit)
        parentLayout.addWidget(self.comboBox)
        parentLayout.addWidget(self.spinBox)
        parentLayout.addWidget(self.doubleSpinBox)
        parentLayout.addWidget(self.button)
        parentLayout.addWidget(self.radioButtonRed)
        parentLayout.addWidget(self.radioButtonYellow)
        parentLayout.addWidget(self.radioButtonBlue)

        centerWidget = QWidget()
        centerWidget.setLayout(parentLayout)
        self.setCentralWidget(centerWidget)

    def clickHandler(self):
        print("clickHandler method debug output:")
        print("Button clicked!")
        print("QLineEdit text:", self.lineEdit.text())
        #comboBox handler (old)
        #print(self.comboBox.currentText())
        print("QSpinBox value:", self.spinBox.value())
        # Breaks when nothing is selected
        print("QButtonGroup checked value:", self.buttonGroup.checkedButton().text())

    def liveTextChangedHandler(self):
        print(self.lineEdit.text())

    def comboBoxHandler(self, currentText):
        print(currentText)

    # currently broken
    def buttonGroupHandler(self):
        if self.buttonGroup.checkedButton() == None:
            print("None")
        else:
            print(self.buttonGroup.checkedButton().text())

    # this one too 
    def buttonGroupHandler2(self):
        try:
            print(self.buttonGroup.checkedButton().text())
        except:
            print(self.buttonGroup.checkedButton())


app = QApplication([])
window = Window()

window.show()
app.exec()