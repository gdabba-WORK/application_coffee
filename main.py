from PyQt5.QtWidgets import QApplication

from dao.product_dao import ProductDao
from dao.saleDetail_dao import SaleDetailDao
from dao.sale_dao import SaleDao
from db_connection.connection_pool import ConnectionPool
from ui.coffee_main import MainUi
from ui.dml_form import DMLUi

if __name__ == "__main__":
    # pool = ConnectionPool.get_instance()
    # connection = pool.get_connection()
    # print(pool, connection)
    app = QApplication([])
    w = MainUi()
    app.exec_()