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
        DialogGarageEdit.resize(210, 84)
        DialogGarageEdit.setMinimumSize(QtCore.QSize(210, 84))
        DialogGarageEdit.setMaximumSize(QtCore.QSize(210, 84))
        self.layoutWidget = QtWidgets.QWidget(DialogGarageEdit)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 173, 64))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkOwned = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkOwned.setObjectName("checkOwned")
        self.horizontalLayout.addWidget(self.checkOwned)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushOk = QtWidgets.QPushButton(self.layoutWidget)
        self.pushOk.setObjectName("pushOk")
        self.verticalLayout.addWidget(self.pushOk)
        self.pushCancel = QtWidgets.QPushButton(self.layoutWidget)
        self.pushCancel.setObjectName("pushCancel")
        self.verticalLayout.addWidget(self.pushCancel)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(DialogGarageEdit)
        QtCore.QMetaObject.connectSlotsByName(DialogGarageEdit)

    def retranslateUi(self, DialogGarageEdit):
        _translate = QtCore.QCoreApplication.translate
        DialogGarageEdit.setWindowTitle(_translate("DialogGarageEdit", "Vehicle Editor"))
        self.checkOwned.setText(_translate("DialogGarageEdit", "Owned"))
        self.pushOk.setText(_translate("DialogGarageEdit", "Ok"))
        self.pushCancel.setText(_translate("DialogGarageEdit", "Cancel"))
