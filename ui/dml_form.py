from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QHeaderView, QTableWidgetItem, QAction, \
    QMessageBox
from skimage.viewer.qt import Qt

from dao.sale_dao import SaleDao


def create_table(table=None, data=None):
    table.setHorizontalHeaderLabels(data)
    # row단위 선택
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    # 테이블 직접 값 입력 불가 설정
    table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    # 균일한 간격으로 열 재배치(Qt Designer에 해당 옵션이 존재하지 않아 코드로 직접 설정)
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    return table


class DMLUi(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("./ui/dml_form.ui")
        self.ui.tab_widget.setCurrentIndex(0)
        self.ui.show()
        self.pro_tbl_widget = create_table(self.ui.pro_tbl_widget, ["code", "name"])
        self.sale_tbl_widget = create_table(self.ui.sale_tbl_widget, ["no", "code", "price", "saleCnt", "marginRate"])
        self.saleDetail_tbl_widget = create_table(self.ui.saleDetail_tbl_widget, ["no", "salePrice", "addTax", "supplyPrice", "marginPrice"])

        # signal & slot
        self.ui.pro_btn_add.clicked.connect(self.add_item)
        self.ui.pro_btn_del.clicked.connect(self.delete_item)
        self.ui.pro_btn_init.clicked.connect(self.init_item)
        self.ui.sale_btn_add.clicked.connect(self.add_item)
        self.ui.sale_btn_del.clicked.connect(self.delete_item)
        self.ui.sale_btn_init.clicked.connect(self.init_item)
        self.ui.saleDetail_btn_add.clicked.connect(self.add_item)
        self.ui.saleDetail_btn_del.clicked.connect(self.delete_item)
        self.ui.saleDetail_btn_init.clicked.connect(self.init_item)

        # 마우스 우클릭시 메뉴
        self.set_context_menu(self.pro_tbl_widget)
        self.set_context_menu(self.sale_tbl_widget)
        self.set_context_menu(self.saleDetail_tbl_widget)

        data_pro = [(1, "마케팅"), (2, "개발"), (3, "인사")]
        data_sale = [(1, 1, 1000, 20, 50), (2, 2, 500, 10, 30), (3, 3, 2000, 50, 10)]
        self.load_data(data_pro, 0)
        self.load_data(data_sale, 1)

    # line edit 초기화
    def init_item(self):
        if self.ui.tab_widget.currentIndex() == 0:
            self.ui.pro_le_code.clear()
            self.ui.pro_le_name.clear()
        elif self.ui.tab_widget.currentIndex() == 1:
            self.ui.sale_le_no.clear()
            self.ui.sale_le_code.clear()
            self.ui.sale_le_price.clear()
            self.ui.sale_le_saleCnt.clear()
            self.ui.sale_le_marginRate.clear()

    # hard coding된 data(원소가 튜플인 리스트)를 tbl_widget에 삽입한다.
    # enumerate(): 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환한다.
    def load_data(self, data, flag):
        if flag == 0:
            for idx, (code, name) in enumerate(data):
                item_code, item_name = self.create_item(code, name)
                print(idx, item_code, item_name)
                nextIdx = self.pro_tbl_widget.rowCount()
                self.pro_tbl_widget.insertRow(nextIdx)
                self.pro_tbl_widget.setItem(nextIdx, 0, item_code)
                self.pro_tbl_widget.setItem(nextIdx, 1, item_name)
        elif flag == 1:
            for idx, (no, code, price, saleCnt, marginRate) in enumerate(data):
                item0, item1, item2, item3, item4 = self.create_item(no, code, price, saleCnt, marginRate)
                print(idx, item0, item1, item2, item3, item4)
                nextIdx = self.sale_tbl_widget.rowCount()
                self.sale_tbl_widget.insertRow(nextIdx)
                self.sale_tbl_widget.setItem(nextIdx, 0, item0)
                self.sale_tbl_widget.setItem(nextIdx, 1, item1)
                self.sale_tbl_widget.setItem(nextIdx, 2, item2)
                self.sale_tbl_widget.setItem(nextIdx, 3, item3)
                self.sale_tbl_widget.setItem(nextIdx, 4, item4)

    # 우클릭 메뉴 생성과 해당 기능별 slot과 connect()한다.
    def set_context_menu(self, tv):
        tv.setContextMenuPolicy(Qt.ActionsContextMenu)
        update_action = QAction("수정", tv)
        delete_action = QAction("삭제(미구현)", tv)
        # todo tbl_widget 우클릭시 삭제 QAction 기능 추가하기
        tv.addAction(update_action)
        tv.addAction(delete_action)
        update_action.triggered.connect(self.__update)
        delete_action.triggered.connect(self.__delete)

    # 우클릭 '수정'선택시 수행되는 기능
    def __update(self):
        # QMessageBox.information(self, 'Update', "확인", QMessageBox.Ok)
        if self.ui.tab_widget.currentIndex() == 0:
            try:
                if self.pro_tbl_widget.selectedIndexes().__len__() > self.pro_tbl_widget.columnCount():
                    raise IndexError('수정은 하나의 행만 가능합니다!')
                selectedItems = self.pro_tbl_widget.selectedItems()
                self.ui.pro_le_code.setText(selectedItems[0].text())
                self.ui.pro_le_name.setText(selectedItems[1].text())
                self.ui.pro_btn_add.setText("수정")
                self.ui.pro_btn_add.clicked.disconnect()
                self.ui.pro_btn_add.clicked.connect(self.update_item)
                self.pro_tbl_widget.setSelectionMode(QAbstractItemView.NoSelection)
            except IndexError as e:
                print(e)

        elif self.ui.tab_widget.currentIndex() == 1:
            try:
                if self.sale_tbl_widget.selectedIndexes().__len__() > self.sale_tbl_widget.columnCount():
                    raise IndexError('수정은 하나의 행만 가능합니다!')
                selectedItems = self.sale_tbl_widget.selectedItems()
                self.ui.sale_le_no.setText(selectedItems[0].text())
                self.ui.sale_le_code.setText(selectedItems[1].text())
                self.ui.sale_le_price.setText(selectedItems[2].text())
                self.ui.sale_le_saleCnt.setText(selectedItems[3].text())
                self.ui.sale_le_marginRate.setText(selectedItems[4].text())
                self.ui.sale_btn_add.setText("수정")
                self.ui.sale_btn_add.clicked.disconnect()
                self.ui.sale_btn_add.clicked.connect(self.update_item)
                self.sale_tbl_widget.setSelectionMode(QAbstractItemView.NoSelection)
            except IndexError as e:
                print(e)

    # todo 재사용필
    # todo 우클릭 삭제는 `191217 미구현...
    def __delete(self):
        pass
        # QMessageBox.information(self, 'Delete', "확인", QMessageBox.Ok)

    # line edit 으로부터 가져온 값들을 create_item()으로 타입을 변환해서 반환
    def get_item_from_le(self):
        if self.ui.tab_widget.currentIndex() == 0:
            code = self.ui.pro_le_code.text()
            name = self.ui.pro_le_name.text()
            return self.create_item(code, name)
        elif self.ui.tab_widget.currentIndex() == 1:
            no = self.ui.sale_le_no.text()
            code = self.ui.sale_le_code.text()
            price = self.ui.sale_le_price.text()
            saleCnt = self.ui.sale_le_saleCnt.text()
            marginRate = self.ui.sale_le_marginRate.text()
            return self.create_item(no, code, price, saleCnt, marginRate)

    # tbl_widget에 들어갈 QTableWidgetItem 객체들을 생성해서 반환한다.
    def create_item(self, *args):
        items = []
        for value in args:
            item = QTableWidgetItem()
            item.setTextAlignment(Qt.AlignCenter)
            item.setData(Qt.DisplayRole, value)
            items.append(item)
        return items

    # line edit 으로부터 가져온 값들을 tbl_widget의 현재행(curruntIdx)에 삽입
    def add_item(self):
        if self.ui.tab_widget.currentIndex() == 0:
            item0, item1 = self.get_item_from_le()
            currentIdx = self.pro_tbl_widget.rowCount()
            self.pro_tbl_widget.insertRow(currentIdx)
            self.pro_tbl_widget.setItem(currentIdx, 0, item0)
            self.pro_tbl_widget.setItem(currentIdx, 1, item1)
        elif self.ui.tab_widget.currentIndex() == 1:
            item0, item1, item2, item3, item4 = self.get_item_from_le()
            currentIdx = self.sale_tbl_widget.rowCount()
            self.sale_tbl_widget.insertRow(currentIdx)
            self.sale_tbl_widget.setItem(currentIdx, 0, item0)
            self.sale_tbl_widget.setItem(currentIdx, 1, item1)
            self.sale_tbl_widget.setItem(currentIdx, 2, item2)
            self.sale_tbl_widget.setItem(currentIdx, 3, item3)
            self.sale_tbl_widget.setItem(currentIdx, 4, item4)
        self.init_item()

    # 우클릭 '수정'으로 '추가'버튼이 '수정'버튼으로 변경/활성화 된 상태에서 수행되는 기능(line edit의 값을 tbl_widget에 반영)
    def update_item(self):
        if self.ui.tab_widget.currentIndex() == 0:
            selectedIndexes = self.pro_tbl_widget.selectedIndexes()
            item0, item1 = self.get_item_from_le()
            self.pro_tbl_widget.setItem(selectedIndexes[0].row(), selectedIndexes[0].column(), item0)
            self.pro_tbl_widget.setItem(selectedIndexes[1].row(), selectedIndexes[1].column(), item1)
            self.ui.pro_btn_add.setText("추가")
            self.ui.pro_btn_add.clicked.disconnect()
            self.ui.pro_btn_add.clicked.connect(self.add_item)
            # self.pro_tbl_widget.setSelectionMode(QAbstractItemView.SingleSelection)
            self.pro_tbl_widget.setSelectionMode(QAbstractItemView.MultiSelection)
        elif self.ui.tab_widget.currentIndex() == 1:
            selectedIndexes = self.sale_tbl_widget.selectedIndexes()
            item0, item1, item2, item3, item4 = self.get_item_from_le()
            self.sale_tbl_widget.setItem(selectedIndexes[0].row(), selectedIndexes[0].column(), item0)
            self.sale_tbl_widget.setItem(selectedIndexes[1].row(), selectedIndexes[1].column(), item1)
            self.sale_tbl_widget.setItem(selectedIndexes[2].row(), selectedIndexes[2].column(), item2)
            self.sale_tbl_widget.setItem(selectedIndexes[3].row(), selectedIndexes[3].column(), item3)
            self.sale_tbl_widget.setItem(selectedIndexes[4].row(), selectedIndexes[4].column(), item4)
            self.ui.sale_btn_add.setText("추가")
            self.ui.sale_btn_add.clicked.disconnect()
            self.ui.sale_btn_add.clicked.connect(self.add_item)
            # self.sale_tbl_widget.setSelectionMode(QAbstractItemView.SingleSelection)
            self.sale_tbl_widget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.init_item()

    # 클릭으로 선택된 row '삭제'버튼으로 삭제
    def delete_item(self):
        if self.ui.tab_widget.currentIndex() == 0:
            try:
                indexList = self.pro_tbl_widget.selectedIndexes()
                for index in indexList:
                    self.pro_tbl_widget.removeRow(index.row())
            except IndexError as e:
                print(e)
        elif self.ui.tab_widget.currentIndex() == 1:
            try:
                indexList = self.sale_tbl_widget.selectedIndexes()
                for index in indexList:
                    self.pro_tbl_widget.removeRow(index.row())
            except IndexError as e:
                print(e)
