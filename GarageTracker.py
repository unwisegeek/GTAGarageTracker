import PyQt5
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Main_Window import Ui_MainWindow
import pandas as pd, sys

global_vehicle_data = pd.read_csv("vehicles.csv",sep=";",engine='python')
global_garage_data = pd.read_csv("garages.csv",sep=";",engine='python')

class DataFrameModel(QtCore.QAbstractTableModel):
    DtypeRole = QtCore.Qt.UserRole + 1000
    ValueRole = QtCore.Qt.UserRole + 1001

    def __init__(self, df=pd.DataFrame(), parent=None):
        super(DataFrameModel, self).__init__(parent)
        self._dataframe = df

    def setDataFrame(self, dataframe):
        self.beginResetModel()
        self._dataframe = dataframe.copy()
        self.endResetModel()

    def dataFrame(self):
        return self._dataframe

    dataFrame = QtCore.pyqtProperty(pd.DataFrame, fget=dataFrame, fset=setDataFrame)

    @QtCore.pyqtSlot(int, QtCore.Qt.Orientation, result=str)
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self._dataframe.columns[section]
            else:
                return str(self._dataframe.index[section])
        return QtCore.QVariant()

    def rowCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return len(self._dataframe.index)

    def columnCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return self._dataframe.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < self.rowCount()
            and 0 <= index.column() < self.columnCount()):
            return QtCore.QVariant()
        row = self._dataframe.index[index.row()]
        col = self._dataframe.columns[index.column()]
        dt = self._dataframe[col].dtype

        val = self._dataframe.iloc[row][col]
        if role == QtCore.Qt.DisplayRole:
            return str(val)
        elif role == DataFrameModel.ValueRole:
            return val
        if role == DataFrameModel.DtypeRole:
            return dt
        return QtCore.QVariant()

    def roleNames(self):
        roles = {
            QtCore.Qt.DisplayRole: b'display',
            DataFrameModel.DtypeRole: b'dtype',
            DataFrameModel.ValueRole: b'value'
        }
        return roles

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
            local_vehicle_data_headers += [col]

        # Configure Vehicle Table
        vmodel = DataFrameModel(local_vehicle_data)
        self.ui.tableVehicle.setModel(vmodel)
        self.ui.tableVehicle.resizeColumnsToContents()

        # Load Garage Data
        local_garage_data = pd.read_csv("garages.csv", sep=";", engine='python')

        # Load Garage SortBy Options
        local_garage_data_headers = []
        for col in local_garage_data.columns:
            local_garage_data_headers += [col]

        # Configure Garage Table
        gmodel = DataFrameModel(local_garage_data)
        self.ui.tableGarage.setModel(gmodel)
        self.ui.tableGarage.resizeColumnsToContents()

        # Populate Vehicle SortBy Combo Box
        for idx in range(0, len(local_vehicle_data_headers)):
            self.ui.comboVehiclesSortBy.addItem(local_vehicle_data_headers[idx])

        # Populate Garages SortBy Combo Box
        for idx in range(0, len(local_garage_data_headers)):
            self.ui.comboGaragesSortBy.addItem(local_garage_data_headers[idx])

        # Set Vehicles as Active Tab
        self.ui.tabWidget.setCurrentWidget(self.ui.tabVehicles)

        # Connections to Slots
        self.ui.comboVehiclesSortBy.activated.connect(self.vehicle_sort_criteria_changed)
        self.ui.comboGaragesSortBy.activated.connect(self.garage_sort_criteria_changed)

    def vehicle_sort_criteria_changed(self):
        sort_criteria = self.ui.comboVehiclesSortBy.currentText()
        vehicle_data = pd.read_csv("vehicles.csv",sep=";",engine='python')
        new_vehicle_data = vehicle_data.sort_values(sort_criteria)
        new_vehicle_data.to_csv("vehicles.csv", index=None, header=True,sep=";")

        vmodel = DataFrameModel(pd.read_csv("vehicles.csv",sep=";",engine='python'))
        self.ui.tableVehicle.setModel(vmodel)

    def garage_sort_criteria_changed(self):
        sort_criteria = self.ui.comboGaragesSortBy.currentText()
        garage_data = pd.read_csv("garages.csv",sep=";",engine='python')
        new_garage_data = garage_data.sort_values(sort_criteria)
        new_garage_data.to_csv("garages.csv", index=None, header=True,sep=";")

        gmodel = DataFrameModel(pd.read_csv("garages.csv",sep=";",engine='python'))
        self.ui.tableGarage.setModel(gmodel)

    def show(self):
        self.main_win.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())