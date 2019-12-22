from PyQt5.QtWidgets import QApplication

from ui.coffee_main import MainUi

if __name__ == "__main__":
    # pool = ConnectionPool.get_instance()
    # connection = pool.get_connection()
    # print(pool, connection)
    app = QApplication([])
    w = MainUi()
    app.exec_()

