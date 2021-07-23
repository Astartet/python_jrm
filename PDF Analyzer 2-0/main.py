from PyQt5 import QtCore, QtGui, QtWidgets
from toolpatv1 import Ui_Toolpat

import sys


class MyWindow(QtWidgets.QMainWindow,QtWidgets.QMessageBox,QtWidgets.QLineEdit, Ui_Toolpat):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_Toolpat()
        self.ui.setupUi(self)
        self.ui.pushButton_41.clicked.connect(self.avisoLegal)
        self.ui.pushButton_3.clicked.connect(self.andalucia)
        self.ui.pushButton_4.clicked.connect(self.BOE)
        self.ui.pushButton_5.clicked.connect(self.Acoruna)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyWindow()
    mainWindow.show()
    sys.exit(app.exec_())