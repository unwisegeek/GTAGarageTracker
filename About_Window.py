# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI Files/about.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About_Window(object):
    def setupUi(self, About_Window):
        About_Window.setObjectName("About_Window")
        About_Window.resize(432, 143)
        About_Window.setMinimumSize(QtCore.QSize(432, 143))
        About_Window.setMaximumSize(QtCore.QSize(432, 143))
        About_Window.setBaseSize(QtCore.QSize(432, 143))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("GarageTracker.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        About_Window.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(About_Window)
        self.gridLayout.setObjectName("gridLayout")
        self.labelIcon = QtWidgets.QLabel(About_Window)
        self.labelIcon.setMinimumSize(QtCore.QSize(111, 91))
        self.labelIcon.setMaximumSize(QtCore.QSize(111, 91))
        self.labelIcon.setBaseSize(QtCore.QSize(111, 91))
        self.labelIcon.setText("")
        self.labelIcon.setObjectName("labelIcon")
        self.gridLayout.addWidget(self.labelIcon, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(About_Window)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(About_Window)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.labelVersion = QtWidgets.QLabel(About_Window)
        self.labelVersion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelVersion.setObjectName("labelVersion")
        self.verticalLayout.addWidget(self.labelVersion)
        self.label_4 = QtWidgets.QLabel(About_Window)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.retranslateUi(About_Window)
        QtCore.QMetaObject.connectSlotsByName(About_Window)

    def retranslateUi(self, About_Window):
        _translate = QtCore.QCoreApplication.translate
        About_Window.setWindowTitle(_translate("About_Window", "About GTA Garage Tracker"))
        self.label.setText(_translate("About_Window", "GTA Garage Tracker"))
        self.label_2.setText(_translate("About_Window", "by John Madon"))
        self.labelVersion.setText(_translate("About_Window", "Version"))
        self.label_4.setText(_translate("About_Window", "Icon designed by Freepik from FlatIcon"))
