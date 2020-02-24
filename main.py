import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from form import Ui_MainWindow

_translate = QtCore.QCoreApplication.translate

brush_back_default = QtGui.QBrush(QtGui.QColor(255, 255, 255))
brush_back_default.setStyle(QtCore.Qt.NoBrush)

brush_back_changed = QtGui.QBrush(QtGui.QColor(0, 170, 0))
brush_back_changed.setStyle(QtCore.Qt.SolidPattern)

brush_fore_default = QtGui.QBrush(QtGui.QColor(0, 0, 0))
brush_fore_default.setStyle(QtCore.Qt.NoBrush)

brush_fore_changed = QtGui.QBrush(QtGui.QColor(255, 255, 255))
brush_fore_changed.setStyle(QtCore.Qt.NoBrush)

brush_back_title = QtGui.QBrush(QtGui.QColor(0, 0, 0))
brush_back_title.setStyle(QtCore.Qt.SolidPattern)

brush_fore_title = QtGui.QBrush(QtGui.QColor(255, 255, 255))
brush_fore_title.setStyle(QtCore.Qt.NoBrush)


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # initialize window and widgets
        self.setFixedWidth(371)
        self.setMinimumHeight(167)
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setupLists()
        self.exists = []

    def resizeEvent(self, event):  # overload resize
        height = self.height()-86
        self.list_pend.setFixedHeight(height)
        self.list_push.setFixedHeight(height)
        self.list_dept.setFixedHeight(height)

    # custom functions below
    def clickMenu(self):
        pass

    def setupLists(self):
        item_title = QtWidgets.QListWidgetItem()
        item_title.setBackground(brush_back_title)
        item_title.setForeground(brush_fore_title)
        item_title.setFlags(QtCore.Qt.NoItemFlags)

        item = QtWidgets.QListWidgetItem(item_title)
        item.setText(_translate("MainWindow", "Clearance"))
        self.list_pend.addItem(item)

        item = QtWidgets.QListWidgetItem(item_title)
        item.setText(_translate("MainWindow", "Push&Start"))
        self.list_push.addItem(item)

        item = QtWidgets.QListWidgetItem(item_title)
        item.setText(_translate("MainWindow", "Departure"))
        self.list_dept.addItem(item)

    def addFlight(self, callsign=''):
        if not callsign:
            callsign = self.lineEdit.text()
            if callsign and callsign not in self.exists:
                item = QtWidgets.QListWidgetItem()
                item.setText(callsign)
                item.setBackground(brush_back_default)
                item.setForeground(brush_fore_default)
                self.list_pend.addItem(item)
                self.exists.append(callsign)
            self.lineEdit.clear()
        else:
            item = QtWidgets.QListWidgetItem()
            item.setText(callsign)
            item.setBackground(brush_back_default)
            item.setForeground(brush_fore_default)
            self.list_pend.addItem(item)

    def resetLists(self):
        self.list_pend.clear()
        self.list_push.clear()
        self.list_dept.clear()
        self.setupLists()  # refill titles

    def setStatusClr(self, item):  # switch status
        if item.background() == brush_back_default:
            item.setBackground(brush_back_changed)
            item.setForeground(brush_fore_changed)
        elif item.background() == brush_back_changed:
            item.setBackground(brush_back_default)
            item.setForeground(brush_fore_default)

    def setStatusDep(self, item):
        if item.background() == brush_back_default:
            item.setBackground(brush_back_changed)
            item.setForeground(brush_fore_changed)
        elif item.background() == brush_back_changed:
            _delete = self.list_dept.takeItem(self.list_dept.row(item))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    appwindow = MainWindow()
    appwindow.show()
    sys.exit(app.exec_())
