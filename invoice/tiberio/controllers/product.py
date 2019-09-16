from PySide2.QtWidgets import QDialog, QTreeWidgetItem
from PySide2.QtCore import Slot, Qt

from views.ui_product import Ui_Product
from controllers.search_product import FormSearchProduct


class FormProduct(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.ui = Ui_Product()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())

        self.ui.txtDescription.returnPressed.connect(self.search_product)
        self.ui.txtQuantity.returnPressed.connect(self.modify_txt)
        self.ui.btnCancel.clicked.connect(self.close)
        self.ui.btnAdd.clicked.connect(self.add_product)

    @Slot()
    def search_product(self):
        ui_searchProduct = FormSearchProduct(self)
        ui_searchProduct.exec_()

    @Slot()
    def add_product(self):
        f = QTreeWidgetItem(self.parent.ui.treeProducts, [
            '15012',
            self.ui.txtQuantity.text(),
            'Unidades',
            self.ui.txtDescription.text(),
            self.ui.txtUnitPrice.text(),
            self.ui.txtTotal.text(),
        ])

        f.setTextAlignment(1, Qt.AlignRight)
        f.setTextAlignment(4, Qt.AlignRight)
        f.setTextAlignment(5, Qt.AlignRight)

        self.set_others_values()

        self.close()

    def set_others_values(self):
        self.parent.ui.lblTotalLetters.setText('SON CINCUENTA MIL CON 00/100 SOLES')
        self.parent.ui.lblTotal.setText('50,000.00')
        self.parent.ui.lblTax.setText('7,627.12')
        self.parent.ui.lblSubTotal.setText('42,372.88')

    def modify_txt(self):
        self.ui.txtQuantity.setText('10.00')
        self.ui.txtTotal.setText('50,000.00')

