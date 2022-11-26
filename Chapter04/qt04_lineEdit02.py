#!usr/bin/python3
# -*- coding: utf-8 -*-

"""
indentation  n.缩进
notation  n.记号

验证器的使用。

Lasted Edited: Nov 25, 2022
"""

from PyQt5.QtWidgets import QApplication,  QLineEdit , QWidget ,  QFormLayout
from PyQt5.QtGui import QIntValidator ,QDoubleValidator  , QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys  


class lineEditDemo(QWidget):
	def __init__(self, parent=None):
		super(lineEditDemo, self).__init__(parent)
		self.setWindowTitle("setEchoMode()")

		formly = QFormLayout(self)

		IntLE = QLineEdit(self)  # 表单布局
		IntLE.setPlaceholderText("整形")
		IntLEV = QIntValidator(self)  # 创建验证器
		IntLEV.setRange(1, 99)
		IntLE.setValidator(IntLEV)  # 设置验证器

		DoubleLE = QLineEdit(self)
		DoubleLE.setPlaceholderText("浮点型")
		DoubleLEV = QDoubleValidator(self)
		DoubleLEV.setRange(-100, 100)  # 这个没限制到，要用的时候再搜下
		DoubleLEV.setNotation(QDoubleValidator.StandardNotation)
		DoubleLEV.setDecimals(2)
		DoubleLE.setValidator(DoubleLEV)

		LE = QLineEdit(self)
		LE.setPlaceholderText("数字和字母")
		LEV = QRegExpValidator(self)
		reg = QRegExp("[a-zA-Z0-9] + $")
		LEV.setRegExp(reg)
		LE.setValidator(LEV)

		formly.addRow("整形", IntLE)
		formly.addRow("浮点型", DoubleLE)
		formly.addRow("字符和字母", LE)

		self.setLayout(formly)


if __name__ == "__main__":       
	app = QApplication(sys.argv)
	win = lineEditDemo()	
	win.show()	
	sys.exit(app.exec_())
