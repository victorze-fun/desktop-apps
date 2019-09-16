# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Fri Feb 15 11:59:36 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(366, 220)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 366, 21))
        self.menubar.setObjectName("menubar")
        self.menuOperaciones = QtWidgets.QMenu(self.menubar)
        self.menuOperaciones.setObjectName("menuOperaciones")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionInvoice = QtWidgets.QAction(MainWindow)
        self.actionInvoice.setObjectName("actionInvoice")
        self.menuOperaciones.addAction(self.actionInvoice)
        self.menubar.addAction(self.menuOperaciones.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Gestión de inventarios", None, -1))
        self.menuOperaciones.setTitle(QtWidgets.QApplication.translate("MainWindow", "Operaciones", None, -1))
        self.actionInvoice.setText(QtWidgets.QApplication.translate("MainWindow", "Compra", None, -1))

