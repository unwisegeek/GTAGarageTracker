import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from Main_Window import Ui_MainWindow
import pandas as pd, sys

# Load Data into Pandas Dataframe
vehicle_data = pd.read_csv('vehicles.csv')

class MainWindow():
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # Configure Vehicle Table
        self.ui.tableVehicle.setRowCount(vehicle_data['Vehicle'].count())
        self.ui.tableVehicle.setColumnCount(4)
        self.ui.tableVehicle.setHorizontalHeaderLabels(["Name","Class","Owned","Garage"])

        local_vehicle_data = vehicle_data

        # Populate SortBy Combo Box
        self.ui.comboVehiclesSortBy.clear()
        local_vehicle_data_headers = list(local_vehicle_data.columns.values)
        for idx in range(0, len(local_vehicle_data_headers)):
            self.ui.comboVehiclesSortBy.addItem(local_vehicle_data_headers[idx])

        # Sort Table Based On comboVehiclesSortBy
        self.refresh()

        # Populate Table
        for idx in range(0, vehicle_data['Vehicle'].count()):
            self.ui.tableVehicle.setItem(idx, 0, PyQt5.QtWidgets.QTableWidgetItem(local_vehicle_data['Vehicle'][idx]))
            self.ui.tableVehicle.setItem(idx, 1, PyQt5.QtWidgets.QTableWidgetItem(local_vehicle_data['Class'][idx]))
            self.ui.tableVehicle.setItem(idx, 2, PyQt5.QtWidgets.QTableWidgetItem(str(local_vehicle_data['Owned'][idx])))
            self.ui.tableVehicle.setItem(idx, 3, PyQt5.QtWidgets.QTableWidgetItem(str(local_vehicle_data['Garage'][idx])))

        self.qTimer = QTimer()
        self.qTimer.setInterval(500)
        self.qTimer.timeout.connect(lambda: self.refresh())
        self.qTimer.start()

    def refresh(self):
        sort_criteria = self.ui.comboVehiclesSortBy.currentText()
        local_vehicle_data = local_vehicle_data.sort_values(sort_criteria)

    def showclick(self, item):
        cellContent = item.data()
        print("{} x {} was clicked!".format(item.column(), item.row()))

    def show(self):
        self.main_win.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())