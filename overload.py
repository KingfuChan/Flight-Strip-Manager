import re

from PyQt5 import QtCore, QtGui, QtWidgets

brush_back_default = QtGui.QBrush(QtGui.QColor(255, 255, 255))
brush_back_default.setStyle(QtCore.Qt.NoBrush)

brush_fore_default = QtGui.QBrush(QtGui.QColor(0, 0, 0))
brush_fore_default.setStyle(QtCore.Qt.NoBrush)


class CustomListWidget(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super(CustomListWidget, self).__init__(parent)
        self.customContextMenuRequested[QtCore.QPoint].connect(
            self.showContext)

    def dropEvent(self, event):
        row = self.currentRow()
        print(row)
        # scan list before dropped
        before = [self.item(i).text() for i in range(self.count())]
        super(CustomListWidget, self).dropEvent(event)
        print(self.currentRow())
        # scan list after dropped
        after = [self.item(i).text() for i in range(self.count())]
        # find difference
        i = 0
        while i < len(before):
            if before[i] == after[i]:
                i += 1
                continue
            else:
                if sorted(before) != sorted(after):
                    # drag&drop in different list, add to bottom
                    temp = self.takeItem(i)
                    temp.setBackground(brush_back_default)
                    temp.setForeground(brush_fore_default)
                    self.addItem(temp)
                elif i == 0:  
                    # drag&drop in same list, drop to top
                    temp = self.takeItem(i)
                    self.insertItem(row, temp)
                break

    def enterEvent(self, event):  # clears all selections to beautify
        super(CustomListWidget, self).enterEvent(event)
        self.clearSelection()

    def showContext(self, pos):
        row = self.row(self.itemAt(pos))
        if row <= 0:  # clicked on title
            return
        popMenu = QtWidgets.QMenu(self)
        resetAction = QtWidgets.QAction("Reset")
        deleteAction = QtWidgets.QAction("Delete")
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
