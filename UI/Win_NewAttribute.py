# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Win_NewAttribute.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Win_NewAttr(object):
    def setupUi(self, Win_NewAttr):
        Win_NewAttr.setObjectName("Win_NewAttr")
        Win_NewAttr.resize(363, 206)
        self.pushButto_OK = QtWidgets.QPushButton(Win_NewAttr)
        self.pushButto_OK.setGeometry(QtCore.QRect(60, 130, 71, 41))
        self.pushButto_OK.setObjectName("pushButto_OK")
        self.pushButto_Cancel = QtWidgets.QPushButton(Win_NewAttr)
        self.pushButto_Cancel.setGeometry(QtCore.QRect(220, 130, 71, 41))
        self.pushButto_Cancel.setObjectName("pushButto_Cancel")
        self.widget = QtWidgets.QWidget(Win_NewAttr)
        self.widget.setGeometry(QtCore.QRect(70, 40, 211, 61))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_name = QtWidgets.QLabel(self.widget)
        self.label_name.setObjectName("label_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_name)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_type = QtWidgets.QLabel(self.widget)
        self.label_type.setObjectName("label_type")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_type)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem)

        self.retranslateUi(Win_NewAttr)
        QtCore.QMetaObject.connectSlotsByName(Win_NewAttr)

    def retranslateUi(self, Win_NewAttr):
        _translate = QtCore.QCoreApplication.translate
        Win_NewAttr.setWindowTitle(_translate("Win_NewAttr", "NewAttribute"))
        self.pushButto_OK.setText(_translate("Win_NewAttr", "确定"))
        self.pushButto_Cancel.setText(_translate("Win_NewAttr", "取消"))
        self.label_name.setText(_translate("Win_NewAttr", "名称        "))
        self.label_type.setText(_translate("Win_NewAttr", "类型"))
        self.comboBox.setItemText(0, _translate("Win_NewAttr", "int"))
        self.comboBox.setItemText(1, _translate("Win_NewAttr", "float"))
        self.comboBox.setItemText(2, _translate("Win_NewAttr", "string"))
