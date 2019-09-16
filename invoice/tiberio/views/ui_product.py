# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'product.ui',
# licensing of 'product.ui' applies.
#
# Created: Tue Feb 19 19:07:27 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Product(object):
    def setupUi(self, Product):
        Product.setObjectName("Product")
        Product.resize(541, 126)
        self.label = QtWidgets.QLabel(Product)
        self.label.setGeometry(QtCore.QRect(20, 24, 58, 13))
        self.label.setObjectName("label")
        self.txtDescription = QtWidgets.QLineEdit(Product)
        self.txtDescription.setGeometry(QtCore.QRect(90, 20, 431, 20))
        self.txtDescription.setObjectName("txtDescription")
        self.txtQuantity = QtWidgets.QLineEdit(Product)
        self.txtQuantity.setGeometry(QtCore.QRect(90, 50, 81, 20))
        self.txtQuantity.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtQuantity.setObjectName("txtQuantity")
        self.label_2 = QtWidgets.QLabel(Product)
        self.label_2.setGeometry(QtCore.QRect(20, 54, 47, 13))
        self.label_2.setObjectName("label_2")
        self.txtUnitPrice = QtWidgets.QLineEdit(Product)
        self.txtUnitPrice.setGeometry(QtCore.QRect(270, 50, 91, 20))
        self.txtUnitPrice.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtUnitPrice.setObjectName("txtUnitPrice")
        self.label_3 = QtWidgets.QLabel(Product)
        self.label_3.setGeometry(QtCore.QRect(190, 54, 73, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Product)
        self.label_4.setGeometry(QtCore.QRect(380, 54, 33, 13))
        self.label_4.setObjectName("label_4")
        self.txtTotal = QtWidgets.QLineEdit(Product)
        self.txtTotal.setGeometry(QtCore.QRect(420, 50, 101, 20))
        self.txtTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtTotal.setObjectName("txtTotal")
        self.btnAdd = QtWidgets.QPushButton(Product)
        self.btnAdd.setGeometry(QtCore.QRect(150, 90, 75, 23))
        self.btnAdd.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnAdd.setObjectName("btnAdd")
        self.btnCancel = QtWidgets.QPushButton(Product)
        self.btnCancel.setGeometry(QtCore.QRect(320, 90, 75, 23))
        self.btnCancel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnCancel.setObjectName("btnCancel")

        self.retranslateUi(Product)
        QtCore.QMetaObject.connectSlotsByName(Product)

    def retranslateUi(self, Product):
        Product.setWindowTitle(QtWidgets.QApplication.translate("Product", "Producto", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Product", "Descripción:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Product", "Cantidad:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Product", "Precio Unitario:", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Product", "Total:", None, -1))
        self.btnAdd.setText(QtWidgets.QApplication.translate("Product", "Agregar", None, -1))
        self.btnCancel.setText(QtWidgets.QApplication.translate("Product", "Cancelar", None, -1))

