#!usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QMainWindow
from _3_1_layoutWin import *
import sys

class LayoutWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(LayoutWin, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    lw = LayoutWin()
    lw.show()
    sys.exit(app.exec_())