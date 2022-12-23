import sys
from PyQt5 import QtCore, QtGui, QtWidgets


# or
# from PySide2 import QtCore, QtGui, QtWidgets


class ComboBox(QtWidgets.QComboBox):
    # https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/widgets/qcombobox.cpp?h=5.15.2#n3173
    def paintEvent(self, event):

        painter = QtWidgets.QStylePainter(self)
        painter.setPen(self.palette().color(QtGui.QPalette.Text))

        # draw the combobox frame, focusrect and selected etc.
        opt = QtWidgets.QStyleOptionComboBox()
        self.initStyleOption(opt)
        painter.drawComplexControl(QtWidgets.QStyle.CC_ComboBox, opt)

        if self.currentIndex() < 0:
            opt.palette.setBrush(
                QtGui.QPalette.ButtonText,
                opt.palette.brush(QtGui.QPalette.ButtonText).color().lighter(),
            )
            if self.placeholderText():
                opt.currentText = self.placeholderText()

        # draw the icon and text
        painter.drawControl(QtWidgets.QStyle.CE_ComboBoxLabel, opt)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.combo_box = ComboBox()
        self.combo_box.addItems(["one", "two", "three"])
        self.combo_box.setPlaceholderText("Some placeholder text here")
        self.combo_box.setCurrentIndex(-1)

        central_w = QtWidgets.QWidget()
        self.setCentralWidget(central_w)
        vbox = QtWidgets.QVBoxLayout(central_w)
        vbox.addWidget(self.combo_box)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()