from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox

from db_connection.coffee_init_service import DbInit


class DDLUi(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("ui/ddl_form.ui")
        self.ui.show()
        self.db = DbInit()

        self.ui.btn_create.clicked.connect(self.db.service)
        self.ui.btn_create.clicked.connect(lambda stat, text=self.ui.btn_create.text() : self.showButtonText(stat, text))
        self.ui.btn_backup.clicked.connect(self.db.backup)
        self.ui.btn_backup.clicked.connect(lambda stat, text=self.ui.btn_backup.text() : self.showButtonText(stat, text))
        self.ui.btn_restore.clicked.connect(self.db.restore)
        self.ui.btn_restore.clicked.connect(lambda stat, text=self.ui.btn_restore.text() : self.showButtonText(stat, text))

    def showButtonText(self, stat, text):
        QMessageBox.information(self, 'System Message', text+' Success', QMessageBox.Ok)

