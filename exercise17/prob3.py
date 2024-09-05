import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from exercise17.prob2 import MessageBoxDisplay


class RobustCalculator(MessageBoxDisplay):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Robust Calculator")

        self.openAction.triggered.connect(self._openFile)

    def _openFile(self):
        path = os.path.dirname(__file__)
        os.chdir(path)
        filename = "result.txt"
        self.filePath = os.path.realpath("result.txt")

        try:
            with open(filename, "r") as results:
                resultText = results.read()
                self.result_label.setText(resultText)
            self.messages = QMessageBox()
            self.messages.setText(f"Reading result to file {self.filePath}")
            self.messages.exec()
            return

        except FileNotFoundError:
            self.messages = QMessageBox()
            self.messages.setText(f"File not found. Please save a file first.")
            self.messages.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RobustCalculator()
    window.show()
    app.exec()
