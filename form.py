# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from overload import CustomLineEdit,CustomListWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 601)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(50.0)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(130, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName("btn_add")
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setGeometry(QtCore.QRect(250, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_reset.setFont(font)
        self.btn_reset.setObjectName("btn_reset")
        self.list_pend = CustomListWidget(self.centralwidget)
        self.list_pend.setGeometry(QtCore.QRect(10, 50, 111, 421))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.list_pend.setFont(font)
        self.list_pend.setDragEnabled(True)
        self.list_pend.setDragDropOverwriteMode(False)
        self.list_pend.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.list_pend.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.list_pend.setObjectName("list_pend")
        self.list_push = CustomListWidget(self.centralwidget)
        self.list_push.setGeometry(QtCore.QRect(130, 50, 111, 421))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.list_push.setFont(font)
        self.list_push.setDragEnabled(True)
        self.list_push.setDragDropOverwriteMode(False)
        self.list_push.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.list_push.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.list_push.setObjectName("list_push")
        self.list_dept = CustomListWidget(self.centralwidget)
        self.list_dept.setGeometry(QtCore.QRect(250, 50, 111, 421))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.list_dept.setFont(font)
        self.list_dept.setDragEnabled(True)
        self.list_dept.setDragDropOverwriteMode(False)
        self.list_dept.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.list_dept.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.list_dept.setObjectName("list_dept")
        self.lineEdit = CustomLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setMaxLength(10)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_add.clicked.connect(MainWindow.addFlight)
        self.btn_reset.clicked.connect(MainWindow.resetLists)
        self.lineEdit.returnPressed.connect(self.btn_add.click)
        self.list_push.itemDoubleClicked['QListWidgetItem*'].connect(MainWindow.setStatusClr)
        self.list_dept.itemDoubleClicked['QListWidgetItem*'].connect(MainWindow.setStatusDep)
        self.list_pend.itemDoubleClicked['QListWidgetItem*'].connect(MainWindow.setStatusClr)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.btn_add)
        MainWindow.setTabOrder(self.btn_add, self.list_pend)
        MainWindow.setTabOrder(self.list_pend, self.list_push)
        MainWindow.setTabOrder(self.list_push, self.list_dept)
        MainWindow.setTabOrder(self.list_dept, self.btn_reset)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Flight Strip Manager"))
        self.btn_add.setText(_translate("MainWindow", "ADD"))
        self.btn_reset.setText(_translate("MainWindow", "RESET"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Callsign"))