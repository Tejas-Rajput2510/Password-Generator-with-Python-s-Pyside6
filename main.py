from pathlib import Path
from PySide6.QtWidgets import (
    QApplication, QCheckBox, QPushButton, QLabel, QLineEdit, QComboBox
)
from PySide6.QtUiTools import QUiLoader
import random

app = QApplication()
loader = QUiLoader()

ui = Path(__file__).parent / "style.ui"
window = loader.load(str(ui))
window.setWindowTitle("Password generator")

#Important global variables
chars_with_both_checked = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()"
char_numbers_only = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
chars_symbols_only = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()"
chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

#Functions
def destroy():
    window.close()

def genpassword():
    password = ""
    if length.currentText() and numbers.isChecked() and symbols.isChecked():
        lengthval = int(length.currentText())
        for i in range(lengthval):
            password += random.choice(chars_with_both_checked)
    elif length.currentText() and numbers.isChecked() and not symbols.isChecked():
        lengthval = int(length.currentText())
        for i in range(lengthval):
            password += random.choice(char_numbers_only)
    elif length.currentText() and not numbers.isChecked() and symbols.isChecked():
        lengthval = int(length.currentText())
        for i in range(lengthval):
            password += random.choice(chars_symbols_only)
    else:
        lengthval = int(length.currentText())
        for i in range(lengthval):
            password += random.choice(chars)
    password_box.setText(password)

#Main
length = window.findChild(QComboBox, "length")
numbers = window.findChild(QCheckBox, "numbers")
symbols = window.findChild(QCheckBox, "symbols")
generate = window.findChild(QPushButton, "generate")
password_box = window.findChild(QLineEdit, "password")

generate.clicked.connect(genpassword)
window.show()
app.exec()