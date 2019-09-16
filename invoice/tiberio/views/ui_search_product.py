# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_product.ui',
# licensing of 'search_product.ui' applies.
#
# Created: Tue Feb 19 19:09:33 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SearchProduct(object):
    def setupUi(self, SearchProduct):
        SearchProduct.setObjectName("SearchProduct")
        SearchProduct.resize(501, 279)
        self.treeProducts = QtWidgets.QTreeWidget(SearchProduct)
        self.treeProducts.setGeometry(QtCore.QRect(10, 10, 481, 261))
        self.treeProducts.setIndentation(0)
        self.treeProducts.setObjectName("treeProducts")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeProducts)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeProducts)

        self.retranslateUi(SearchProduct)
        QtCore.QMetaObject.connectSlotsByName(SearchProduct)

    def retranslateUi(self, SearchProduct):
        SearchProduct.setWindowTitle(QtWidgets.QApplication.translate("SearchProduct", "Productos", None, -1))
        self.treeProducts.headerItem().setText(0, QtWidgets.QApplication.translate("SearchProduct", "Descripción", None, -1))
        self.treeProducts.headerItem().setText(1, QtWidgets.QApplication.translate("SearchProduct", "Unid. Med.", None, -1))
        self.treeProducts.headerItem().setText(2, QtWidgets.QApplication.translate("SearchProduct", "Precio Unitario", None, -1))
        __sortingEnabled = self.treeProducts.isSortingEnabled()
        self.treeProducts.setSortingEnabled(False)
        self.treeProducts.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("SearchProduct", "Laptop Lenovo 720-15ikb Intel I7-8550u", None, -1))
        self.treeProducts.topLevelItem(0).setText(1, QtWidgets.QApplication.translate("SearchProduct", "Unidades", None, -1))
        self.treeProducts.topLevelItem(0).setText(2, QtWidgets.QApplication.translate("SearchProduct", "4,400.00", None, -1))
        self.treeProducts.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("SearchProduct", "Laptop Lenovo Legion Y530 Core I7-8750h", None, -1))
        self.treeProducts.topLevelItem(1).setText(1, QtWidgets.QApplication.translate("SearchProduct", "Unidades", None, -1))
        self.treeProducts.topLevelItem(1).setText(2, QtWidgets.QApplication.translate("SearchProduct", "5,000.00", None, -1))
        self.treeProducts.setSortingEnabled(__sortingEnabled)

