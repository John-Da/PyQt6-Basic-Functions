import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QListWidget,
    QLabel,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Input App")
        layout = QVBoxLayout()

        self.boxChoices = QListWidget()
        self.boxChoices.addItems(["Apple", "Banana", "Cherry", "Date", "Elderberry"])
        self.boxChoices.currentTextChanged.connect(self.show_choice)

        self.choiceLabel = QLabel("No item selected")


        layout.addWidget(self.boxChoices)
        layout.addWidget(self.choiceLabel)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def show_choice(self, text):
        
        self.choiceLabel.setText(f"Selected: {text}")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())