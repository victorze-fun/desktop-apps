from PySide2.QtWidgets import QDialog
from PySide2.QtCore import Slot, Qt

from views.ui_search_product import Ui_SearchProduct


class FormSearchProduct(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.ui = Ui_SearchProduct()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())

        self.set_col_width_tree_widget()

        self.ui.treeProducts.itemDoubleClicked.connect(self.get_product)

    @Slot()
    def get_product(self, item):
        self.parent.ui.txtDescription.setText(item.text(0))
        self.parent.ui.txtUnitPrice.setText(item.text(2))
        self.close()

    def set_col_width_tree_widget(self):
        self.ui.treeProducts.setColumnWidth(0, 280)
        self.ui.treeProducts.setColumnWidth(1, 90)
        self.ui.treeProducts.setColumnWidth(2, 90)

