import logging
import sys

from PyQt5 import QtWidgets, QtGui

from FuriganaQt.package import constants
from FuriganaQt.package.base import create_config
from FuriganaQt.package.mainwindow import MainWindow

logger = logging.getLogger(__name__)


class App:
    def __init__(self):
        self.config = create_config()
        self.app = QtWidgets.QApplication(sys.argv)

        # set app icon
        self.app.setWindowIcon(QtGui.QIcon(constants.PATH_APP_ICON))

        # set title
        self.app.setApplicationName(constants.STR_WINDOW_TITLE)

        self.window = MainWindow(self.config)

    def run(self):
        logger.info('Program run')
        self.window.show()
        self.app.exec_()
