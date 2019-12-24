from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from ui.ddl_form import SettingUi
from ui.dml_form import ManipulationUi


class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__setupUi(self)
        self.show()

        self.s_ui = SettingUi()
        self.btn_ddl.clicked.connect(self.switchSui)
        self.s_ui.closeSignal.connect(self.show)

        self.m_ui = ManipulationUi()
        self.btn_dml.clicked.connect(self.switchMui)
        self.m_ui.closeSignal.connect(self.show)

        self.btn_exit.clicked.connect(self.close)

    # Setting Ui로 전환
    def switchSui(self):
        self.hide()
        self.s_ui.show()

    # Manipulation Ui로 전환
    def switchMui(self):
        self.hide()
        self.m_ui.load_data()
        self.m_ui.show()

    # PyUIC5 툴로 자동 생성된 메소드 1/2 (uic 모듈의 loadUi()와 같다)
    def __setupUi(self, MainWindow):
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

        self.__retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # PyUIC5 툴로 자동 생성된 메소드 2/2
    def __retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Coffee Application"))
        self.btn_exit.setText(_translate("MainWindow", "종료"))
        self.btn_ddl.setText(_translate("MainWindow", "관리자"))
        self.btn_dml.setText(_translate("MainWindow", "사용자"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))