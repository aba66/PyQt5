#!usr/bin/python3
# -*- coding: utf-8 -*-

"""
树型组件，那可以用来做好友列表啊。

Lasted Edited: Nov 26, 2022
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon ,  QBrush , QColor
from PyQt5.QtCore import Qt 


class TreeWidgetDemo(QMainWindow):   
	def __init__(self,parent=None):
		super(TreeWidgetDemo, self).__init__()
		self.setGeometry(600, 400, 650, 350)

		self.tw = QTreeWidget(self)
		self.tw.setColumnCount(2)
		self.tw.setHeaderLabels(['key', 'value'])
		self.tw.setGeometry(0, 0, 600, 300)

		# 设置根结点
		root = QTreeWidgetItem(self.tw)
		root.setText(0, 'root')

		# 设置结点
		node1 = QTreeWidgetItem(root)
		node1.setText(0, 'child1')
		node1.setText(1, 'ios')
		node1.setCheckState(0, Qt.Checked)

		# 设置结点
		node2 = QTreeWidgetItem(root)
		node2.setText(0, 'child2')

		# 设置结点
		node3 = QTreeWidgetItem(node2)
		node3.setText(0, 'child3')
		node3.setText(1, 'android')

		self.tw.addTopLevelItem(root)
		self.tw.expandAll()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	tree = TreeWidgetDemo()
	tree.show()
	sys.exit(app.exec_())
