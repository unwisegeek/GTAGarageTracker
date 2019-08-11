# from Ui_Windows import
import pandas as pd
import subprocess
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Main_Window import Ui_MainWindow
from Vehicle_Edit import Ui_DialogVehicleEdit
from Garage_Edit import Ui_DialogGarageEdit
from About_Window import Ui_About_Window

global_vehicle_data = pd.read_csv("vehicles.csv", sep=";", engine='python')
global_garage_data = pd.read_csv("garages.csv", sep=";", engine='python')


# noinspection PyMethodOverriding
class DataFrameModel(QtGui.QStandardItemModel):
    def __init__(self, data, parent=None):
        QtGui.QStandardItemModel.__init__(self, parent)
        self._data = data
        for row in data.values.tolist():
            data_row = [QtGui.QStandardItem("{}".format(x)) for x in row]
            self.appendRow(data_row)
        return

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def headerData(self, x, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[x]
        if orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
            return self._data.index[x]
        return None


class GarageEditor(QDialog, Ui_DialogGarageEdit):
    def __init__(self, target, parent=None):
        super(GarageEditor, self).__init__(parent)
        self.setupUi(self)

        # Load the Dataframes
        garages_data = pd.read_csv("garages.csv", sep=';', engine='python').sort_values('Name')

        self.setWindowTitle("Garage Editor - {}".format(target))

        # Find the target in the dataframe and populate the variables
        garage_info = {"index": "", "name": "", "type": "", "capacity": "", "owned": ""}
        for idx in range(0, len(garages_data['Name'])):
            if garages_data['Name'][idx] == target:
                garage_info['index'] = idx
                garage_info['name'] = garages_data['Name'][idx]
                garage_info['type'] = garages_data['Type'][idx]
                garage_info['capacity'] = garages_data['Capacity'][idx]
                garage_info['owned'] = str(garages_data['Owned'][idx])
                garage_info['plan'] = str(garages_data['Plan'][idx])

        # Process the variables into the QT Layout
        if garage_info['owned'] == "True":
            self.checkOwned.setChecked(True)
        if garage_info['plan'] != " ":
            self.lineGaragePlan.setText(garage_info['plan'])

        # Connect Slots
        self.pushCancel.clicked.connect(self.close)
        self.pushOk.clicked.connect(lambda: self.write_config(garage_info))

    def write_config(self, garage_info):
        garages_data = pd.read_csv("garages.csv", sep=';')
        garages_data['Owned'][int(garage_info['index'])] = self.checkOwned.isChecked()
        if self.lineGaragePlan.text() == "":
            self.lineGaragePlan.setText(" ")
        garages_data['Plan'][int(garage_info['index'])] = self.lineGaragePlan.text()
        garages_data.to_csv("garages.csv", sep=';', index=False)
        self.close()

    def show(self):
        self.garage_edit_win.show()


class AboutWindow(QDialog, Ui_About_Window):
    def __init__(self, parent=None):
        super(AboutWindow, self).__init__(parent)
        self.setupUi(self)

        icon = QPixmap("GarageTracker.svg")
        self.labelIcon.setPixmap(icon)
        self.labelVersion.setText("Version 0.5")

    def show(self):
        self.show()


class VehicleEditor(QDialog, Ui_DialogVehicleEdit):
    def __init__(self, target, parent=None):
        super(VehicleEditor, self).__init__(parent)
        self.setupUi(self)

        # Load the Dataframes
        vehicle_data = pd.read_csv("vehicles.csv", sep=';', engine='python')
        garages_data = pd.read_csv("garages.csv", sep=';', engine='python').sort_values('Name')

        self.setWindowTitle("Vehicle Editor - {}".format(target))

        # Find the target in the dataframe and populate the variables
        vehicle_info = {"index": "", "name": "", "owned": "", "garage": ""}
        for idx in range(0, len(vehicle_data['Vehicle'])):
            if vehicle_data['Vehicle'][idx] == target:
                vehicle_info['index'] = idx
                vehicle_info['name'] = vehicle_data['Vehicle'][idx]
                vehicle_info['owned'] = str(vehicle_data['Owned'][idx])
                vehicle_info['garage'] = str(vehicle_data['Garage'][idx])
                vehicle_info['pegasus'] = str(vehicle_data['Pegasus'][idx])
                vehicle_info['wishlist'] = str(vehicle_data['Wishlist'][idx])
                vehicle_info['insured'] = str(vehicle_data['Insured'][idx])
                vehicle_info['modified'] = str(vehicle_data['Modified'][idx])

        # Process the variables into the QT Layout
        if vehicle_info['owned'] == "True":
            self.checkOwned.setChecked(True)
        if vehicle_info['pegasus'] == "True":
            self.checkPegasus.setChecked(True)
        if vehicle_info['wishlist'] == "True":
            self.checkWishlist.setChecked(True)
        if vehicle_info['insured'] == "True":
            self.checkInsured.setChecked(True)
        if vehicle_info['modified'] == "True":
            self.checkModified.setChecked(True)
        if vehicle_info['garage'] != "None":
            for idx in range(0, len(garages_data['Name'])):
                if garages_data['Owned'][idx] is True and garages_data['Name'][idx] == vehicle_info['garage']:
                    self.comboGarage.addItem(vehicle_info['garage'])
        self.comboGarage.addItem("None")
        for idx in range(0, len(garages_data['Name'])):
            if garages_data['Owned'][idx] is True and garages_data['Name'][idx] != vehicle_info['garage']:
                self.comboGarage.addItem(garages_data['Name'][idx])

        # Connect Slots
        self.pushCancel.clicked.connect(self.close)
        self.pushOk.clicked.connect(lambda: self.write_config(vehicle_data, vehicle_info))

    def write_config(self, vehicle_data, vehicle_info):
        vehicle_data['Owned'][int(vehicle_info['index'])] = self.checkOwned.isChecked()
        vehicle_data['Garage'][int(vehicle_info['index'])] = self.comboGarage.currentText()
        vehicle_data['Wishlist'][int(vehicle_info['index'])] = self.checkWishlist.isChecked()
        vehicle_data['Pegasus'][int(vehicle_info['index'])] = self.checkPegasus.isChecked()
        vehicle_data['Insured'][int(vehicle_info['index'])] = self.checkInsured.isChecked()
        vehicle_data['Modified'][int(vehicle_info['index'])] = self.checkModified.isChecked()
        vehicle_data.to_csv("vehicles.csv", sep=';', index=False)
        self.close()

    def show(self):
        self.vehicle_edit_win.show()


# noinspection PyAttributeOutsideInit
class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # Load Vehicle Data
        local_vehicle_data = pd.read_csv("vehicles.csv", sep=";", engine='python')

        # Load Garage Data
        local_garage_data = pd.read_csv("garages.csv", sep=";", engine='python')

        # Set Vehicle SortBy Options
        local_vehicle_data_headers = []
        for col in global_vehicle_data.columns:
            if col != "Index":
                local_vehicle_data_headers += [col]

        # Set Garage SortBy Options
        local_garage_data_headers = []
        for col in local_garage_data.columns:
            if col != "Index":
                local_garage_data_headers += [col]

        # Configure Vehicle Table
        vmodel = DataFrameModel(local_vehicle_data)
        self.ui.tableVehicle.setModel(vmodel)
        self.ui.tableVehicle.setColumnHidden(0, True)
        self.ui.tableVehicle.setColumnHidden(8, True)
        self.set_vheaders()

        # Configure Garage Table
        gmodel = DataFrameModel(local_garage_data)
        self.ui.tableGarage.setModel(gmodel)
        self.ui.tableGarage.setColumnHidden(0, True)
        self.set_gheaders()

        # Populate Vehicle SortBy Combo Box
        for idx in range(0, len(local_vehicle_data_headers)):
            if local_vehicle_data_headers[idx] != "Pegasus":
                self.ui.comboVehiclesSortBy.addItem(local_vehicle_data_headers[idx])

        # Populate Garages SortBy Combo Box
        for idx in range(0, len(local_garage_data_headers)):
            self.ui.comboGaragesSortBy.addItem(local_garage_data_headers[idx])

        # Set Vehicles as Active Tab
        self.ui.tabWidget.setCurrentWidget(self.ui.tabVehicles)

        # Load Garage Data into List
        for idx in range(0, len(local_garage_data['Name'])):
            if local_garage_data['Owned'][idx]:
                self.ui.listDashboard.addItem(local_garage_data['Name'][idx])
        self.ui.listDashboard.addItem("Pegasus Vehicles")
        self.ui.listDashboard.addItem("Wishlist")
        self.ui.listDashboard.setCurrentRow(0)

        # Configure Dashboard Table
        target = self.ui.listDashboard.currentItem().text()
        vehicle_data = pd.read_csv("vehicles.csv", sep=";")
        filtered_vehicle_list = vehicle_data[vehicle_data['Garage'].str.contains(target)]
        dtmodel = DataFrameModel(filtered_vehicle_list)
        self.ui.tableDashboard.setModel(dtmodel)
        self.ui.tableDashboard.setColumnHidden(0, True)
        self.ui.tableDashboard.setColumnHidden(8, True)
        self.ui.tableDashboard.setModel(dtmodel)
        self.set_dtheaders()

        # Connections to Slots
        self.ui.actionTimerOpen.triggered.connect(lambda: subprocess.Popen(['python3', 'QtGTATimer.py']))
        self.ui.actionAbout.triggered.connect(lambda: self.about_menu_clicked())
        self.ui.actionQuit.triggered.connect(lambda: sys.exit())
        self.ui.comboVehiclesSortBy.activated.connect(self.vehicle_sort_criteria_changed)
        self.ui.comboGaragesSortBy.activated.connect(self.garage_sort_criteria_changed)
        self.ui.listDashboard.clicked.connect(lambda: self.dashboard_list_clicked())
        self.ui.listDashboard.selectionModel().currentChanged.connect(lambda: self.dashboard_list_clicked())
        self.ui.pushVehicleSearch.clicked.connect(lambda: self.table_vehicle_search())
        self.ui.pushGarageSearch.clicked.connect(lambda: self.table_garage_search())
        self.ui.tableVehicle.doubleClicked.connect(lambda: self.table_vehicle_clicked())
        self.ui.tableGarage.doubleClicked.connect(lambda: self.table_garage_clicked())
        self.ui.tableDashboard.doubleClicked.connect(lambda: self.table_dashboard_clicked())

    def dashboard_list_clicked(self):
        target = ""
        for ix in self.ui.listDashboard.selectedIndexes():
            target = ix.data(Qt.DisplayRole)
        vehicle_data = pd.read_csv("vehicles.csv", sep=";")
        filtered_vehicle_list = []
        list_info = {"Index": [], "Vehicle": [], "Class": [], "Owned": [], "Pegasus": [], "Wishlist": [],
                     "Garage": []}
        if target == "Pegasus Vehicles":
            for idx in range(0, len(vehicle_data['Vehicle'])):
                if vehicle_data['Pegasus'][idx] is True and vehicle_data['Owned'][idx] is True:
                    list_info["Index"].append(str(vehicle_data['Index'][idx]))
                    list_info["Vehicle"].append(str(vehicle_data['Vehicle'][idx]))
                    list_info["Class"].append(str(vehicle_data['Class'][idx]))
                    list_info["Owned"].append(str(vehicle_data['Owned'][idx]))
                    list_info["Pegasus"].append(str(vehicle_data['Pegasus'][idx]))
                    list_info["Wishlist"].append(str(vehicle_data['Wishlist'][idx]))
                    list_info["Garage"].append(str(vehicle_data['Garage'][idx]))
            filtered_vehicle_list = pd.DataFrame({"Index": list_info["Index"], "Vehicle": list_info["Vehicle"],
                                                  "Class": list_info["Class"], "Owned": list_info["Owned"],
                                                  "Pegasus": list_info["Pegasus"], "Wishlist": list_info["Wishlist"],
                                                  "Garage": list_info["Garage"]
                                                  })
        elif target == "Wishlist":
            for idx in range(0, len(vehicle_data['Vehicle'])):
                if vehicle_data['Wishlist'][idx]:
                    list_info["Index"].append(str(vehicle_data['Index'][idx]))
                    list_info["Vehicle"].append(str(vehicle_data['Vehicle'][idx]))
                    list_info["Class"].append(str(vehicle_data['Class'][idx]))
                    list_info["Owned"].append(str(vehicle_data['Owned'][idx]))
                    list_info["Pegasus"].append(str(vehicle_data['Pegasus'][idx]))
                    list_info["Wishlist"].append(str(vehicle_data['Wishlist'][idx]))
                    list_info["Garage"].append(str(vehicle_data['Garage'][idx]))
                filtered_vehicle_list = pd.DataFrame({"Index": list_info["Index"], "Vehicle": list_info["Vehicle"],
                                                      "Class": list_info["Class"], "Owned": list_info["Owned"],
                                                      "Pegasus": list_info["Pegasus"],
                                                      "Wishlist": list_info["Wishlist"],
                                                      "Garage": list_info["Garage"]
                                                      })
        else:
            filtered_vehicle_list = vehicle_data[vehicle_data['Garage'].str.contains(target)]
        dtmodel = DataFrameModel(filtered_vehicle_list)
        self.ui.tableDashboard.setModel(dtmodel)
        self.ui.tableDashboard.setColumnHidden(0, True)
        self.ui.tableDashboard.setColumnHidden(8, True)
        self.set_dtheaders()

    def table_dashboard_clicked(self):
        col = ""
        target = ""
        for ix in self.ui.tableDashboard.selectedIndexes():
            col = ix.column()
            target = ix.data(Qt.DisplayRole)
        if col == 1:
            self.child_win = VehicleEditor(target)
            self.child_win.exec_()
        self.dashboard_list_clicked()

    def table_vehicle_search(self):
        vehicle_data = pd.read_csv("vehicles.csv", sep=';')
        filtered_vehicle_data = vehicle_data[vehicle_data['Vehicle'].str.contains(self.ui.lineVehicleSearch.text())]
        vmodel = DataFrameModel(filtered_vehicle_data)
        self.ui.tableVehicle.setModel(vmodel)
        self.ui.tableVehicle.setColumnHidden(0, True)
        self.set_vheaders()

    def table_garage_search(self):
        garage_data = pd.read_csv("garages.csv", sep=';')
        filtered_garage_data = garage_data[garage_data['Name'].str.contains(self.ui.lineGarageSearch.text())]
        gmodel = DataFrameModel(filtered_garage_data)
        self.ui.tableGarage.setModel(gmodel)
        self.ui.tableGarage.setColumnHidden(0, True)
        self.set_gheaders()

    def table_vehicle_clicked(self):
        target = ""
        col = ""
        for ix in self.ui.tableVehicle.selectedIndexes():
            col = ix.column()
            target = ix.data(Qt.DisplayRole)
        if col == 1:
            self.child_win = VehicleEditor(target)
            self.child_win.exec_()
            if self.ui.lineVehicleSearch.text() != "":
                self.table_vehicle_search()
            else:
                vmodel = DataFrameModel(pd.read_csv("vehicles.csv", sep=';'))
                self.ui.tableVehicle.setModel(vmodel)
                self.ui.tableVehicle.setColumnHidden(0, True)
                self.set_vheaders()

    def about_menu_clicked(self):
        # noinspection PyAttributeOutsideInit
        self.child_win = AboutWindow()
        self.child_win.exec()

    def table_garage_clicked(self):
        target = ""
        col = ""
        for ix in self.ui.tableGarage.selectedIndexes():
            col = ix.column()
            target = ix.data(Qt.DisplayRole)
        if col == 1:
            self.child_win = GarageEditor(target)
            self.child_win.exec_()
            if self.ui.lineGarageSearch.text() != "":
                self.table_garage_search()
            else:
                gmodel = DataFrameModel(pd.read_csv("garages.csv", sep=';'))
                self.ui.tableGarage.setModel(gmodel)
                self.ui.tableGarage.setColumnHidden(0, True)
                self.set_gheaders()

    def vehicle_sort_criteria_changed(self):
        sort_criteria = self.ui.comboVehiclesSortBy.currentText()
        vehicle_data = pd.read_csv("vehicles.csv", sep=";", engine='python')
        new_vehicle_data = vehicle_data.sort_values(sort_criteria)
        new_vehicle_data.to_csv("vehicles.csv", index=False, header=True, sep=";")

        vmodel = DataFrameModel(pd.read_csv("vehicles.csv", sep=";", engine='python'))
        self.ui.tableVehicle.setModel(vmodel)

    def garage_sort_criteria_changed(self):
        sort_criteria = self.ui.comboGaragesSortBy.currentText()
        garage_data = pd.read_csv("garages.csv", sep=";", engine='python')
        new_garage_data = garage_data.sort_values(sort_criteria)
        new_garage_data.to_csv("garages.csv", index=False, header=True, sep=";")

        gmodel = DataFrameModel(pd.read_csv("garages.csv", sep=";", engine='python'))
        self.ui.tableGarage.setModel(gmodel)

    def set_vheaders(self):
        vheader = self.ui.tableVehicle.horizontalHeader()
        vheader.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        vheader.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        vheader.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        vheader.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        vheader.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        vheader.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        vheader.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)

    def set_gheaders(self):
        gheader = self.ui.tableGarage.horizontalHeader()
        gheader.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        gheader.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        gheader.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        gheader.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        gheader.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)

    def set_dtheaders(self):
        dtheader = self.ui.tableDashboard.horizontalHeader()
        dtheader.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        dtheader.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        dtheader.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        dtheader.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        dtheader.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        dtheader.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        dtheader.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)

    def show(self):
        self.main_win.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
