#!usr/bin/python3
# -*- coding: utf-8 -*-

"""
简单温习了。

Lasted Edited: November 25, 2022
"""


from PyQt5.QtWidgets import QApplication, QMainWindow
from _3_5_SignalSlotWin2 import *
import sys


class SignalSlotWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(SignalSlotWin, self).__init__()  # 看下super（）的用法
        self.setupUi(self)

        # # self.checkBox.clicked[bool].connect(self.label.setVisible)
        # self.checkBox.clicked[bool].connect(self.lineEdit.setEnabled)

        self.checkBox.clicked[bool].connect(self.clicked_checkBox)

        # self.checkBox.clicked.connect(self.on_checkBox_clicked)

    def clicked_checkBox(self, checked):  # 函数名用on_checkBox_clicked（）会出错
        self.label.setVisible(checked)
        self.lineEdit.setEnabled(checked)

    # def on_checkBox_clicked(self, checked):  # 这个函数有问题。多了checked这个参数就会有问题。感觉是这个函数名和参数的个数有冲突。
    #     self.label.setVisible(checked)

    # def on_checkBox_clicked(self):  # 这个就可以
    #     self.label.setVisible(self.checkBox.isChecked())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    lw = SignalSlotWin()
    lw.show()
    sys.exit(app.exec_())