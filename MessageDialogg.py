# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'b.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DialogMessage(object):
    def __init__(self, Dialog):
        self.Dialog = Dialog

    def setupUi(self):
        self.Dialog.setObjectName(_fromUtf8("Dialog"))
        self.Dialog.resize(287, 110)
        self.label = QtGui.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 80, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(self.Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(80, 30, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        #QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clicked_button)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def retranslateUi(self):
        self.Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "输入密码：", None))
        self.pushButton.setText(_translate("Dialog", "OK", None))

    def clicked_button(self):
        print("a")
        self.Dialog.close()
        pass