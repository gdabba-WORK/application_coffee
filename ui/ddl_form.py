from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.Qt import QAbstractButton
from PyQt5.QtWidgets import QAbstractButton
from PyQt5.QtCore import pyqtSignal


class CoffeeUiDDL(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("database_setting/ddl_form.ui")
        self.ui.show()
        self.db = DbInit()

        # 변수 stat에는 true가 assignment 된다.
        # ==QAbstractButton.py==
        # def clicked(self, bool=False):  # real signature unknown; restored from __doc__
        #     """ clicked(self, bool = False) [signal] """
        #     pass

        self.ui.btn_create.clicked.connect(self.db.service)
        self.ui.btn_create.clicked.connect(lambda stat, text=self.ui.btn_create.text() : self.showButtonText(stat, text))
        self.ui.btn_backup.clicked.connect(self.db.backup)
        self.ui.btn_backup.clicked.connect(lambda stat, text=self.ui.btn_backup.text() : self.showButtonText(stat, text))
        self.ui.btn_restore.clicked.connect(self.db.restore)
        self.ui.btn_restore.clicked.connect(lambda stat, text=self.ui.btn_restore.text() : self.showButtonText(stat, text))

    def showButtonText(self, stat, text):
        QMessageBox.information(self, 'System Message', text+' Success', QMessageBox.Ok)

