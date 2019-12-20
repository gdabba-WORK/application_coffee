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

    # pdt = ProductDao()
    # pdt.insert_product()
    # pdt.delete_product()
    # pdt.select()
    # pdt.update_product()

    #
    # dao = SaleDao()
    # dao.select_item()
    # dao.insert_item('D001', 3333, 100, 5)
    # dao.update_item('D001', 4444, 50, 50, 6)
    # dao.delete_item(6)
    # dao.myPrint()

    # app = QApplication([])
    # w = MainUi()
    # app.exec_()

    saleDao = SaleDao()
    saleDao.select_item()

    productDao = ProductDao()
    productDao.select_item()

    saledetailDao = SaleDetailDao()
    saledetailDao.select_item()