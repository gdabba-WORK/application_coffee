# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dml_form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QHeaderView, QAction, QTableWidgetItem, QMessageBox
from skimage.viewer.qt import Qt

from dao.product_dao import ProductDao
from dao.saleDetail_dao import SaleDetailDao
from dao.sale_dao import SaleDao


def set_table(table=None, data=None):
    table.setHorizontalHeaderLabels(data)
    # row단위 선택
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    # 테이블 직접 값 입력 불가 설정
    table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    # 균일한 간격으로 열 재배치(Qt Designer에 해당 옵션이 존재하지 않아 코드로 직접 설정)
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


class DMLUi(QWidget):
    closeSignal = pyqtSignal()
    pDao = ProductDao()
    sDao = SaleDao()
    sdDao = SaleDetailDao()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)

        set_table(self.pro_tbl_widget, ["code", "name"])
        set_table(self.sale_tbl_widget, ["no", "code", "price", "saleCnt", "marginRate"])
        set_table(self.saleDetail_tbl_widget, ["no", "salePrice", "addTax", "supplyPrice", "marginPrice"])

        self.tab_widget.setCurrentIndex(0)

        # signal & slot
        self.pro_btn_add.clicked.connect(self.add_item)
        self.pro_btn_del.clicked.connect(self.delete_item)
        self.pro_btn_init.clicked.connect(self.init_item)
        self.sale_btn_add.clicked.connect(self.add_item)
        self.sale_btn_del.clicked.connect(self.delete_item)
        self.sale_btn_init.clicked.connect(self.init_item)
        self.saleDetail_btn_add.clicked.connect(self.add_item)
        self.saleDetail_btn_del.clicked.connect(self.delete_item)
        self.saleDetail_btn_init.clicked.connect(self.init_item)

        # 마우스 우클릭시 메뉴
        self.set_context_menu(self.pro_tbl_widget)
        self.set_context_menu(self.sale_tbl_widget)
        self.set_context_menu(self.saleDetail_tbl_widget)
        self.load_data_from_db()

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

    # tbl_widget에 들어갈 QTableWidgetItem 객체들을 생성해서 반환한다.
    def create_item(self, *args):
        items = []
        for value in args:
            item = QTableWidgetItem()
            item.setTextAlignment(Qt.AlignCenter)
            item.setData(Qt.DisplayRole, value)
            items.append(item)
        return items

    # enumerate(): 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환한다.
    def load_data(self, data, flag):
        if flag == 0:
            [self.pro_tbl_widget.removeRow(0) for _ in range(self.pro_tbl_widget.rowCount())]
            for idx, (code, name) in enumerate(data):
                item_code, item_name = self.create_item(code, name)
                nextIdx = self.pro_tbl_widget.rowCount()
                self.pro_tbl_widget.insertRow(nextIdx)
                self.pro_tbl_widget.setItem(nextIdx, 0, item_code)
                self.pro_tbl_widget.setItem(nextIdx, 1, item_name)
        elif flag == 1:
            [self.sale_tbl_widget.removeRow(0) for _ in range(self.sale_tbl_widget.rowCount())]
            for idx, (no, code, price, saleCnt, marginRate) in enumerate(data):
                item0, item1, item2, item3, item4 = self.create_item(no, code, price, saleCnt, marginRate)
                nextIdx = self.sale_tbl_widget.rowCount()
                self.sale_tbl_widget.insertRow(nextIdx)
                self.sale_tbl_widget.setItem(nextIdx, 0, item0)
                self.sale_tbl_widget.setItem(nextIdx, 1, item1)
                self.sale_tbl_widget.setItem(nextIdx, 2, item2)
                self.sale_tbl_widget.setItem(nextIdx, 3, item3)
                self.sale_tbl_widget.setItem(nextIdx, 4, item4)
        elif flag == 2:
            [self.saleDetail_tbl_widget.removeRow(0) for _ in range(self.saleDetail_tbl_widget.rowCount())]
            for idx, (no, salePrice, addTax, supplyPrice, marginPrice) in enumerate(data):
                item0, item1, item2, item3, item4 = self.create_item(no, salePrice, addTax, supplyPrice, marginPrice)
                nextIdx = self.saleDetail_tbl_widget.rowCount()
                self.saleDetail_tbl_widget.insertRow(nextIdx)
                self.saleDetail_tbl_widget.setItem(nextIdx, 0, item0)
                self.saleDetail_tbl_widget.setItem(nextIdx, 1, item1)
                self.saleDetail_tbl_widget.setItem(nextIdx, 2, item2)
                self.saleDetail_tbl_widget.setItem(nextIdx, 3, item3)
                self.saleDetail_tbl_widget.setItem(nextIdx, 4, item4)

    # DB에서 테이블별 데이터 읽어오기
    def load_data_from_db(self):
        self.load_data(self.pDao.select_item(), 0)
        self.load_data(self.sDao.select_item(), 1)
        self.load_data(self.sdDao.select_item(), 2)

    # 우클릭 '수정'선택시 수행되는 기능
    def __update(self):
        # QMessageBox.information(self, 'Update', "확인", QMessageBox.Ok)
        if self.tab_widget.currentIndex() == 0:
            try:
                if self.pro_tbl_widget.selectedIndexes().__len__() > self.pro_tbl_widget.columnCount():
                    raise IndexError('수정은 하나의 행만 가능합니다!')
                selectedItems = self.pro_tbl_widget.selectedItems()
                self.pro_le_code.setText(selectedItems[0].text())
                self.pro_le_name.setText(selectedItems[1].text())
                self.pro_btn_add.setText("수정")
                self.pro_btn_add.clicked.disconnect()
                self.pro_btn_add.clicked.connect(self.update_item)
                self.pro_btn_del.setDisabled(True)
                self.pro_tbl_widget.setSelectionMode(QAbstractItemView.NoSelection)
            except IndexError as e:
                print(e)
        elif self.tab_widget.currentIndex() == 1:
            try:
                if self.sale_tbl_widget.selectedIndexes().__len__() > self.sale_tbl_widget.columnCount():
                    raise IndexError('수정은 하나의 행만 가능합니다!')
                selectedItems = self.sale_tbl_widget.selectedItems()
                self.sale_le_no.setText(selectedItems[0].text())
                self.sale_le_code.setText(selectedItems[1].text())
                self.sale_le_price.setText(selectedItems[2].text())
                self.sale_le_saleCnt.setText(selectedItems[3].text())
                self.sale_le_marginRate.setText(selectedItems[4].text())
                self.sale_btn_add.setText("수정")
                self.sale_btn_add.clicked.disconnect()
                self.sale_btn_add.clicked.connect(self.update_item)
                self.sale_btn_del.setDisabled(True)
                self.sale_tbl_widget.setSelectionMode(QAbstractItemView.NoSelection)
            except IndexError as e:
                print(e)
        elif self.tab_widget.currentIndex() == 2:
            try:
                if self.saleDetail_tbl_widget.selectedIndexes().__len__() > self.saleDetail_tbl_widget.columnCount():
                    raise IndexError('수정은 하나의 행만 가능합니다!')
                selectedItems = self.saleDetail_tbl_widget.selectedItems()
                self.saleDetail_le_no.setText(selectedItems[0].text())
                self.saleDetail_le_salePrice.setText(selectedItems[1].text())
                self.saleDetail_le_addTax.setText(selectedItems[2].text())
                self.saleDetail_le_supplyPrice.setText(selectedItems[3].text())
                self.saleDetail_le_marginPrice.setText(selectedItems[4].text())
                self.saleDetail_btn_add.setText("수정")
                self.saleDetail_btn_add.clicked.disconnect()
                self.saleDetail_btn_add.clicked.connect(self.update_item)
                self.saleDetail_btn_del.setDisabled(True)
                self.saleDetail_tbl_widget.setSelectionMode(QAbstractItemView.NoSelection)
            except IndexError as e:
                print(e)

    # todo 우클릭 삭제는 `191220 미구현...
    def __delete(self):
        pass
        QMessageBox.information(self, 'Delete', "확인", QMessageBox.Ok)

    # line edit 으로부터 가져온 값들을 create_item()으로 타입을 변환해서 반환
    def get_item_from_le(self):
        if self.tab_widget.currentIndex() == 0:
            code = self.pro_le_code.text()
            name = self.pro_le_name.text()
            return code, name
        elif self.tab_widget.currentIndex() == 1:
            no = self.sale_le_no.text()
            code = self.sale_le_code.text()
            price = self.sale_le_price.text()
            saleCnt = self.sale_le_saleCnt.text()
            marginRate = self.sale_le_marginRate.text()
            return no, code, price, saleCnt, marginRate
        elif self.tab_widget.currentIndex() == 2:
            no = self.saleDetail_le_no.text()
            salePrice = self.saleDetail_le_salePrice.text()
            addTax = self.saleDetail_le_addTax.text()
            supplyPrice = self.saleDetail_le_supplyPrice.text()
            marginPrice = self.saleDetail_le_marginPrice.text()
            return no, salePrice, addTax, supplyPrice, marginPrice

    # line edit 초기화
    def init_item(self):
        if self.tab_widget.currentIndex() == 0:
            self.pro_le_code.clear()
            self.pro_le_name.clear()
        elif self.tab_widget.currentIndex() == 1:
            self.sale_le_no.clear()
            self.sale_le_code.clear()
            self.sale_le_price.clear()
            self.sale_le_saleCnt.clear()
            self.sale_le_marginRate.clear()
        elif self.tab_widget.currentIndex() == 2:
            self.saleDetail_le_no.clear()
            self.saleDetail_le_salePrice.clear()
            self.saleDetail_le_addTax.clear()
            self.saleDetail_le_supplyPrice.clear()
            self.saleDetail_le_marginPrice.clear()

    # line edit 으로부터 가져온 값들을 tbl_widget의 현재행(curruntIdx)에 삽입
    def add_item(self):
        if self.tab_widget.currentIndex() == 0:
            item0, item1 = self.get_item_from_le()
            self.pDao.insert_item(item0, item1)
        elif self.tab_widget.currentIndex() == 1:
            item0, item1, item2, item3, item4 = self.get_item_from_le()
            self.sDao.insert_item(item0, item1, item2, item3, item4)
        elif self.tab_widget.currentIndex() == 2:
            item0, item1, item2, item3, item4 = self.get_item_from_le()
            self.sdDao.insert_item(item0, item1, item2, item3, item4)
        self.load_data_from_db()
        self.init_item()

    # 우클릭 '수정'으로 '추가'버튼이 '수정'버튼으로 변경/활성화 된 상태에서 수행되는 기능(line edit의 값을 tbl_widget에 반영)
    def update_item(self):
        if self.tab_widget.currentIndex() == 0:
            selectedIndexes = self.pro_tbl_widget.selectedIndexes()
            item0, item1 = self.get_item_from_le()
            self.pro_tbl_widget.setItem(selectedIndexes[0].row(), selectedIndexes[0].column(), item0)
            self.pro_tbl_widget.setItem(selectedIndexes[1].row(), selectedIndexes[1].column(), item1)
            self.pro_btn_add.setText("추가")
            self.pro_btn_add.clicked.disconnect()
            self.pro_btn_add.clicked.connect(self.add_item)
            self.pro_btn_del.setEnabled(True)
            # self.pro_tbl_widget.setSelectionMode(QAbstractItemView.SingleSelection)
            self.pro_tbl_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        elif self.tab_widget.currentIndex() == 1:
            selectedIndexes = self.sale_tbl_widget.selectedIndexes()
            item0, item1, item2, item3, item4 = self.get_item_from_le()
            self.sale_tbl_widget.setItem(selectedIndexes[0].row(), selectedIndexes[0].column(), item0)
            self.sale_tbl_widget.setItem(selectedIndexes[1].row(), selectedIndexes[1].column(), item1)
            self.sale_tbl_widget.setItem(selectedIndexes[2].row(), selectedIndexes[2].column(), item2)
            self.sale_tbl_widget.setItem(selectedIndexes[3].row(), selectedIndexes[3].column(), item3)
            self.sale_tbl_widget.setItem(selectedIndexes[4].row(), selectedIndexes[4].column(), item4)
            self.sale_btn_add.setText("추가")
            self.sale_btn_add.clicked.disconnect()
            self.sale_btn_add.clicked.connect(self.add_item)
            self.sale_btn_del.setEnabled(True)
            # self.sale_tbl_widget.setSelectionMode(QAbstractItemView.SingleSelection)
            self.sale_tbl_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        elif self.tab_widget.currentIndex() == 2:
            selectedIndexes = self.saleDetail_tbl_widget.selectedIndexes()
            item0, item1, item2, item3, item4 = self.get_item_from_le()
            self.saleDetail_tbl_widget.setItem(selectedIndexes[0].row(), selectedIndexes[0].column(), item0)
            self.saleDetail_tbl_widget.setItem(selectedIndexes[1].row(), selectedIndexes[1].column(), item1)
            self.saleDetail_tbl_widget.setItem(selectedIndexes[2].row(), selectedIndexes[2].column(), item2)
            self.saleDetail_tbl_widget.setItem(selectedIndexes[3].row(), selectedIndexes[3].column(), item3)
            self.saleDetail_tbl_widget.setItem(selectedIndexes[4].row(), selectedIndexes[4].column(), item4)
            self.saleDetail_btn_add.setText("추가")
            self.saleDetail_btn_add.clicked.disconnect()
            self.saleDetail_btn_add.clicked.connect(self.add_item)
            self.saleDetail_btn_del.setEnabled(True)
            # self.sale_tbl_widget.setSelectionMode(QAbstractItemView.SingleSelection)
            self.saleDetail_tbl_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.init_item()

    # 클릭으로 선택된 row '삭제'버튼으로 삭제
    def delete_item(self):
        if self.tab_widget.currentIndex() == 0:
            try:
                indexList = self.pro_tbl_widget.selectedIndexes()
                rowList = [index.row() for index in indexList if index.column() is 0]
                rowList.sort()
                for row in reversed(rowList):
                    self.pro_tbl_widget.removeRow(row)
            except IndexError as e:
                print(e)
        elif self.tab_widget.currentIndex() == 1:
            try:
                indexList = self.sale_tbl_widget.selectedIndexes()
                rowList = [index.row() for index in indexList if index.column() is 0]
                rowList.sort()
                for row in reversed(rowList):
                    self.sale_tbl_widget.removeRow(row)
            except IndexError as e:
                print(e)
        elif self.tab_widget.currentIndex() == 2:
            try:
                indexList = self.saleDetail_tbl_widget.selectedIndexes()
                rowList = [index.row() for index in indexList if index.column() is 0]
                rowList.sort()
                for row in reversed(rowList):
                    self.saleDetail_tbl_widget.removeRow(row)
            except IndexError as e:
                print(e)

    # 화면이 닫히면 closeSignal 발생
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.closeSignal.emit()
        super().closeEvent(a0)

    # PyUIC5 툴로 자동 생성된 메소드
    def setupUi(self, dml_widget):
        dml_widget.setObjectName("dml_widget")
        dml_widget.resize(947, 614)
        self.gridLayout = QtWidgets.QGridLayout(dml_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.tab_widget = QtWidgets.QTabWidget(dml_widget)
        self.tab_widget.setObjectName("tab_widget")
        self.pro_tab_widget = QtWidgets.QWidget()
        self.pro_tab_widget.setObjectName("pro_tab_widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.pro_tab_widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pro_btn_add = QtWidgets.QPushButton(self.pro_tab_widget)
        self.pro_btn_add.setObjectName("pro_btn_add")
        self.horizontalLayout.addWidget(self.pro_btn_add)
        self.pro_btn_del = QtWidgets.QPushButton(self.pro_tab_widget)
        self.pro_btn_del.setObjectName("pro_btn_del")
        self.horizontalLayout.addWidget(self.pro_btn_del)
        self.pro_btn_init = QtWidgets.QPushButton(self.pro_tab_widget)
        self.pro_btn_init.setObjectName("pro_btn_init")
        self.horizontalLayout.addWidget(self.pro_btn_init)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.pro_lbl_code = QtWidgets.QLabel(self.pro_tab_widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pro_lbl_code.setFont(font)
        self.pro_lbl_code.setObjectName("pro_lbl_code")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pro_lbl_code)
        self.pro_le_code = QtWidgets.QLineEdit(self.pro_tab_widget)
        self.pro_le_code.setObjectName("pro_le_code")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pro_le_code)
        self.pro_lbl_name = QtWidgets.QLabel(self.pro_tab_widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pro_lbl_name.setFont(font)
        self.pro_lbl_name.setObjectName("pro_lbl_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pro_lbl_name)
        self.pro_le_name = QtWidgets.QLineEdit(self.pro_tab_widget)
        self.pro_le_name.setObjectName("pro_le_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pro_le_name)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        self.pro_tbl_widget = QtWidgets.QTableWidget(self.pro_tab_widget)
        self.pro_tbl_widget.setColumnCount(2)
        self.pro_tbl_widget.setObjectName("pro_tbl_widget")
        self.pro_tbl_widget.setRowCount(0)
        self.gridLayout_2.addWidget(self.pro_tbl_widget, 2, 0, 1, 1)
        self.tab_widget.addTab(self.pro_tab_widget, "")
        self.sale_tab_widget = QtWidgets.QWidget()
        self.sale_tab_widget.setObjectName("sale_tab_widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.sale_tab_widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.sale_lbl_no = QtWidgets.QLabel(self.sale_tab_widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sale_lbl_no.setFont(font)
        self.sale_lbl_no.setObjectName("sale_lbl_no")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.sale_lbl_no)
        self.sale_le_no = QtWidgets.QLineEdit(self.sale_tab_widget)
        self.sale_le_no.setObjectName("sale_le_no")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sale_le_no)
        self.sale_lbl_code = QtWidgets.QLabel(self.sale_tab_widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sale_lbl_code.setFont(font)
        self.sale_lbl_code.setObjectName("sale_lbl_code")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.sale_lbl_code)
        self.sale_le_code = QtWidgets.QLineEdit(self.sale_tab_widget)
        self.sale_le_code.setObjectName("sale_le_code")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sale_le_code)
        self.sale_lbl_price = QtWidgets.QLabel(self.sale_tab_widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sale_lbl_price.setFont(font)
        self.sale_lbl_price.setObjectName("sale_lbl_price")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.sale_lbl_price)
        self.sale_lbl_saleCnt = QtWidgets.QLabel(self.sale_tab_widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sale_lbl_saleCnt.setFont(font)
        self.sale_lbl_saleCnt.setObjectName("sale_lbl_saleCnt")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.sale_lbl_saleCnt)
        self.sale_lbl_marginRate = QtWidgets.QLabel(self.sale_tab_widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sale_lbl_marginRate.setFont(font)
        self.sale_lbl_marginRate.setObjectName("sale_lbl_marginRate")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.sale_lbl_marginRate)
        self.sale_le_price = QtWidgets.QLineEdit(self.sale_tab_widget)
        self.sale_le_price.setObjectName("sale_le_price")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sale_le_price)
        self.sale_le_saleCnt = QtWidgets.QLineEdit(self.sale_tab_widget)
        self.sale_le_saleCnt.setObjectName("sale_le_saleCnt")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sale_le_saleCnt)
        self.sale_le_marginRate = QtWidgets.QLineEdit(self.sale_tab_widget)
        self.sale_le_marginRate.setObjectName("sale_le_marginRate")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sale_le_marginRate)
        self.gridLayout_3.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.sale_btn_add = QtWidgets.QPushButton(self.sale_tab_widget)
        self.sale_btn_add.setObjectName("sale_btn_add")
        self.horizontalLayout_2.addWidget(self.sale_btn_add)
        self.sale_btn_del = QtWidgets.QPushButton(self.sale_tab_widget)
        self.sale_btn_del.setObjectName("sale_btn_del")
        self.horizontalLayout_2.addWidget(self.sale_btn_del)
        self.sale_btn_init = QtWidgets.QPushButton(self.sale_tab_widget)
        self.sale_btn_init.setObjectName("sale_btn_init")
        self.horizontalLayout_2.addWidget(self.sale_btn_init)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.sale_tbl_widget = QtWidgets.QTableWidget(self.sale_tab_widget)
        self.sale_tbl_widget.setColumnCount(5)
        self.sale_tbl_widget.setObjectName("sale_tbl_widget")
        self.sale_tbl_widget.setRowCount(0)
        self.gridLayout_3.addWidget(self.sale_tbl_widget, 2, 0, 1, 1)
        self.tab_widget.addTab(self.sale_tab_widget, "")
        self.saleDetail_tab_widget = QtWidgets.QWidget()
        self.saleDetail_tab_widget.setObjectName("saleDetail_tab_widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.saleDetail_tab_widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.saleDetail_lbl_no = QtWidgets.QLabel(self.saleDetail_tab_widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.saleDetail_lbl_no.setFont(font)
        self.saleDetail_lbl_no.setObjectName("saleDetail_lbl_no")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.saleDetail_lbl_no)
        self.saleDetail_le_no = QtWidgets.QLineEdit(self.saleDetail_tab_widget)
        self.saleDetail_le_no.setObjectName("saleDetail_le_no")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.saleDetail_le_no)
        self.saleDetail_lbl_salePrice = QtWidgets.QLabel(self.saleDetail_tab_widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.saleDetail_lbl_salePrice.setFont(font)
        self.saleDetail_lbl_salePrice.setObjectName("saleDetail_lbl_salePrice")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.saleDetail_lbl_salePrice)
        self.saleDetail_le_salePrice = QtWidgets.QLineEdit(self.saleDetail_tab_widget)
        self.saleDetail_le_salePrice.setObjectName("saleDetail_le_salePrice")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.saleDetail_le_salePrice)
        self.saleDetail_lbl_addTax = QtWidgets.QLabel(self.saleDetail_tab_widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.saleDetail_lbl_addTax.setFont(font)
        self.saleDetail_lbl_addTax.setObjectName("saleDetail_lbl_addTax")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.saleDetail_lbl_addTax)
        self.saleDetail_lbl_supplyPrice = QtWidgets.QLabel(self.saleDetail_tab_widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.saleDetail_lbl_supplyPrice.setFont(font)
        self.saleDetail_lbl_supplyPrice.setObjectName("saleDetail_lbl_supplyPrice")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.saleDetail_lbl_supplyPrice)
        self.saleDetail_lbl_marginPrice = QtWidgets.QLabel(self.saleDetail_tab_widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.saleDetail_lbl_marginPrice.setFont(font)
        self.saleDetail_lbl_marginPrice.setObjectName("saleDetail_lbl_marginPrice")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.saleDetail_lbl_marginPrice)
        self.saleDetail_le_addTax = QtWidgets.QLineEdit(self.saleDetail_tab_widget)
        self.saleDetail_le_addTax.setObjectName("saleDetail_le_addTax")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.saleDetail_le_addTax)
        self.saleDetail_le_supplyPrice = QtWidgets.QLineEdit(self.saleDetail_tab_widget)
        self.saleDetail_le_supplyPrice.setObjectName("saleDetail_le_supplyPrice")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.saleDetail_le_supplyPrice)
        self.saleDetail_le_marginPrice = QtWidgets.QLineEdit(self.saleDetail_tab_widget)
        self.saleDetail_le_marginPrice.setObjectName("saleDetail_le_marginPrice")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.saleDetail_le_marginPrice)
        self.gridLayout_4.addLayout(self.formLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.saleDetail_btn_add = QtWidgets.QPushButton(self.saleDetail_tab_widget)
        self.saleDetail_btn_add.setObjectName("saleDetail_btn_add")
        self.horizontalLayout_3.addWidget(self.saleDetail_btn_add)
        self.saleDetail_btn_del = QtWidgets.QPushButton(self.saleDetail_tab_widget)
        self.saleDetail_btn_del.setObjectName("saleDetail_btn_del")
        self.horizontalLayout_3.addWidget(self.saleDetail_btn_del)
        self.saleDetail_btn_init = QtWidgets.QPushButton(self.saleDetail_tab_widget)
        self.saleDetail_btn_init.setObjectName("saleDetail_btn_init")
        self.horizontalLayout_3.addWidget(self.saleDetail_btn_init)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.saleDetail_tbl_widget = QtWidgets.QTableWidget(self.saleDetail_tab_widget)
        self.saleDetail_tbl_widget.setColumnCount(5)
        self.saleDetail_tbl_widget.setObjectName("saleDetail_tbl_widget")
        self.saleDetail_tbl_widget.setRowCount(0)
        self.gridLayout_4.addWidget(self.saleDetail_tbl_widget, 2, 0, 1, 1)
        self.tab_widget.addTab(self.saleDetail_tab_widget, "")
        self.gridLayout.addWidget(self.tab_widget, 0, 0, 1, 1)

        self.retranslateUi(dml_widget)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(dml_widget)

    # PyUIC5 툴로 자동 생성된 메소드
    def retranslateUi(self, dml_widget):
        _translate = QtCore.QCoreApplication.translate
        dml_widget.setWindowTitle(_translate("dml_widget", "Form"))
        self.pro_btn_add.setText(_translate("dml_widget", "추가"))
        self.pro_btn_del.setText(_translate("dml_widget", "삭제"))
        self.pro_btn_init.setText(_translate("dml_widget", "초기화"))
        self.pro_lbl_code.setText(_translate("dml_widget", "code"))
        self.pro_lbl_name.setText(_translate("dml_widget", "name"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.pro_tab_widget), _translate("dml_widget", "Product"))
        self.sale_lbl_no.setText(_translate("dml_widget", "no"))
        self.sale_lbl_code.setText(_translate("dml_widget", "code"))
        self.sale_lbl_price.setText(_translate("dml_widget", "price"))
        self.sale_lbl_saleCnt.setText(_translate("dml_widget", "saleCnt"))
        self.sale_lbl_marginRate.setText(_translate("dml_widget", "marginRate"))
        self.sale_btn_add.setText(_translate("dml_widget", "추가"))
        self.sale_btn_del.setText(_translate("dml_widget", "삭제"))
        self.sale_btn_init.setText(_translate("dml_widget", "초기화"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.sale_tab_widget), _translate("dml_widget", "Sale"))
        self.saleDetail_lbl_no.setText(_translate("dml_widget", "no"))
        self.saleDetail_lbl_salePrice.setText(_translate("dml_widget", "salePrice"))
        self.saleDetail_lbl_addTax.setText(_translate("dml_widget", "addTax"))
        self.saleDetail_lbl_supplyPrice.setText(_translate("dml_widget", "supplyPrice"))
        self.saleDetail_lbl_marginPrice.setText(_translate("dml_widget", "marginPrice"))
        self.saleDetail_btn_add.setText(_translate("dml_widget", "추가"))
        self.saleDetail_btn_del.setText(_translate("dml_widget", "삭제"))
        self.saleDetail_btn_init.setText(_translate("dml_widget", "초기화"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.saleDetail_tab_widget), _translate("dml_widget", "SaleDetail"))

