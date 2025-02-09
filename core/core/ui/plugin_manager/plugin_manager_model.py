from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt


class PluginManagerModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None, plugins=[]):
        super().__init__(parent)
        self.plugins = plugins

    def get_element(self, index):
        if (index.isValid()):
            element = self.plugins[index.row()]
            if element:
                return element
        return self.plugins

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.plugins)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return 5

    def data(self, index, role=Qt.DisplayRole):
        element = self.get_element(index)
        if index.column() == 0 and role == Qt.DisplayRole:
            return element.plugin_specification.id
        elif index.column() == 1 and role == Qt.DisplayRole:
            return element.name # pristup property-ju
        elif index.column() == 2 and role == Qt.DisplayRole:
            return element.plugin_specification.description
        elif index.column() == 3 and role == Qt.DisplayRole:
            return element.plugin_specification.core_version
        elif index.column() == 4 and role == Qt.DecorationRole:
            if element.activated:
                return QtGui.QIcon("resources/icons/check.png")
            else:
                return QtGui.QIcon("resources/icons/cross.png")

    def setData(self, index, value, role):
        if role == Qt.EditRole and index.isValid():
            self.plugins[index.row()] = value
            self.dataChanged.emit(index, index, [QtCore.Qt.DisplayRole])
            return True
        return False
    
    def flags(self, index):
        return super().flags(index)# | Qt.ItemIsEditable


    def parent(self, child_index):
        return QtCore.QModelIndex()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if section == 0 and orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return "ID"
        elif section == 1 and orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return "Naziv"
        elif section == 2 and orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return "Opis"
        elif section == 3 and orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return "Verzija aplikacije"
        elif section == 4 and orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return "Status"

    def refresh(self):
        self.dataChanged.emit(self.index(0, 0), self.index(self.rowCount(), self.columnCount()))