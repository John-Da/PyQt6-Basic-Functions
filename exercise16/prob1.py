import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from exercise14.prob2 import MainWindow


class WindowsMenusToolBar(MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator with Menus and Toolbar")
        self.resize(400, 200)

        self._createActions()
        self._createToolBars()
        self._addMenus()

    def _createActions(self):
        path = os.path.dirname(__file__)
        os.chdir(path)

        self.newIcon = QAction(QIcon("images/file-open.svg"), "Open", self)
        self.saveIcon = QAction(QIcon("images/file-save.png"), "Save", self)
        self.clearIcon = QAction(QIcon("images/edit-clear.png"), "Clear", self)

    def _createToolBars(self):
        fileToolBar = self.addToolBar("File")
        fileToolBar.addAction(self.newIcon)
        fileToolBar.addAction(self.saveIcon)
        fileToolBar.addAction(self.clearIcon)

    def _createFileTB(self):
        self.openToolBar = self.addToolBar("Open")
        self.saveToolBar = self.addToolBar("Save")
        self.exitToolBar = self.addToolBar("Exit")

    def _addMenus(self):
        self._addFileMenu()
        self._addEditMenu()
        self._addHelpMenu()

    def _addFileMenu(self):
        path = os.path.dirname(__file__)
        os.chdir(path)
        self.openAction = QAction(QIcon("images/file-open.svg"), "Open", self)
        self.saveAction = QAction(QIcon("images/file-save.png"), "Save", self)
        self.exitAction = QAction("Exit", self)

        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addAction(self.exitAction)

    def _addEditMenu(self):
        path = os.path.dirname(__file__)
        os.chdir(path)
        self.clearAction = QAction(QIcon("images/edit-clear.png"), "Clear", self)

        self.copyAction = QAction("Copy", self)
        self.pasteAction = QAction("Paste", self)
        self.cutAction = QAction("Cut", self)
        self.editMenu.addAction(self.clearAction)
        self.editMenu.addAction(self.copyAction)
        self.editMenu.addAction(self.pasteAction)
        self.editMenu.addAction(self.cutAction)

    def _addHelpMenu(self):
        self.colorAction = QAction("Color", self)
        self.sizeAction = QAction("Size", self)
        self.configMenu.addAction(self.colorAction)
        self.configMenu.addAction(self.sizeAction)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WindowsMenusToolBar()
    window.show()
    app.exec()
