import inspect

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QHeaderView, QTableWidgetItem, QMessageBox
from mysql.connector import Error
from skimage.viewer.qt import Qt

from db_connection.connection_pool import ConnectionPool

select_sql1 = """SELECT (SELECT count(*)+1 FROM sale_detail WHERE salePrice > sd.salePrice) as rank,
s.code, p.name, s.price, s.saleCnt, sd.supplyPrice, sd.addTax, sd.salePrice, s.marginRate, sd.marginPrice
FROM product as p join sale as s on p.code =s.code join sale_detail as sd on s.no = sd.no
ORDER BY sd.salePrice DESC"""

select_sql2 = """SELECT (SELECT count(*)+1 FROM sale_detail WHERE marginPrice > sd.marginPrice) as rank,
s.code, p.name, s.price, s.saleCnt, sd.supplyPrice, sd.addTax, sd.salePrice, s.marginRate, sd.marginPrice
FROM product as p join sale as s on p.code =s.code join sale_detail as sd on s.no = sd.no
ORDER BY sd.marginPrice DESC"""


def iter_row(cursor, size=5):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row


class RankUi(QWidget):
    def __init__(self, flag):
        super().__init__()
        self.__setupUi(self)
        self.lbl.setText('판 매 금 액 순 위') if flag is 1 else self.lbl.setText('마 진 액 순 위')
        self.set_table(self.tbl_widget1, ['순위', '제품코드', '제품명', '제품단가', '판매수량',
                                          '공급가액', '부가세액', '판매금액', '마진율', '마진액'])
        self.set_table(self.tbl_widget2, ['합계', '제품코드', '제품명', '제품단가', '판매수량',
                                          '공급가액', '부가세액', '판매금액', '마진율', '마진액'])
        self.connection_pool = ConnectionPool.get_instance()
        self.load_data_from_db(flag)
        self.show()

    def select_item(self, flag):
        print("\n______{}()______".format(inspect.stack()[0][3]))
        try:
            conn = self.connection_pool.get_connection()
            cursor = conn.cursor()
            # cursor.execute("USE coffee")
            cursor.execute(select_sql1) if flag is 1 else cursor.execute(select_sql2)
            res = []
            [res.append(row) for row in iter_row(cursor, 5)]
            return res
        except Error as e:
            raise e
        finally:
            cursor.close()
            conn.close()

    def create_item(self, *args):
        items = []
        for value in args:
            item = QTableWidgetItem()
            item.setTextAlignment(Qt.AlignCenter)
            item.setData(Qt.DisplayRole, value)
            items.append(item)
        return items

    def load_data_from_db(self, flag):
        try:
            sum_var5 = 0
            sum_var6 = 0
            sum_var7 = 0
            sum_var9 = 0
            for idx, (var0, var1, var2, var3, var4, var5, var6, var7, var8, var9) in enumerate(self.select_item(flag)):
                item0, item1, item2, item3, item4, item5, item6, item7, item8, item9 = \
                    self.create_item(var0, var1, var2, var3, var4, var5, var6, var7, var8, var9)
                nextIdx = self.tbl_widget1.rowCount()
                self.tbl_widget1.insertRow(nextIdx)
                self.tbl_widget1.setItem(nextIdx, 0, item0)
                self.tbl_widget1.setItem(nextIdx, 1, item1)
                self.tbl_widget1.setItem(nextIdx, 2, item2)
                self.tbl_widget1.setItem(nextIdx, 3, item3)
                self.tbl_widget1.setItem(nextIdx, 4, item4)
                self.tbl_widget1.setItem(nextIdx, 5, item5)
                self.tbl_widget1.setItem(nextIdx, 6, item6)
                self.tbl_widget1.setItem(nextIdx, 7, item7)
                self.tbl_widget1.setItem(nextIdx, 8, item8)
                self.tbl_widget1.setItem(nextIdx, 9, item9)
                sum_var5 += var5
                sum_var6 += var6
                sum_var7 += var7
                sum_var9 += var9
            item0, item5, item6, item7, item9 = \
                self.create_item('합계', sum_var5, sum_var6, sum_var7, sum_var9)
            self.tbl_widget2.insertRow(0)
            self.tbl_widget2.setItem(0, 0, item0)
            self.tbl_widget2.setItem(0, 5, item5)
            self.tbl_widget2.setItem(0, 6, item6)
            self.tbl_widget2.setItem(0, 7, item7)
            self.tbl_widget2.setItem(0, 9, item9)
        except Error as e:
            QMessageBox.information(self, "Load Error", e.msg, QMessageBox.Ok)
            self.close()

    def set_table(self, table=None, data=None):
        table.setHorizontalHeaderLabels(data)
        # row단위 선택
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 테이블 직접 값 입력 불가 설정
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 균일한 간격으로 열 재배치(Qt Designer에 해당 옵션이 존재하지 않아 코드로 직접 설정)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def __setupUi(self, widget):
        widget.setObjectName("Form")
        widget.resize(946, 517)
        self.gridLayout = QtWidgets.QGridLayout(widget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl = QtWidgets.QLabel(widget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lbl.setFont(font)
        self.lbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setObjectName("lbl")
        self.verticalLayout.addWidget(self.lbl)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.tbl_widget1 = QtWidgets.QTableWidget(widget)
        self.tbl_widget1.setColumnCount(10)
        self.tbl_widget1.setObjectName("tbl_widget1")
        self.tbl_widget1.setRowCount(0)
        self.verticalLayout.addWidget(self.tbl_widget1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.tbl_widget2 = QtWidgets.QTableWidget(widget)
        self.tbl_widget2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_widget2.sizePolicy().hasHeightForWidth())
        self.tbl_widget2.setSizePolicy(sizePolicy)
        self.tbl_widget2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.tbl_widget2.setColumnCount(10)
        self.tbl_widget2.setObjectName("tbl_widget2")
        self.tbl_widget2.setRowCount(0)
        self.tbl_widget2.horizontalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tbl_widget2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.__retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def __retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("Form", "Form"))
        self.lbl.setText(_translate("Form", "제목"))
