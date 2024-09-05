import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from exercise16.prob1 import WindowsMenusToolBar


class ActionConfiguration(WindowsMenusToolBar):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator with Status and Shortcuts")

        self._createShortcuts()
        self.statusbar = self.statusBar()
        self.statusbar.showMessage("Ready", 3000)

        self.newIcon.setStatusTip("Open a file")
        self.saveIcon.setStatusTip("Save a file")
        self.clearIcon.setStatusTip("Clear the result")

        self.openAction.triggered.connect(self._openStatus)
        self.saveAction.triggered.connect(self._saveStatus)
        self.exitAction.triggered.connect(self._exitStatus)
        self.clearAction.triggered.connect(self._clearStatus)
        self.copyAction.triggered.connect(self._copyStatus)
        self.pasteAction.triggered.connect(self._pasteStatus)
        self.cutAction.triggered.connect(self._cutStatus)
        self.colorAction.triggered.connect(self._colorStatus)
        self.sizeAction.triggered.connect(self._sizeStatus)

    def _createShortcuts(self):
        self.openAction.setShortcut(QKeySequence("Ctrl+O"))
        self.saveAction.setShortcut(QKeySequence("Ctrl+S"))
        self.exitAction.setShortcut(QKeySequence("Ctrl+Q"))
        self.clearAction.setShortcut(QKeySequence("Ctrl+R"))

    def _openStatus(self):
        self.statusbar.showMessage("Open a file", 1000)

    def _saveStatus(self):
        self.statusbar.showMessage("Save a file", 1000)

    def _exitStatus(self):
        self.statusbar.showMessage("Exit the application", 1000)

    def _clearStatus(self):
        self.statusbar.showMessage("Clear the result", 1000)

    def _copyStatus(self):
        self.statusbar.showMessage("Copy", 1000)

    def _pasteStatus(self):
        self.statusbar.showMessage("Paste", 1000)

    def _cutStatus(self):
        self.statusbar.showMessage("Cut", 1000)

    def _colorStatus(self):
        self.statusbar.showMessage("Text Color", 1000)

    def _sizeStatus(self):
        self.statusbar.showMessage("Text Size", 1000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ActionConfiguration()
    window.show()
    app.exec()
