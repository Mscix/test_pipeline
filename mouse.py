from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit, QVBoxLayout, QLabel
from PySide6.QtCore import QSize
from pytestqt.qtbot import QtBot
import sys # for commandline arguments

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Click here")
        self.setCentralWidget(self.label)
        self.show()

    def mousePressEvent(self, event):
        print("Mischa hat unlimited swag")
        print(event.pos())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

