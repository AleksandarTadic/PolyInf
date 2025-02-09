from PySide6 import QtWidgets, QtCore, QtGui

from databases.databaseFactory import DatabaseFactory
from databases.metadata_handler.metadata_factory import MetadataFactory
from .....design_patterns.observer.observable import Observable

class TableModel(QtCore.QAbstractTableModel, Observable):
    def __init__(self, parent, columns=None, values=None):
        super().__init__(parent)
        self.interface = parent
        self.observers = []
        self.data_info = self.interface.data_info
        self.credentials = self.interface.credentials
        self.columns = columns
        self.values = values
        self.database = DatabaseFactory().get_database(self.data_info["type"], self.credentials)
        self.metadata = MetadataFactory().get_metadata_handler(self.data_info["type"])

        self.rows = self.database.get_all(self.data_info["name"], self.columns, self.values)
        self.column_names = self.metadata.get_code_names(self.data_info["name"])
        self.headers = self.metadata.get_headers(self.data_info["name"])

    def get_element(self, index):
        if (index.isValid()):
            element = self.rows[index.row()]
            if element:
                return element
        return self.rows

    def rowCount(self, index):
        return len(self.rows)

    def columnCount(self, index):
        return len(self.headers)
    
    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        for i in range(len(self.headers)):
            if section == i and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
                return self.headers[i]
            
    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
                value = self.rows[index.row()][self.column_names[index.column()]]
                return str(value)

    def refresh(self):
        self.dataChanged.emit(self.index(0, 0), self.index(self.rowCount(), self.columnCount()))