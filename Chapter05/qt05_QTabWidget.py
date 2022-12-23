#!usr/bin/python3
# -*- coding: utf-8 -*-

"""
标签组件，可以在消息和好友列表之间切换。

Lasted Edited: Nov 26, 2022
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class TabDemo(QTabWidget):
	def __init__(self, parent=None):
		super(TabDemo, self).__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(600, 400, 650, 350)

		self.tab1 = QWidget(self)
		self.init_tab1()
		self.addTab(self.tab1, "tab1")

		self.tab2 = QWidget(self)
		self.addTab(self.tab2, "tab2")
		self.init_tab2()

		self.tab3 = QWidget(self)
		self.addTab(self.tab3, "tab3")
		self.init_tab3()

	def init_tab1(self):
		fl = QFormLayout()
		fl.addRow("Name", QLineEdit())
		self.tab1.setLayout(fl)

	def init_tab2(self):
		fl = QFormLayout()
		hbox = QHBoxLayout()
		hbox.addWidget(QRadioButton("Male"))
		hbox.addWidget(QRadioButton("Female"))
		fl.addRow("Sex", hbox)
		self.tab2.setLayout(fl)

	def init_tab3(self):
		fl = QFormLayout()
		hbox = QHBoxLayout()
		hbox.addWidget(QCheckBox("math"))
		hbox.addWidget(QCheckBox("physics"))
		fl.addRow("Course", hbox)
		self.tab3.setLayout(fl)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = TabDemo()
	demo.show()
	sys.exit(app.exec_())
