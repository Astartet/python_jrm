import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
import glob

def mensaje():
    """msg = QMessageBox()
    msg.setText("Texto de prueba")
    msg.setDetailedText("Texto de prueba detallado")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.exec_()"""
    print("hola")
def mensajeImportante():
    msg = QMessageBox()
    msg.setWindowTitle("Aviso Legal")
    msg.setText("Aviso Legal. Haga click en 'Mostrar Detalles...' para saber más.")
    msg.setDetailedText("Esta es una aplicación propiedad de INVEPAT GO SL.\n Con sede en Avenida Ronda de los Tejadres Nº 27, Córdoba.\n La difusión de esta aplicación así como su contenido y funcionalidad, fuera del entorno INVEPAT GO SL., está totalmente prohibido.")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.exec_()

app = QApplication(sys.argv)
window = QWidget()
window.resize(1920,1080)
window.setWindowTitle("TOOLPAT")
#window.setStyleSheet("background-color: #041e42")
label = QLabel(window)
label.setText("TOOLPAT")
label.move(550,100)
label.setStyleSheet("color: white; border: 1px solid white; text-align: center;")
label.resize(265,150)
label.setFont(QFont('Arial', 20))
label.show()
























# Aviso Legal Boton
bl = QPushButton(window)
bl.setText("Aviso Legal")
bl.show()
bl.clicked.connect(mensajeImportante)
window.showMaximized()
sys.exit(app.exec_())