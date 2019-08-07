import PyQt5
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from Main_Window import Ui_MainWindow
from Vehicle_Edit import Ui_DialogVehicleEdit
from Garage_Edit import Ui_DialogGarageEdit
import pandas as pd, sys

global_vehicle_data = pd.read_csv("vehicles.csv",sep=";",engine='python')
global_garage_data = pd.read_csv("garages.csv",sep=";",engine='python')

class DataFrameModel(QtGui.QStandardItemModel):
    def __init__(self, data, parent=None):
        QtGui.QStandardItemModel.__init__(self, parent)
        self._data = data
        for row in data.values.tolist():
            data_row = [ QtGui.QStandardItem("{}".format(x)) for x in row ]
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
        garages_data = pd.read_csv("garages.csv",sep=';',engine='python').sort_values('Name')

        self.setWindowTitle("Garage Editor - {}".format(target))

        # Find the target in the dataframe and populate the variables
        garage_info = { "index": "", "name": "", "type": "", "capacity": "", "owned": "" }
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
        garages_data = pd.read_csv("garages.csv",sep=';')
        garages_data['Owned'][int(garage_info['index'])] = self.checkOwned.isChecked()
        if self.lineGaragePlan.text() == "":
            self.lineGaragePlan.setText(" ")
        garages_data['Plan'][int(garage_info['index'])] = self.lineGaragePlan.text()
        garages_data.to_csv("garages.csv",sep=';',index=False)
        self.close()


    def show(self):
        self.garage_edit_win.show()

class VehicleEditor(QDialog, Ui_DialogVehicleEdit):
    def __init__(self, target, parent=None):
        super(VehicleEditor, self).__init__(parent)
        self.setupUi(self)

        # Load the Dataframes
        vehicle_data = pd.read_csv("vehicles.csv",sep=';',engine='python')
        garages_data = pd.read_csv("garages.csv",sep=';',engine='python').sort_values('Name')

        self.setWindowTitle("Vehicle Editor - {}".format(target))

        # Find the target in the dataframe and populate the variables
        vehicle_info = { "index": "", "name": "", "owned": "", "garage": ""}
        for idx in range(0, len(vehicle_data['Vehicle'])):
            if vehicle_data['Vehicle'][idx] == target:
                vehicle_info['index'] = idx
                vehicle_info['name'] = vehicle_data['Vehicle'][idx]
                vehicle_info['owned'] = str(vehicle_data['Owned'][idx])
                vehicle_info['garage'] = str(vehicle_data['Garage'][idx])

        # Process the variables into the QT Layout
        if vehicle_info['owned'] == "True":
            self.checkOwned.setChecked(True)
        if vehicle_info['garage'] != "None":
            for idx in range(0, len(garages_data['Name'])):
                if garages_data['Owned'][idx] == True and garages_data['Name'][idx] == vehicle_info['garage']:
                    self.comboGarage.addItem(vehicle_info['garage'])
        self.comboGarage.addItem("None")
        for idx in range(0, len(garages_data['Name'])):
            if garages_data['Owned'][idx] == True and garages_data['Name'][idx] != vehicle_info['garage']:
                self.comboGarage.addItem(garages_data['Name'][idx])

        # Connect Slots
        self.pushCancel.clicked.connect(self.close)
        self.pushOk.clicked.connect(lambda: self.write_config(vehicle_data, vehicle_info))

    def write_config(self, vehicle_data, vehicle_info):
        vehicle_data['Owned'][int(vehicle_info['index'])] = self.checkOwned.isChecked()
        vehicle_data['Garage'][int(vehicle_info['index'])] = self.comboGarage.currentText()
        vehicle_data.to_csv("vehicles.csv",sep=';',index=False)
        self.close()


    def show(self):
        self.vehicle_edit_win.show()

