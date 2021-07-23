from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from textos import Ui_MainWindow


class Ventana(QtWidgets.QMainWindow,QtWidgets.QLineEdit, Ui_MainWindow):
    def __init__(self):
        super(Ventana, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.mostrar)
    """def mostrar(self):
        day = self.ui.lineEdit.text()
        month = self.ui.lineEdit2.text()
        year = self.ui.lineEdit3.text()
        fecha = year+month+day
        print(fecha)"""

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ventana()
    window.show()
    sys.exit(app.exec_())