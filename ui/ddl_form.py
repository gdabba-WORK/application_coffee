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
    db = DbInit()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)

        self.btn_create.clicked.connect(self.db.service)
        self.btn_create.clicked.connect(lambda stat, text=self.btn_create.text():
                                        self.showButtonText(stat, text))
        self.btn_backup.clicked.connect(self.db.backup)
        self.btn_backup.clicked.connect(lambda stat, text=self.btn_backup.text():
                                        self.showButtonText(stat, text))
        self.btn_restore.clicked.connect(self.db.restore)
        self.btn_restore.clicked.connect(lambda stat, text=self.btn_restore.text():
                                         self.showButtonText(stat, text))

        self.btn_goback.clicked.connect(self.close)

    def showButtonText(self, stat, text):
        QMessageBox.information(self, 'System Message', text+' Success', QMessageBox.Ok)

    def close(self) -> bool:
        self.closeSignal.emit()
        return super().close()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.closeSignal.emit()
        super().closeEvent(a0)

    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(532, 189)
        self.gridLayout = QtWidgets.QGridLayout(widget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.btn_create = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_create.setFont(font)
        self.btn_create.setObjectName("btn_create")
        self.btn_backup = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_backup.setFont(font)
        self.btn_backup.setObjectName("btn_backup")
        self.btn_restore = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_restore.setFont(font)
        self.btn_restore.setObjectName("btn_restore")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.btn_goback = QtWidgets.QPushButton(widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_goback.setFont(font)
        self.btn_goback.setObjectName("btn_goback")
        self.gridLayout.addWidget(self.btn_goback, 1, 0, 1, 1)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "DDL Application"))
        self.btn_create.setText(_translate("widget", "Create"))
        self.btn_backup.setText(_translate("widget", "Backup"))
        self.btn_restore.setText(_translate("widget", "Restore"))
        self.btn_goback.setText(_translate("widget", "뒤로가기"))