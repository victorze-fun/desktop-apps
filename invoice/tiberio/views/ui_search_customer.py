# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_customer.ui',
# licensing of 'search_customer.ui' applies.
#
# Created: Tue Feb 19 17:55:56 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SearchCustomer(object):
    def setupUi(self, SearchCustomer):
        SearchCustomer.setObjectName("SearchCustomer")
        SearchCustomer.resize(471, 282)
        self.treeCustomers = QtWidgets.QTreeWidget(SearchCustomer)
        self.treeCustomers.setGeometry(QtCore.QRect(10, 10, 451, 261))
        self.treeCustomers.setIndentation(0)
        self.treeCustomers.setColumnCount(2)
        self.treeCustomers.setObjectName("treeCustomers")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeCustomers)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeCustomers)

        self.retranslateUi(SearchCustomer)
        QtCore.QMetaObject.connectSlotsByName(SearchCustomer)

    def retranslateUi(self, SearchCustomer):
        SearchCustomer.setWindowTitle(QtWidgets.QApplication.translate("SearchCustomer", "Cliente", None, -1))
        self.treeCustomers.headerItem().setText(0, QtWidgets.QApplication.translate("SearchCustomer", "RUC", None, -1))
        self.treeCustomers.headerItem().setText(1, QtWidgets.QApplication.translate("SearchCustomer", "Razón Social", None, -1))
        __sortingEnabled = self.treeCustomers.isSortingEnabled()
        self.treeCustomers.setSortingEnabled(False)
        self.treeCustomers.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("SearchCustomer", "20451512027", None, -1))
        self.treeCustomers.topLevelItem(0).setText(1, QtWidgets.QApplication.translate("SearchCustomer", "HARDTECH SOLUTIONS S.A.C.", None, -1))
        self.treeCustomers.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("SearchCustomer", "20453318040", None, -1))
        self.treeCustomers.topLevelItem(1).setText(1, QtWidgets.QApplication.translate("SearchCustomer", "CORPORACION GRUPONET S.A.C.", None, -1))
        self.treeCustomers.setSortingEnabled(__sortingEnabled)

