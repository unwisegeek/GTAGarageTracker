# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vehicle_edit.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogVehicleEdit(object):
    def setupUi(self, DialogVehicleEdit):
        DialogVehicleEdit.setObjectName("DialogVehicleEdit")
        DialogVehicleEdit.resize(459, 84)
        DialogVehicleEdit.setMinimumSize(QtCore.QSize(459, 84))
        DialogVehicleEdit.setMaximumSize(QtCore.QSize(459, 84))
        self.comboGarage = QtWidgets.QComboBox(DialogVehicleEdit)
        self.comboGarage.setGeometry(QtCore.QRect(10, 40, 351, 31))
        self.comboGarage.setObjectName("comboGarage")
        self.checkOwned = QtWidgets.QCheckBox(DialogVehicleEdit)
        self.checkOwned.setGeometry(QtCore.QRect(280, 10, 78, 22))
        self.checkOwned.setObjectName("checkOwned")
        self.pushCancel = QtWidgets.QPushButton(DialogVehicleEdit)
        self.pushCancel.setGeometry(QtCore.QRect(360, 40, 95, 31))
        self.pushCancel.setObjectName("pushCancel")
        self.pushOk = QtWidgets.QPushButton(DialogVehicleEdit)
        self.pushOk.setGeometry(QtCore.QRect(360, 10, 95, 27))
        self.pushOk.setObjectName("pushOk")

        self.retranslateUi(DialogVehicleEdit)
        QtCore.QMetaObject.connectSlotsByName(DialogVehicleEdit)

    def retranslateUi(self, DialogVehicleEdit):
        _translate = QtCore.QCoreApplication.translate
        DialogVehicleEdit.setWindowTitle(_translate("DialogVehicleEdit", "Vehicle Editor"))
        self.checkOwned.setText(_translate("DialogVehicleEdit", "Owned"))
        self.pushCancel.setText(_translate("DialogVehicleEdit", "Cancel"))
        self.pushOk.setText(_translate("DialogVehicleEdit", "Ok"))
