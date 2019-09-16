import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QDialog, QTreeWidgetItem
from PySide2.QtCore import Qt

from controllers.main import MainWindow

if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_DisableWindowContextHelpButton)
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
