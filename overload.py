import re

from PyQt5 import QtCore, QtGui, QtWidgets

_translate = QtCore.QCoreApplication.translate

# brushes
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


class CustomListWidget(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super(CustomListWidget, self).__init__(parent)
        self.customContextMenuRequested[QtCore.QPoint].connect(
            self.showContext)

    def dropEvent(self, event):
        row = self.currentRow()
        # scan list before dropped
        before = [self.item(i).text() for i in range(self.count())]
        super(CustomListWidget, self).dropEvent(event)
        # scan list after dropped
        after = [self.item(i).text() for i in range(self.count())]
        # find difference
        i = 0
        if sorted(before) == sorted(after):  # drag&drop in same list
            if before[0] != after[0]:
                temp = self.takeItem(0)
                self.insertItem(row, temp)
        else:  # drag&drop between different list
            while i < len(before) and before[i] == after[i]:
                i += 1  # locate difference
            temp = self.takeItem(i)
            temp.setBackground(brush_back_default)
            temp.setForeground(brush_fore_default)
            self.addItem(temp)

    def enterEvent(self, event):  # clears all selections to beautify
        super(CustomListWidget, self).enterEvent(event)
        self.clearSelection()

    def showContext(self, pos):
        row = self.row(self.itemAt(pos))
        if row <= 0:  # clicked on title
            return

        # calculate sequence
        seq = 1
        for r in range(1, row):
            if self.item(r).background() == brush_back_default:
                seq += 1
        if self.item(row).background() == brush_back_changed:
            seq = 0

        # add menu actions
        popMenu = QtWidgets.QMenu(self)
        seqAction = QtWidgets.QAction()
        seqAction.setText(_translate("MainWindow", f"Seq: {seq}"))
        seqAction.setEnabled(False)
        resetAction = QtWidgets.QAction()
        resetAction.setText(_translate("MainWindow", "Reset"))
        deleteAction = QtWidgets.QAction()
        deleteAction.setText(_translate("MainWindow", "Delete"))
        popMenu.addAction(seqAction)
        popMenu.addSeparator()
        popMenu.addAction(resetAction)
        popMenu.addAction(deleteAction)
        action = popMenu.exec_(QtGui.QCursor.pos())

        # when clicked on the menu
        if action == resetAction:
            item = self.takeItem(row)
            self.parent().parent().addFlight(item.text())  # my grandparent is MainWindow
        elif action == deleteAction:
            item = self.takeItem(row)


class CustomLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super(CustomLineEdit, self).__init__(parent)
        self.setValidator(QtGui.QRegExpValidator(
            QtCore.QRegExp(u"[A-Za-z0-9]*")))
        self.textEdited['QString'].connect(self.capitalize)

    def keyPressEvent(self, event):
        if event.key() == 16777216:  # esc key
            self.clear()
        else:
            super(CustomLineEdit, self).keyPressEvent(event)

    def capitalize(self, string):
        string = string.upper()
        self.setText(string)
