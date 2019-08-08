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
        self.widget = QtWidgets.QWidget(DialogVehicleEdit)
        self.widget.setGeometry(QtCore.QRect(370, 10, 87, 62))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushOk = QtWidgets.QPushButton(self.widget)
        self.pushOk.setObjectName("pushOk")
        self.verticalLayout.addWidget(self.pushOk)
        self.pushCancel = QtWidgets.QPushButton(self.widget)
        self.pushCancel.setObjectName("pushCancel")
        self.verticalLayout.addWidget(self.pushCancel)
        self.widget1 = QtWidgets.QWidget(DialogVehicleEdit)
        self.widget1.setGeometry(QtCore.QRect(10, 10, 351, 63))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkWishlist = QtWidgets.QCheckBox(self.widget1)
        self.checkWishlist.setObjectName("checkWishlist")
        self.horizontalLayout.addWidget(self.checkWishlist)
        self.checkPegasus = QtWidgets.QCheckBox(self.widget1)
        self.checkPegasus.setObjectName("checkPegasus")
        self.horizontalLayout.addWidget(self.checkPegasus)
        self.checkOwned = QtWidgets.QCheckBox(self.widget1)
        self.checkOwned.setObjectName("checkOwned")
        self.horizontalLayout.addWidget(self.checkOwned)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.comboGarage = QtWidgets.QComboBox(self.widget1)
        self.comboGarage.setObjectName("comboGarage")
        self.verticalLayout_2.addWidget(self.comboGarage)

        self.retranslateUi(DialogVehicleEdit)
        QtCore.QMetaObject.connectSlotsByName(DialogVehicleEdit)

    def retranslateUi(self, DialogVehicleEdit):
        _translate = QtCore.QCoreApplication.translate
        DialogVehicleEdit.setWindowTitle(_translate("DialogVehicleEdit", "Vehicle Editor"))
        self.pushOk.setText(_translate("DialogVehicleEdit", "Ok"))
        self.pushCancel.setText(_translate("DialogVehicleEdit", "Cancel"))
        self.checkWishlist.setText(_translate("DialogVehicleEdit", "Wishlist"))
        self.checkPegasus.setText(_translate("DialogVehicleEdit", "Pegasus"))
        self.checkOwned.setText(_translate("DialogVehicleEdit", "Owned"))
