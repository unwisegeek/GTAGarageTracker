# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(832, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 791, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.tabVehicles = QtWidgets.QWidget()
        self.tabVehicles.setObjectName("tabVehicles")
        self.tableVehicle = QtWidgets.QTableView(self.tabVehicles)
        self.tableVehicle.setGeometry(QtCore.QRect(0, 0, 651, 511))
        self.tableVehicle.setObjectName("tableVehicle")
        self.labelSortBy = QtWidgets.QLabel(self.tabVehicles)
        self.labelSortBy.setGeometry(QtCore.QRect(660, 10, 58, 16))
        self.labelSortBy.setObjectName("labelSortBy")
        self.comboVehiclesSortBy = QtWidgets.QComboBox(self.tabVehicles)
        self.comboVehiclesSortBy.setGeometry(QtCore.QRect(660, 30, 121, 26))
        self.comboVehiclesSortBy.setObjectName("comboVehiclesSortBy")
        self.tabWidget.addTab(self.tabVehicles, "")
        self.tabGarages = QtWidgets.QWidget()
        self.tabGarages.setObjectName("tabGarages")
        self.tableGarage = QtWidgets.QTableView(self.tabGarages)
        self.tableGarage.setGeometry(QtCore.QRect(0, 0, 651, 511))
        self.tableGarage.setObjectName("tableGarage")
        self.labelGarageSortBy = QtWidgets.QLabel(self.tabGarages)
        self.labelGarageSortBy.setGeometry(QtCore.QRect(660, 10, 58, 16))
        self.labelGarageSortBy.setObjectName("labelGarageSortBy")
        self.comboGaragesSortBy = QtWidgets.QComboBox(self.tabGarages)
        self.comboGaragesSortBy.setGeometry(QtCore.QRect(660, 30, 121, 26))
        self.comboGaragesSortBy.setObjectName("comboGaragesSortBy")
        self.tabWidget.addTab(self.tabGarages, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 832, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GTA Garage Tracker"))
        self.labelSortBy.setText(_translate("MainWindow", "Sort By"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVehicles), _translate("MainWindow", "Vehicles"))
        self.labelGarageSortBy.setText(_translate("MainWindow", "Sort By"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGarages), _translate("MainWindow", "Garages"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
