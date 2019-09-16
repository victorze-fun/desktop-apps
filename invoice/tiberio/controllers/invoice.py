from PySide2.QtWidgets import QDialog
from PySide2.QtCore import Slot, Qt

from controllers.search_customer import FormSearchCustomer
from controllers.product import FormProduct

from views.ui_invoice import Ui_Invoice


class FormInvoice(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Invoice()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.ui.treeProducts.setAlternatingRowColors(True)

        self.ui.cboDocType.addItem('Factura')
        self.ui.cboCurrency.addItem('Soles')

        self.set_col_width_tree_widget()

        self.ui.txtDocCustomer.returnPressed.connect(self.search_customer)
        self.ui.btnSave.clicked.connect(self.save_invoice)
        self.ui.btnCancel.clicked.connect(self.close)
        self.ui.btnItem.clicked.connect(self.open_form_product)


    def set_col_width_tree_widget(self):
        self.ui.treeProducts.setColumnWidth(0, 70)
        self.ui.treeProducts.setColumnWidth(1, 80)
        self.ui.treeProducts.setColumnWidth(2, 70)
        self.ui.treeProducts.setColumnWidth(3, 190)
        self.ui.treeProducts.setColumnWidth(4, 90)
        self.ui.treeProducts.setColumnWidth(5, 90)

    @Slot()
    def open_form_product(self):
        ui_product = FormProduct(self)
        ui_product.exec_()

    @Slot()
    def search_customer(self):
        print('search')
        ui_cliente = FormSearchCustomer(self)
        ui_cliente.exec_()

    @Slot()
    def save_invoice(self):
        print('Saved invoice')

