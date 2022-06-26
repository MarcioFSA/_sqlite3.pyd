
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox,
                             QPushButton, QTableWidgetItem, QWidget)

from view.login import Ui_login
from view import Imagens

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_login()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())


