from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QAbstractItemView, QHeaderView, QTableWidgetItem, QAction, \
    QMessageBox
from skimage.viewer.qt import Qt

from dao.sale_dao import SaleDao


def create_table(table = None, data = None):
    table.setHorizontalHeaderLabels(data)
    # row단위 선택
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    # 테이블 직접 값 입력 불가 설정
    table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    # 균일한 간격으로 열 재배치(Qt Designer에 해당 옵션이 존재하지 않아 코드로 직접 설정)
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    return table


class DMLUI(QWidget):
    def __init__(self):
        super().__init__()

        dao = SaleDao()
        self.ui = uic.loadUi("./ui/dml_form.ui")
        self.ui.stk_widget.setCurrentIndex(1)
        self.ui.show()
        self.pro_tbl_widget = create_table(self.ui.pro_tbl_widget, ["code", "name"])
        self.sale_tbl_widget = create_table(self.ui.sale_tbl_widget, ["no", "code", "price", "saleCnt", "marginRate"])

        # # signal & slot
        # self.ui.btn_add.clicked.connect(self.add_item)
        # # self.ui.btn_update.clicked.connect(self.update_item)
        # self.ui.btn_del.clicked.connect(self.delete_item)
        # self.ui.btn_init.clicked.connect(self.init_item)
        #
        # # 마우스 우클릭시 메뉴
        # self.set_context_menu(self.tbl_widget)
        #
        # data = [(1, "마케팅", 8), (2, "개발", 10), (3, "인사", 20)]
        # self.load_data(data)

    # enumerate(): 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환한다.
    def load_data(self, data):
        for idx, (no, name, floor) in enumerate(data):
            item_no, item_name, item_floor = self.create_item(no, name, floor)
            print(idx, item_no, item_name, item_floor)
            nextIdx = self.tbl_widget.rowCount()
            self.tbl_widget.insertRow(nextIdx)
            self.tbl_widget.setItem(nextIdx, 0, item_no)
            self.tbl_widget.setItem(nextIdx, 1, item_name)
            self.tbl_widget.setItem(nextIdx, 2, item_floor)

    def set_context_menu(self, tv):
        tv.setContextMenuPolicy(Qt.ActionsContextMenu)
        update_action = QAction("수정", tv)
        delete_action = QAction("삭제(미구현)", tv)
        # todo tbl_widget 우클릭시 삭제 QAction 기능 추가하기
        tv.addAction(update_action)
        tv.addAction(delete_action)
        update_action.triggered.connect(self.__update)
        delete_action.triggered.connect(self.__delete)

    def __update(self):
        # QMessageBox.information(self, 'Update', "확인", QMessageBox.Ok)
        selectedItems = self.tbl_widget.selectedItems()
        self.ui.le_no.setText(selectedItems[0].text())
        self.ui.le_name.setText(selectedItems[1].text())
        self.ui.le_floor.setText(selectedItems[2].text())
        self.ui.btn_add.setText("수정")
        self.ui.btn_add.clicked.disconnect()
        self.ui.btn_add.clicked.connect(self.update_item)

        self.tbl_widget.setSelectionMode(QAbstractItemView.NoSelection)

    def __delete(self):
        QMessageBox.information(self, 'Delete', "확인", QMessageBox.Ok)

    def add_item(self):
        item_no, item_name, item_floor = self.get_item_from_le()
        currentIdx = self.tbl_widget.rowCount()
        self.tbl_widget.insertRow(currentIdx)
        self.tbl_widget.setItem(currentIdx, 0, item_no)
        self.tbl_widget.setItem(currentIdx, 1, item_name)
        self.tbl_widget.setItem(currentIdx, 2, item_floor)
        self.init_item()

    def get_item_from_le(self):
        no = self.ui.le_no.text()
        name = self.ui.le_name.text()
        floor = self.ui.le_floor.text()

        item_no, item_name, item_floor = self.create_item(no, name, floor)

        return item_no, item_name, item_floor

    def create_item(self, no, name, floor):
        item_no = QTableWidgetItem()
        item_no.setTextAlignment(Qt.AlignCenter)
        item_no.setData(Qt.DisplayRole, no)
        item_name = QTableWidgetItem()
        item_name.setTextAlignment(Qt.AlignCenter)
        item_name.setData(Qt.DisplayRole, name)
        item_floor = QTableWidgetItem()
        item_floor.setTextAlignment(Qt.AlignCenter)
        item_floor.setData(Qt.DisplayRole, floor)
        return item_no, item_name, item_floor

    def update_item(self):
        selectedIndexes = self.tbl_widget.selectedIndexes()
        item_no, item_name, item_floor = self.get_item_from_le()

        self.tbl_widget.setItem(selectedIndexes[0].row(), 0, item_no)
        self.tbl_widget.setItem(selectedIndexes[1].row(), 1, item_name)
        self.tbl_widget.setItem(selectedIndexes[2].row(), 2, item_floor)

        self.ui.btn_add.setText("추가")
        self.ui.btn_add.clicked.disconnect()
        self.ui.btn_add.clicked.connect(self.add_item)

        self.tbl_widget.setSelectionMode(QAbstractItemView.SingleSelection)

        self.init_item()

    def delete_item(self):
        selectionIdxs = self.tbl_widget.selectedIndexes()[0]
        print(selectionIdxs)
        self.tbl_widget.removeRow(selectionIdxs.row())

    def init_item(self):
        self.ui.le_no.clear()
        self.ui.le_name.clear()
        self.ui.le_floor.clear()