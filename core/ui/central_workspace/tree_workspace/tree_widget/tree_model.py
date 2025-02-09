from PySide6 import QtWidgets, QtCore, QtGui

from databases.databaseFactory import DatabaseFactory
from databases.metadata_handler.metadata_factory import MetadataFactory
from .....design_patterns.observer.observable import Observable

class TreeModel(Observable):
    def __init__(self, parent, columns=None, values=None):
        super().__init__()
        self.interface = parent
        self.data_info = self.interface.data_info
        self.credentials = self.interface.credentials
        self.columns = columns
        self.values = values
        self.database = DatabaseFactory().get_database(self.data_info["type"], self.credentials)
        self.metadata = MetadataFactory().get_metadata_handler(self.data_info["type"])

        self.data = self.database.get_all(self.data_info["name"], self.columns, self.values)
        self.column_names = self.metadata.get_code_names(self.data_info["name"])
        self.headers = self.metadata.get_headers(self.data_info["name"])

