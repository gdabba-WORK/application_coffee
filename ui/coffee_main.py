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

        self.btn_exit.clicked.connect(self.close)

    def switchDDL(self):
        self.hide()
        self.ddl.show()

    def switchDML(self):
        self.hide()
        self.dml.load_data()
        self.dml.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 374)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setMinimumSize(QtCore.QSize(500, 100))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit.setFont(font)
        self.btn_exit.setObjectName("btn_exit")
        self.gridLayout.addWidget(self.btn_exit, 2, 0, 1, 1)
        self.btn_ddl = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ddl.setMinimumSize(QtCore.QSize(500, 100))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.btn_ddl.setFont(font)
        self.btn_ddl.setObjectName("btn_ddl")
        self.gridLayout.addWidget(self.btn_ddl, 0, 0, 1, 1)
        self.btn_dml = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dml.setMinimumSize(QtCore.QSize(500, 100))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.btn_dml.setFont(font)
        self.btn_dml.setObjectName("btn_dml")
        self.gridLayout.addWidget(self.btn_dml, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 20))
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
        self.btn_exit.setText(_translate("MainWindow", "종료"))
        self.btn_ddl.setText(_translate("MainWindow", "관리자"))
        self.btn_dml.setText(_translate("MainWindow", "사용자"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))