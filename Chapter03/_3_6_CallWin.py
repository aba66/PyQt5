#!usr/bin/python3
# -*- coding: utf-8 -*-

"""
Lasted Edited: November 25, 2022
"""


from PyQt5.QtWidgets import QApplication, QMainWindow
from _3_6_Win import *
from _3_6_ChildForm import *
import sys


class Win(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Win, self).__init__()
        self.setupUi(self)
        self.child = ChildrenWin()
        self.addWinAction.triggered.connect(self.child_show)

    def child_show(self):
        self.MaingridLayout.addWidget(self.child)
        self.child.show()


class ChildrenWin(QMainWindow, Ui_Form):
    def __init__(self):
        super(ChildrenWin, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    lw = Win()
    lw.show()
    sys.exit(app.exec_())