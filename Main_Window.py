# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI Files/Main_Window.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(781, 672)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("GarageTracker.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabVehicles = QtWidgets.QWidget()
        self.tabVehicles.setObjectName("tabVehicles")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tabVehicles)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableVehicle = QtWidgets.QTableView(self.tabVehicles)
        self.tableVehicle.setObjectName("tableVehicle")
        self.horizontalLayout.addWidget(self.tableVehicle)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelSortBy = QtWidgets.QLabel(self.tabVehicles)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSortBy.sizePolicy().hasHeightForWidth())
        self.labelSortBy.setSizePolicy(sizePolicy)
        self.labelSortBy.setMinimumSize(QtCore.QSize(150, 31))
        self.labelSortBy.setMaximumSize(QtCore.QSize(150, 31))
        self.labelSortBy.setObjectName("labelSortBy")
        self.verticalLayout_2.addWidget(self.labelSortBy)
        self.comboVehiclesSortBy = QtWidgets.QComboBox(self.tabVehicles)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboVehiclesSortBy.sizePolicy().hasHeightForWidth())
        self.comboVehiclesSortBy.setSizePolicy(sizePolicy)
        self.comboVehiclesSortBy.setMinimumSize(QtCore.QSize(150, 31))
        self.comboVehiclesSortBy.setMaximumSize(QtCore.QSize(150, 31))
        self.comboVehiclesSortBy.setBaseSize(QtCore.QSize(150, 31))
        self.comboVehiclesSortBy.setObjectName("comboVehiclesSortBy")
        self.verticalLayout_2.addWidget(self.comboVehiclesSortBy)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 368, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineVehicleSearch = QtWidgets.QLineEdit(self.tabVehicles)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(150)
        sizePolicy.setVerticalStretch(31)
        sizePolicy.setHeightForWidth(self.lineVehicleSearch.sizePolicy().hasHeightForWidth())
        self.lineVehicleSearch.setSizePolicy(sizePolicy)
        self.lineVehicleSearch.setMinimumSize(QtCore.QSize(150, 31))
        self.lineVehicleSearch.setMaximumSize(QtCore.QSize(150, 31))
        self.lineVehicleSearch.setBaseSize(QtCore.QSize(150, 31))
        self.lineVehicleSearch.setObjectName("lineVehicleSearch")
        self.verticalLayout.addWidget(self.lineVehicleSearch)
        self.pushVehicleSearch = QtWidgets.QPushButton(self.tabVehicles)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(150)
        sizePolicy.setVerticalStretch(31)
        sizePolicy.setHeightForWidth(self.pushVehicleSearch.sizePolicy().hasHeightForWidth())
        self.pushVehicleSearch.setSizePolicy(sizePolicy)
        self.pushVehicleSearch.setMinimumSize(QtCore.QSize(150, 31))
        self.pushVehicleSearch.setMaximumSize(QtCore.QSize(150, 31))
        self.pushVehicleSearch.setBaseSize(QtCore.QSize(150, 31))
        self.pushVehicleSearch.setObjectName("pushVehicleSearch")
        self.verticalLayout.addWidget(self.pushVehicleSearch)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tabVehicles, "")
        self.tabGarages = QtWidgets.QWidget()
        self.tabGarages.setObjectName("tabGarages")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tabGarages)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableGarage = QtWidgets.QTableView(self.tabGarages)
        self.tableGarage.setObjectName("tableGarage")
        self.horizontalLayout_3.addWidget(self.tableGarage)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.labelGarageSortBy = QtWidgets.QLabel(self.tabGarages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(150)
        sizePolicy.setVerticalStretch(31)
        sizePolicy.setHeightForWidth(self.labelGarageSortBy.sizePolicy().hasHeightForWidth())
        self.labelGarageSortBy.setSizePolicy(sizePolicy)
        self.labelGarageSortBy.setMinimumSize(QtCore.QSize(150, 31))
        self.labelGarageSortBy.setMaximumSize(QtCore.QSize(150, 31))
        self.labelGarageSortBy.setBaseSize(QtCore.QSize(150, 31))
        self.labelGarageSortBy.setObjectName("labelGarageSortBy")
        self.verticalLayout_6.addWidget(self.labelGarageSortBy)
        self.comboGaragesSortBy = QtWidgets.QComboBox(self.tabGarages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboGaragesSortBy.sizePolicy().hasHeightForWidth())
        self.comboGaragesSortBy.setSizePolicy(sizePolicy)
        self.comboGaragesSortBy.setMinimumSize(QtCore.QSize(150, 31))
        self.comboGaragesSortBy.setMaximumSize(QtCore.QSize(150, 31))
        self.comboGaragesSortBy.setBaseSize(QtCore.QSize(150, 31))
        self.comboGaragesSortBy.setObjectName("comboGaragesSortBy")
        self.verticalLayout_6.addWidget(self.comboGaragesSortBy)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        spacerItem1 = QtWidgets.QSpacerItem(20, 358, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lineGarageSearch = QtWidgets.QLineEdit(self.tabGarages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineGarageSearch.sizePolicy().hasHeightForWidth())
        self.lineGarageSearch.setSizePolicy(sizePolicy)
        self.lineGarageSearch.setMinimumSize(QtCore.QSize(150, 31))
        self.lineGarageSearch.setMaximumSize(QtCore.QSize(150, 31))
        self.lineGarageSearch.setBaseSize(QtCore.QSize(150, 31))
        self.lineGarageSearch.setObjectName("lineGarageSearch")
        self.verticalLayout_7.addWidget(self.lineGarageSearch)
        self.pushGarageSearch = QtWidgets.QPushButton(self.tabGarages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushGarageSearch.sizePolicy().hasHeightForWidth())
        self.pushGarageSearch.setSizePolicy(sizePolicy)
        self.pushGarageSearch.setMinimumSize(QtCore.QSize(150, 31))
        self.pushGarageSearch.setMaximumSize(QtCore.QSize(150, 31))
        self.pushGarageSearch.setBaseSize(QtCore.QSize(150, 31))
        self.pushGarageSearch.setObjectName("pushGarageSearch")
        self.verticalLayout_7.addWidget(self.pushGarageSearch)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tabGarages, "")
        self.tabDashboard = QtWidgets.QWidget()
        self.tabDashboard.setObjectName("tabDashboard")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tabDashboard)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tableDashboard = QtWidgets.QTableView(self.tabDashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableDashboard.sizePolicy().hasHeightForWidth())
        self.tableDashboard.setSizePolicy(sizePolicy)
        self.tableDashboard.setObjectName("tableDashboard")
        self.horizontalLayout_5.addWidget(self.tableDashboard)
        self.listDashboard = QtWidgets.QListWidget(self.tabDashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listDashboard.sizePolicy().hasHeightForWidth())
        self.listDashboard.setSizePolicy(sizePolicy)
        self.listDashboard.setMinimumSize(QtCore.QSize(150, 0))
        self.listDashboard.setMaximumSize(QtCore.QSize(150, 16777215))
        self.listDashboard.setObjectName("listDashboard")
        self.horizontalLayout_5.addWidget(self.listDashboard)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tabDashboard, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 781, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTimer = QtWidgets.QMenu(self.menubar)
        self.menuTimer.setObjectName("menuTimer")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionTimerOpen = QtWidgets.QAction(MainWindow)
        self.actionTimerOpen.setObjectName("actionTimerOpen")
        self.actionHelpContents = QtWidgets.QAction(MainWindow)
        self.actionHelpContents.setObjectName("actionHelpContents")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAdd_Vehicle = QtWidgets.QAction(MainWindow)
        self.actionAdd_Vehicle.setObjectName("actionAdd_Vehicle")
        self.actionVWC = QtWidgets.QAction(MainWindow)
        self.actionVWC.setObjectName("actionVWC")
        self.menuFile.addAction(self.actionAdd_Vehicle)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuTimer.addAction(self.actionTimerOpen)
        self.menuTimer.addAction(self.actionVWC)
        self.menuHelp.addAction(self.actionHelpContents)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTimer.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GTA Garage Tracker"))
        self.labelSortBy.setText(_translate("MainWindow", "Sort By"))
        self.pushVehicleSearch.setText(_translate("MainWindow", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVehicles), _translate("MainWindow", "Vehicles"))
        self.labelGarageSortBy.setText(_translate("MainWindow", "Sort By"))
        self.pushGarageSearch.setText(_translate("MainWindow", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGarages), _translate("MainWindow", "Garages"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDashboard), _translate("MainWindow", "Dashboard"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTimer.setTitle(_translate("MainWindow", "Utilities"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionTimerOpen.setText(_translate("MainWindow", "Mission Timer"))
        self.actionHelpContents.setText(_translate("MainWindow", "Contents"))
        self.actionAbout.setText(_translate("MainWindow", "About GTAGarageTracker"))
        self.actionAdd_Vehicle.setText(_translate("MainWindow", "Add Vehicle"))
        self.actionVWC.setText(_translate("MainWindow", "Vehicle Warehouse Checklist"))
