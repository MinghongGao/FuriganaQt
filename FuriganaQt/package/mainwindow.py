from PyQt5 import QtWidgets

from FuriganaQt.package.ui.mainwindow_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, config):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.config = config
