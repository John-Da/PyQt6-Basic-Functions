from argparse import Action
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Context Menu Font Style")
        self.setFixedSize(QSize(500, 200))

        self.label = QLabel()


        self.comboList = QComboBox()
        self.comboList.addItems(['Bold', 'Italic'])
        self.comboList.currentTextChanged.connect(self.menupopup)


        layout = QVBoxLayout()
        # layout.addWidget(self.label)
        layout.addWidget(self.checklist1)
        layout.addWidget(self.comboList)


        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def menupopup(self, item):
        context = QMenu(self)
        context.addAction(Action('Bold', self))
        context.addAction(Action('Italic', self))
        context.triggered.connect(self.menu_choice)
        context.exec(e.globalPos())

    def menu_choice(self, action):
        if action == 'Bold':
            ...
        else:
            ...
        


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
