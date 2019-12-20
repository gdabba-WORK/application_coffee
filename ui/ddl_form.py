# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ddl_form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QMessageBox

from db_connection.coffee_init_service import DbInit


class DDLUi(QWidget):
    closeSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)

        self.db = DbInit()
        self.btn_create.clicked.connect(self.db.service)
        self.btn_create.clicked.connect(lambda stat, text=self.btn_create.text():
                                        self.showButtonText(stat, text))
        self.btn_backup.clicked.connect(self.db.backup)
        self.btn_backup.clicked.connect(lambda stat, text=self.btn_backup.text():
                                        self.showButtonText(stat, text))
        self.btn_restore.clicked.connect(self.db.restore)
        self.btn_restore.clicked.connect(lambda stat, text=self.btn_restore.text():
                                         self.showButtonText(stat, text))

    def showButtonText(self, stat, text):
        QMessageBox.information(self, 'System Message', text+' Success', QMessageBox.Ok)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.closeSignal.emit()
        super().closeEvent(a0)

    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(532, 295)
        self.splitter = QtWidgets.QSplitter(widget)
        self.splitter.setGeometry(QtCore.QRect(50, 30, 401, 101))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.btn_create = QtWidgets.QPushButton(self.splitter)
        self.btn_create.setObjectName("btn_create")
        self.btn_backup = QtWidgets.QPushButton(self.splitter)
        self.btn_backup.setObjectName("btn_backup")
        self.btn_restore = QtWidgets.QPushButton(self.splitter)
        self.btn_restore.setObjectName("btn_restore")
        self.btn_close = QtWidgets.QPushButton(widget)
        self.btn_close.setGeometry(QtCore.QRect(200, 190, 80, 23))
        self.btn_close.setObjectName("btn_close")

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)


    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "DDL Application"))
        self.btn_create.setText(_translate("widget", "Create"))
        self.btn_backup.setText(_translate("widget", "Backup"))
        self.btn_restore.setText(_translate("widget", "Restore"))
        self.btn_close.setText(_translate("widget", "close"))
