from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Name Form")
        self.setFixedSize(QSize(600, 200))

        self.label1 = QLabel("First Name:")
        font = self.label1.font()
        font.setPointSize(20)
        self.label1.setFont(font)

        self.label2 = QLabel("Last Name:")
        font = self.label2.font()
        font.setPointSize(20)
        self.label2.setFont(font)

        self.input1 = QLineEdit()

        self.input2 = QLineEdit()

        self.cancel = QPushButton("Cancel")
        font = self.cancel.font()
        font.setPointSize(20)
        self.cancel.setFont(font)
        self.cancel.setStyleSheet("color:red;")
        self.submit = QPushButton("Submit")
        font = self.submit.font()
        font.setPointSize(20)
        self.submit.setFont(font)
        self.submit.setStyleSheet("color:green;")

        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.input1, 0, 3)
        layout.addWidget(self.input2, 1, 3)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.cancel)
        button_layout.addWidget(self.submit)

        overall = QVBoxLayout()
        overall.addLayout(layout)
        overall.addLayout(button_layout)

        container = QWidget()
        container.setLayout(overall)

        self.setCentralWidget(container)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