class MainWindow():
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # Load Vehicle Data
        local_vehicle_data = pd.read_csv("vehicles.csv",sep=";",engine='python')

        # Set Vehicle SortBy Options
        local_vehicle_data_headers = []
        for col in global_vehicle_data.columns:
            if col != "Index":
                local_vehicle_data_headers += [col]

        # Configure Vehicle Table
        vmodel = DataFrameModel(local_vehicle_data)
        self.ui.tableVehicle.setModel(vmodel)
        self.ui.tableVehicle.resizeColumnsToContents()
        self.ui.tableVehicle.setColumnHidden(0,True)

        # Load Garage Data
        local_garage_data = pd.read_csv("garages.csv", sep=";", engine='python')

        # Load Garage SortBy Options
        local_garage_data_headers = []
        for col in local_garage_data.columns:
            if col != "Index":
                local_garage_data_headers += [col]

        # Configure Garage Table
        gmodel = DataFrameModel(local_garage_data)
        self.ui.tableGarage.setModel(gmodel)
        self.ui.tableGarage.resizeColumnsToContents()
        self.ui.tableGarage.setColumnHidden(0, True)

        # Populate Vehicle SortBy Combo Box
        for idx in range(0, len(local_vehicle_data_headers)):
            self.ui.comboVehiclesSortBy.addItem(local_vehicle_data_headers[idx])

        # Populate Garages SortBy Combo Box
        for idx in range(0, len(local_garage_data_headers)):
            self.ui.comboGaragesSortBy.addItem(local_garage_data_headers[idx])

        # Set Vehicles as Active Tab
        self.ui.tabWidget.setCurrentWidget(self.ui.tabVehicles)

        # Load Garage Data into List
        for idx in range(0, len(local_garage_data['Name'])):
            if local_garage_data['Owned'][idx] == True:
                self.ui.listDashboard.addItem(local_garage_data['Name'][idx])
        self.ui.listDashboard.setCurrentRow(0)

        dtmodel = DataFrameModel(local_vehicle_data)
        target = self.ui.listDashboard.currentItem().text()
        vehicle_data = pd.read_csv("vehicles.csv", sep=";")
        filtered_vehicle_list = vehicle_data[vehicle_data['Garage'].str.contains(target) == True]
        dtmodel = DataFrameModel(filtered_vehicle_list)
        self.ui.tableDashboard.setModel(dtmodel)
        self.ui.tableDashboard.resizeColumnsToContents()
        self.ui.tableDashboard.setColumnHidden(0, True)
        self.ui.tableDashboard.setModel(dtmodel)
        self.ui.tableDashboard.resizeColumnsToContents()
        self.ui.tableDashboard.setColumnHidden(0, True)

        # Connections to Slots
        self.ui.comboVehiclesSortBy.activated.connect(self.vehicle_sort_criteria_changed)
        self.ui.comboGaragesSortBy.activated.connect(self.garage_sort_criteria_changed)
        self.ui.tableVehicle.doubleClicked.connect(lambda: self.table_vehicle_clicked())
        self.ui.tableGarage.doubleClicked.connect(lambda: self.table_garage_clicked())
        self.ui.pushVehicleSearch.clicked.connect(lambda: self.table_vehicle_search())
        self.ui.pushGarageSearch.clicked.connect(lambda: self.table_garage_search())
        self.ui.listDashboard.clicked.connect(lambda: self.dashboard_list_clicked())
        self.ui.listDashboard.selectionModel().currentChanged.connect(lambda: self.dashboard_list_clicked())
        self.ui.tableDashboard.doubleClicked.connect(lambda: self.table_dashboard_clicked())
        self.ui.actionQuit.triggered.connect(lambda: sys.exit())

    def dashboard_list_clicked(self):
        target = ""
        for ix in self.ui.listDashboard.selectedIndexes():
            col = ix.column()
            target = ix.data(Qt.DisplayRole)
        vehicle_data = pd.read_csv("vehicles.csv",sep=";")
        filtered_vehicle_list = vehicle_data[vehicle_data['Garage'].str.contains(target)==True]
        dtmodel = DataFrameModel(filtered_vehicle_list)
        self.ui.tableDashboard.setModel(dtmodel)
        self.ui.tableDashboard.resizeColumnsToContents()
        self.ui.tableDashboard.setColumnHidden(0, True)

    def table_dashboard_clicked(self):
        for ix in self.ui.tableDashboard.selectedIndexes():
            col = ix.column()
            target = ix.data(Qt.DisplayRole)
        if col == 1:
            self.child_win = VehicleEditor(target)
            self.child_win.exec_()
        vehicle_data = pd.read_csv("vehicles.csv", sep=";")
        filtered_vehicle_list = vehicle_data[vehicle_data['Garage'].str.contains(self.ui.listDashboard.currentItem().text()) == True]
        dtmodel = DataFrameModel(filtered_vehicle_list)
        self.ui.tableDashboard.setModel(dtmodel)
        self.ui.tableDashboard.resizeColumnsToContents()
        self.ui.tableDashboard.setColumnHidden(0, True)


    def table_vehicle_search(self):
        vehicle_data = pd.read_csv("vehicles.csv",sep=';')
        filtered_vehicle_data = vehicle_data[vehicle_data['Vehicle'].str.contains(self.ui.lineVehicleSearch.text())==True]
        vmodel = DataFrameModel(filtered_vehicle_data)
        self.ui.tableVehicle.setModel(vmodel)
        self.ui.tableVehicle.resizeColumnsToContents()
        self.ui.tableVehicle.setColumnHidden(0, True)
        self.ui.tableVehicle.setColumnHidden(3, True)
        self.ui.tableVehicle.setColumnHidden(4, True)


    def table_garage_search(self):
        garage_data = pd.read_csv("garages.csv",sep=';')
        filtered_garage_data = garage_data[garage_data['Name'].str.contains(self.ui.lineGarageSearch.text())==True]
        gmodel = DataFrameModel(filtered_garage_data)
        self.ui.tableGarage.setModel(gmodel)
        self.ui.tableGarage.resizeColumnsToContents()
        self.ui.tableGarage.setColumnHidden(0, True)

    def table_vehicle_clicked(self):
        for ix in self.ui.tableVehicle.selectedIndexes():
            col = ix.column()
            target = ix.data(Qt.DisplayRole)
        if col == 1:
            self.child_win = VehicleEditor(target)
            self.child_win.exec_()
            if self.ui.lineVehicleSearch.text() != "":
                self.table_vehicle_search()
            else:
                vmodel = DataFrameModel(pd.read_csv("vehicles.csv",sep=';'))
                self.ui.tableVehicle.setModel(vmodel)
                self.ui.tableVehicle.resizeColumnsToContents()
                self.ui.tableVehicle.setColumnHidden(0, True)

    def table_garage_clicked(self):
        for ix in self.ui.tableGarage.selectedIndexes():
            col = ix.column()
            target = ix.data(Qt.DisplayRole)
        if col == 1:
            self.child_win = GarageEditor(target)
            self.child_win.exec_()
            if self.ui.lineGarageSearch.text() != "":
                self.table_garage_search()
            else:
                gmodel = DataFrameModel(pd.read_csv("garages.csv",sep=';'))
                self.ui.tableGarage.setModel(gmodel)
                self.ui.tableGarage.resizeColumnsToContents()
                self.ui.tableGarage.setColumnHidden(0, True)

    def vehicle_sort_criteria_changed(self):
        sort_criteria = self.ui.comboVehiclesSortBy.currentText()
        vehicle_data = pd.read_csv("vehicles.csv",sep=";",engine='python')
        new_vehicle_data = vehicle_data.sort_values(sort_criteria)
        new_vehicle_data.to_csv("vehicles.csv", index=False, header=True,sep=";")

        vmodel = DataFrameModel(pd.read_csv("vehicles.csv",sep=";",engine='python'))
        self.ui.tableVehicle.setModel(vmodel)

    def garage_sort_criteria_changed(self):
        sort_criteria = self.ui.comboGaragesSortBy.currentText()
        garage_data = pd.read_csv("garages.csv",sep=";",engine='python')
        new_garage_data = garage_data.sort_values(sort_criteria)
        new_garage_data.to_csv("garages.csv", index=False, header=True,sep=";")

        gmodel = DataFrameModel(pd.read_csv("garages.csv",sep=";",engine='python'))
        self.ui.tableGarage.setModel(gmodel)

    def show(self):
        self.main_win.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())