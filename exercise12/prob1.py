from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(QSize(500, 200))

        self.label = QLabel()
        font = self.label.font()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("background:yellow; color:black;")

        self.input = QLineEdit()
        self.input.textChanged.connect(self.change_Text)

        self.listWidget = QListWidget()
        self.listWidget.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        itemlist = ["EN842300", "EN842314", "EN842315"]
        for i in range(len(itemlist)):
            items = QListWidgetItem(itemlist[i])
            self.listWidget.addItem(items)
        self.listWidget.itemClicked.connect(self.printItemText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.listWidget)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def change_Text(self):

        inputtext = self.input.text()
        hello = f"Hello {inputtext}!"
        return self.label.setText(hello)

    def printItemText(self):
        inputtext = self.input.text()
        items = self.listWidget.selectedItems()
        x = []
        for i in range(len(items)):
            x.append(str(self.listWidget.selectedItems()[i].text()))
        return self.label.setText(
            f'Hello {inputtext}! You are interested in these courses {",".join(map(str, x))}'
        )


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
