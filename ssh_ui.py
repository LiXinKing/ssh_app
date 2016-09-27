# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ssh.ui'
#
# Created: Sun Sep 25 20:59:05 2016
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
from ssh_manage import exec_cmd

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(344, 188)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 20, 101, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 60, 101, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 100, 101, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 30, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 80, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(50, 140, 81, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton,   QtCore.SIGNAL(_fromUtf8("clicked()")), self.clicked_button1)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clicked_button2)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clicked_button3)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "解锁admin锁定", None))
        self.pushButton_2.setText(_translate("Dialog", "强制修改密码", None))
        self.pushButton_3.setText(_translate("Dialog", "补丁不还原", None))
        self.label.setText(_translate("Dialog", "IP：", None))
        self.label_2.setText(_translate("Dialog", "PWD：", None))
        self.comboBox.setItemText(0, _translate("Dialog", "version_a", None))
        self.comboBox.setItemText(1, _translate("Dialog", "version_b", None))
        self.label_3.setText(_translate("Dialog", "VER：", None))

    def clicked_button1(self):
        """
        解锁admin密码
        :return:
        """
        exec_ip = self.lineEdit.text()
        #a = self.comboBox.currentText()
        # TODO:ADD cmd here
        cmd = ""
        pass_word = self.lineEdit_2.text()
        result_msg = exec_cmd(exec_ip, "root", pass_word, cmd)
        msg_box = QtGui.QMessageBox(QtGui.QMessageBox.Warning, "Alert", "解锁admin密码:%s" % result_msg)
        msg_box.exec_()

    def clicked_button2(self):
        """
        修改admin密码
        :return:
        """
        exec_ip = self.lineEdit.text()
        #a = self.comboBox.currentText()
        # TODO:ADD cmd here
        cmd = ""
        pass_word = self.lineEdit_2.text()
        result_msg = exec_cmd(exec_ip, "root", pass_word, cmd)
        msg_box = QtGui.QMessageBox(QtGui.QMessageBox.Warning, "Alert", "修改admin密码:%s" % result_msg)
        msg_box.exec_()

    def clicked_button3(self):
        """
        防止回退补丁
        :return:
        """
        exec_ip = self.lineEdit.text()
        #a = self.comboBox.currentText()
        # TODO:ADD cmd here
        cmd = ""
        pass_word = self.lineEdit_2.text()
        result_msg = exec_cmd(exec_ip, "root", pass_word, cmd)
        msg_box = QtGui.QMessageBox(QtGui.QMessageBox.Warning, "Alert", "防止回退补丁:%s" % result_msg)
        msg_box.exec_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = QtGui.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())
