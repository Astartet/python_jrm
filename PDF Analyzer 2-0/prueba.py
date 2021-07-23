# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\prueba.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
import os
from time import sleep


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

    def mensaje(self, MainWindow):
        msg = QtWidgets.QMessageBox()
        msg.setText("Texto de prueba")
        msg.setDetailedText("Texto de prueba detallado")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msg.exec_()
    def andalucia(self, MainWindow):
        day = "08"
        month = "07"
        year = "2021"
        fecha = day+month+year
        directorio = "Descargas"
        if os.path.exists(directorio+"/"+fecha):
            pass
        else:
            os.makedirs(directorio+"/"+fecha)  
        url = "https://www.juntadeandalucia.es/eboja/buscador/search.do?fd=fd&eboja=on&q=&startDate="+year+"-"+month+"-"+day+"&endDate="+year+"-"+month+"-"+day+"&type=&section=&organisation=&ordenacion="

        options = webdriver.ChromeOptions()
        prefs = {'download.default_directory':'C:\\Users\\Usuario\\Desktop\\Proyectos_Invepat\\Repositorio\\pdf_analyzer_invepat\\PDF Analyzer 2-0\\'+directorio+"\\"+fecha, 'download.prompt_for_download':False, 'plugins.always_open_pdf_externally':True}
        options.add_experimental_option('prefs',prefs)
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        sleep(2)
        enlace = driver.find_element_by_css_selector("ul.listado_resultados li div.mb-4 a")
        enlace.click()

        pdf = driver.find_element_by_css_selector("ul.listado_pdf li.item a")
        pdf.click()
        sleep(15)
        driver.quit()



"""if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())"""
