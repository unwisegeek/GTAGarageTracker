# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'garage_edit.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogGarageEdit(object):
    def setupUi(self, DialogGarageEdit):
        DialogGarageEdit.setObjectName("DialogGarageEdit")
        DialogGarageEdit.resize(459, 84)
        DialogGarageEdit.setMinimumSize(QtCore.QSize(459, 84))
        DialogGarageEdit.setMaximumSize(QtCore.QSize(459, 84))
        self.widget = QtWidgets.QWidget(DialogGarageEdit)
        self.widget.setGeometry(QtCore.QRect(10, 10, 441, 64))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.checkOwned = QtWidgets.QCheckBox(self.widget)
        self.checkOwned.setObjectName("checkOwned")
        self.horizontalLayout.addWidget(self.checkOwned)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.lineGaragePlan = QtWidgets.QLineEdit(self.widget)
        self.lineGaragePlan.setObjectName("lineGaragePlan")
        self.verticalLayout_2.addWidget(self.lineGaragePlan)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushOk = QtWidgets.QPushButton(self.widget)
        self.pushOk.setObjectName("pushOk")
        self.verticalLayout.addWidget(self.pushOk)
        self.pushCancel = QtWidgets.QPushButton(self.widget)
        self.pushCancel.setObjectName("pushCancel")
        self.verticalLayout.addWidget(self.pushCancel)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(DialogGarageEdit)
        QtCore.QMetaObject.connectSlotsByName(DialogGarageEdit)

    def retranslateUi(self, DialogGarageEdit):
        _translate = QtCore.QCoreApplication.translate
        DialogGarageEdit.setWindowTitle(_translate("DialogGarageEdit", "Vehicle Editor"))
        self.label.setText(_translate("DialogGarageEdit", "Plan"))
        self.checkOwned.setText(_translate("DialogGarageEdit", "Owned"))
        self.pushOk.setText(_translate("DialogGarageEdit", "Ok"))
        self.pushCancel.setText(_translate("DialogGarageEdit", "Cancel"))
