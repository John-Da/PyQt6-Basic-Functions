import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from exercise17.prob1 import EnhancedCalculator


class MessageBoxDisplay(EnhancedCalculator):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator with Message Box")

        self.fNum_input.returnPressed.connect(self._firstInput)
        self.lNum_input.returnPressed.connect(self._secondInput)

    def _firstInput(self):
        try:
            fmsg = "Please enter the first number"
            float(self.fNum_input.text())
        except:
            self.messages = QMessageBox()
            self.messages.setText(f"{fmsg}")
            self.messages.exec()

    def _secondInput(self):
        try:
            smsg = "Please enter the second number"
            float(self.lNum_input.text())
        except:
            self.messages = QMessageBox()
            self.messages.setText(f"{smsg}")
            self.messages.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MessageBoxDisplay()
    window.show()
    app.exec()
