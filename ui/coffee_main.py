# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coffee_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from ui.ddl_form import DDLUi
from ui.dml_form import DMLUi


class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.show()

        self.ddl = DDLUi()
        self.btn_ddl.clicked.connect(self.switchDDL)
        self.ddl.closeSignal.connect(self.show)

        self.dml = DMLUi()
        self.btn_dml.clicked.connect(self.switchDML)
        self.dml.closeSignal.connect(self.show)

    def switchDDL(self):
        self.hide()
        self.ddl.show()

    def switchDML(self):
        self.hide()
        self.dml.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 511)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 502, 420))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_ddl = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_ddl.setMinimumSize(QtCore.QSize(500, 100))
        self.btn_ddl.setObjectName("btn_ddl")
        self.gridLayout.addWidget(self.btn_ddl, 0, 0, 1, 1)
        self.btn_dml = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_dml.setMinimumSize(QtCore.QSize(500, 100))
        self.btn_dml.setObjectName("btn_dml")
        self.gridLayout.addWidget(self.btn_dml, 1, 0, 1, 1)
        self.btn_dcl = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_dcl.setMinimumSize(QtCore.QSize(500, 100))
        self.btn_dcl.setObjectName("btn_dcl")
        self.gridLayout.addWidget(self.btn_dcl, 2, 0, 1, 1)
        self.btn_exit = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_exit.setMinimumSize(QtCore.QSize(500, 100))
        self.btn_exit.setObjectName("btn_exit")
        self.gridLayout.addWidget(self.btn_exit, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 20))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Coffee Application"))
        self.btn_ddl.setText(_translate("MainWindow", "DDL"))
        self.btn_dml.setText(_translate("MainWindow", "DML"))
        self.btn_dcl.setText(_translate("MainWindow", "DCL"))
        self.btn_exit.setText(_translate("MainWindow", "Exit"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))

