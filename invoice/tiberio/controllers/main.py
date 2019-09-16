from PySide2.QtWidgets import QApplication, QMainWindow, QDialog, QTreeWidgetItem
from PySide2.QtCore import Qt, Slot

from views.ui_main import Ui_MainWindow
from controllers.invoice import FormInvoice


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())

        self.ui.actionInvoice.triggered.connect(self.show_ui_invoice)

    @Slot()
    def show_ui_invoice(self):
        ui_invoice = FormInvoice(self)
        ui_invoice.exec_()

