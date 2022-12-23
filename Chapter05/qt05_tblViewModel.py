#!usr/bin/python3
# -*- coding: utf-8 -*-

"""
表视图。

字符串格式化参考：https://cloud.tencent.com/developer/article/1640697

Lasted Edited: Nov 26, 2022
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Table(QWidget):
	def __init__(self, arg=None):
		super(Table, self).__init__()
		self.setGeometry(600, 400, 650, 350)
		self.model = QStandardItemModel(4, 4)
		self.model.setHorizontalHeaderLabels(['1', '2', '3', '4'])
		for i in range(4):
			for j in range(4):
				item = QStandardItem("%d行，%d列" % (i, j))  # 也可以使用("{}行，{}列".format(i, j))
				self.model.setItem(i, j, item)

		self.tv = QTableView(self)
		self.tv.setGeometry(0, 0, 600, 300)
		self.tv.setModel(self.model)


if __name__ == '__main__':
	app = QApplication(sys.argv)	
	table = Table()
	table.show()
	sys.exit(app.exec_())
