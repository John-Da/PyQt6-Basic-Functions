from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from prob3 import MainWidow


class EnhanceNoteApp(MainWidow):
    def __init__(self):
        super().__init__()

        self.inputList = []
        self.saveBtn.clicked.connect(self.addInputText)

    def addInputText(self):
        self.inputList.append(self.inputInput.text())
        self.textInput.setText('\n'.join(map(str, self.inputList)))
        self.clear_inputs()


    def clear_inputs(self):
        self.inputInput.clear()



if __name__ == "__main__":
    EnhanceNoteApp()