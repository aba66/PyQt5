#!usr/bin/python3
# -*- coding: utf-8 -*-

"""
表组件。

Lasted Edited: Nov 26, 2022
"""

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem, QAbstractItemView  )

class Table(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle("QTableWidget 例子")
		self.resize(430,230);
		self.tw = QTableWidget(self)
		self.tw.setGeometry(0, 0, 400, 200)
		self.tw.setRowCount(4)
		self.tw.setColumnCount(3)
		self.tw.setHorizontalHeaderLabels(["Name", "Sex", "Weight(Kg)"])
		twi = QTableWidgetItem("zhangsan")
		self.tw.setItem(0, 0, twi)
		twi = QTableWidgetItem("M")
		self.tw.setItem(0, 1, twi)
		twi = QTableWidgetItem("65")
		self.tw.setItem(0, 2, twi)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = Table()  
	example.show()   
	sys.exit(app.exec_())
