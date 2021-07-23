from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui,self).__init__()
        uic.loadUi('untitled.ui', self)
        self.showMaximized()

    def mensajeImportante():
        msg = QMessageBox()
        msg.setWindowTitle("Aviso Legal")
        msg.setText("Aviso Legal. Haga click en 'Mostrar Detalles...' para saber más.")
        msg.setDetailedText(
            "Esta es una aplicación propiedad de INVEPAT GO SL.\n Con sede en Avenida Ronda de los Tejadres Nº 27, Córdoba.\n La difusión de esta aplicación así como su contenido y funcionalidad, fuera del entorno INVEPAT GO SL., está totalmente prohibido.")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()