import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from mainwindow import *

about_info = """Flight Stirp Manager by Kingfu Chan

For updates and instructions please visit
https://github.com/KingfuChan/Flight-Strip-Manager

Application built with Python(v3.6.6) and PyQt5(v5.14.1), under the license of GNU General Public License v2.0.
For non-commercial use only.
"""

_translate = QtCore.QCoreApplication.translate


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # initialize window and widgets
        self.setFixedWidth(371)
        self.setMinimumHeight(167)
        self.setupLists()
        self.actionOpac_Curr.setText(_translate(
            "MainWindow", f"Current: 100%"))
        self.exists = []
        self.count_total = 0
        self.count_depart = 0

    # overload events

    def resizeEvent(self, event):  # overload resize
        height = self.height()-self.menuBar.height()-self.list_dept.y()-10
        self.list_pend.setFixedHeight(height)
        self.list_push.setFixedHeight(height)
        self.list_dept.setFixedHeight(height)

    def closeEvent(self, event):  # confirm on exit
        confirm = QMessageBox.question(
            self, self.windowTitle(),
            _translate("MainWindow", "Are you sure to exit?"),
            QMessageBox.Ok | QMessageBox.Cancel)
        if confirm == QMessageBox.Ok:
            event.accept()
        else:
            event.ignore()

    # custom functions below

    def clickMenu(self, action):
        if action == self.actionExit:
            self.close()
        elif action == self.actionReset:
            self.resetLists()
        elif action == self.actionAbout:
            _about = QMessageBox.about(self, self.windowTitle(), about_info)
        elif action == self.actionStatistics:
            txt1 = _translate(
                "MainWindow", f"{len(self.exists)}\tflights operating.")
            txt2 = _translate(
                "MainWindow", f"{self.count_depart}\tflights departed.")
            txt3 = _translate(
                "MainWindow", f"{self.count_total}\tflights in total.")
            stat = '\n'.join((txt1, txt2, txt3))
            QMessageBox.information(self, self.windowTitle(), stat)
        elif action == self.actionOpac_Incr:
            opac = self.windowOpacity() + 0.10
            opac = round(opac, 1) if opac <= 1.00 else 1.00
            self.setWindowOpacity(opac)
            self.actionOpac_Curr.setText(_translate(
                "MainWindow", f"Current: {round(opac*100)}%"))
        elif action == self.actionOpac_Decr:
            opac = self.windowOpacity() - 0.10
            opac = round(opac, 1) if opac >= 0.10 else 0.10
            self.setWindowOpacity(opac)
            self.actionOpac_Curr.setText(_translate(
                "MainWindow", f"Current: {round(opac*100)}%"))
        elif action == self.actionOpac_Rest:
            self.setWindowOpacity(1.00)
            self.actionOpac_Curr.setText(
                _translate("MainWindow", f"Current: 100%"))
        elif action == self.actionStay_on_top:
            if self.actionStay_on_top.isChecked():
                self.setWindowFlags(self.windowFlags() |
                                    QtCore.Qt.WindowStaysOnTopHint)
            else:
                self.setWindowFlags(self.windowFlags() & ~
                                    QtCore.Qt.WindowStaysOnTopHint)
            self.show()

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
        confirm = QMessageBox.question(
            self, self.windowTitle(),
            _translate("MainWindow", "Are you sure to reset all lists?"),
            QMessageBox.Ok | QMessageBox.Cancel)
        if confirm != QMessageBox.Ok:
            return
        self.list_pend.clear()
        self.list_push.clear()
        self.list_dept.clear()
        self.setupLists()  # refill titles
        # clear stats
        self.exists = []
        self.count_total = 0
        self.count_depart = 0

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
            self.exists.remove(item.text())
            _delete = self.list_dept.takeItem(self.list_dept.row(item))
            self.count_depart += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    appwindow = MainWindow()
    appwindow.show()
    sys.exit(app.exec_())
