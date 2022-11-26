#!usr/bin/python3
# -*- coding: utf-8 -*-

"""
QLineEdit
setEchoMode()方法的使用。  应用场景有很多啊，比如：用来生成是否显示密码的文本框等。

Lasted Edited: November 25, 2022
"""

from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
import sys  


class lineEditDemo(QWidget):
	def __init__(self, parent=None):
		super(lineEditDemo, self).__init__(parent)
		self.setWindowTitle("setEchoMode()")

		formly = QFormLayout(self)

		NormalLE = QLineEdit(self)  # 表单布局
		NormalLE.setPlaceholderText("Normal")  # 该文本框未输入字符时，显示字符串"Normal"
		NormalLE.setEchoMode(QLineEdit.Normal)
		NoEchoLE = QLineEdit(self)
		NoEchoLE.setPlaceholderText("NoEcho")
		NoEchoLE.setEchoMode(QLineEdit.NoEcho)
		PasswordLE = QLineEdit(self)
		PasswordLE.setPlaceholderText("Password")
		PasswordLE.setEchoMode(QLineEdit.Password)
		PasswordEchoOnEditLE = QLineEdit(self)  # 可以用来生成是否显示密码的文本框
		PasswordEchoOnEditLE.setPlaceholderText("PasswordEchoOnEdit")
		PasswordEchoOnEditLE.setEchoMode(QLineEdit.PasswordEchoOnEdit)

		formly.addRow("Normal", NormalLE)
		formly.addRow("NoEcho", NoEchoLE)
		formly.addRow("Password", PasswordLE)
		formly.addRow("PasswordEchoOnEdit", PasswordEchoOnEditLE)

		self.setLayout(formly)


if __name__ == "__main__":       
	app = QApplication(sys.argv)
	win = lineEditDemo()	
	win.show()	
	sys.exit(app.exec_())
