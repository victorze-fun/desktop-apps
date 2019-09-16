from PySide2.QtWidgets import QDialog
from PySide2.QtCore import Slot

from views.ui_search_customer import Ui_SearchCustomer


class FormSearchCustomer(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.ui = Ui_SearchCustomer()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())

        self.set_col_width_tree_widget()

        self.ui.treeCustomers.itemDoubleClicked.connect(self.get_customer)

    @Slot()
    def get_customer(self, item):
        self.parent.ui.txtDocCustomer.setText(item.text(0))
        self.parent.ui.lblNameCustomer.setText(item.text(1))
        self.close()

    def set_col_width_tree_widget(self):
        self.ui.treeCustomers.setColumnWidth(0, 90)
        self.ui.treeCustomers.setColumnWidth(1, 230)

