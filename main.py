from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit, QVBoxLayout, QLabel
from PySide6.QtCore import QSize
import sys # for commandline arguments

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My first window')
        self.label = QLabel("Label")
        self.label2 = QLabel('Label2')
        self.field = QLineEdit()
        self.button = QPushButton('Button')
        self.field.textChanged.connect(self.label2.setText)
        self.button.clicked.connect(self.on_button_click)

        layout = QVBoxLayout()
        layout.addWidget(self.field)
        layout.addWidget(self.label)
        layout.addWidget(self.label2)
        layout.addWidget(self.button)
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def on_button_click(self):
        self.label.setText("Hello")



