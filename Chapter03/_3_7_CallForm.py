#!usr/bin/python3
# -*- coding: utf-8 -*-

"""
标签里加图片

Lasted Edited: November 25, 2022
"""


from PyQt5.QtWidgets import QApplication, QMainWindow
from _3_7_Form import *
import sys


class Form(QMainWindow, Ui_Form):
    def __init__(self):
        super(Form, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    lw = Form()
    lw.show()
    sys.exit(app.exec_())