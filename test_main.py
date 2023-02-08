import pytest
from time import sleep
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit, QVBoxLayout, QLabel
from PySide6.QtCore import QSize, Qt
from pytestqt.qtbot import QtBot
from PySide6.QtTest import QTest


from main import MainWindow

def test_button_click(qtbot):
    app = MainWindow()
    qtbot.addWidget(app)
    app.show()
    qtbot.waitForWindowShown(app)
    app.close()
    assert app.label.text() == "Label"
    qtbot.mouseClick(app.button, Qt.LeftButton)
    assert app.label.text() == "Hello"



