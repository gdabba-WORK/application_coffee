from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMainWindow


class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("ui/coffee_main.ui")
        self.ui.show()

