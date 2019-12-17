from PyQt5.QtWidgets import QApplication, QWidget

from dao.sale_dao import SaleDao
from ui.dml_form import DMLUI


class NameErrorr(BaseException):
    pass


def my_exception_handle():
    try:
        print("try()")
        raise NameErrorr
        print("try() end")
    except NameErrorr:
        print(NameErrorr)
    finally:
        print("finally()")


if __name__ == "__main__":
    # pool = ConnectionPool.get_instance()
    # connection = pool.get_connection()
    # print(pool, connection)

    # pdt = ProductDao()
    # pdt.insert_product()
    # pdt.delete_product()
    # pdt.select()
    # pdt.update_product()

    # my_exception_handle()
    # dao = SaleDao()
    # dao.select_item()
    # dao.insert_item('D001', 3333, 100, 5)
    # dao.update_item('D001', 4444, 50, 50, 6)
    # dao.delete_item(6)
    # dao.myPrint()

    #PyUIC5로 생성한 클래스 사용방법
    # widget = QWidget()
    # w = Ui_dml_widget()
    # w.setupUi(widget)
    # w.retranslateUi(widget)
    # widget.show()

    app = QApplication([])
    w = DMLUI()
    app.exec_()