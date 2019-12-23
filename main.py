from PyQt5.QtWidgets import QApplication

from ui.coffee_main import MainUi

if __name__ == "__main__":
    app = QApplication([])
    w = MainUi()
    app.exec_()

