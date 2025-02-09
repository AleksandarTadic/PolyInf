from PySide6 import QtWidgets, QtGui, QtCore

from .table_workspace.table_workspace import TableWorkspace
from .web_workspace.web_workspace import WebWorkspace
from .text_workspace.text_workspace import TextWorkspace
from .tree_workspace.tree_workspace import TreeWorkspace
from .workspace_model import WorkspaceModel

class CentralWorkspaceWidget(QtWidgets.QWidget):
    def __init__(self, parent, data_info, credentials):
        super().__init__(parent)
        self.main_window = parent
        self.central_widget = self.main_window.central_widget # TAB WIDGET
        self.workspace_model = WorkspaceModel(data_info, credentials)
        
        self.layout = QtWidgets.QVBoxLayout()
        self.central_workspace = None

        self.central_workspace = self.get_central_widget()
        self.layout.addWidget(self.central_workspace)
        self.setLayout(self.layout)

    def get_model(self):
        return self.workspace_model

    def delete_widget(self):
        delete = self.layout.takeAt(0)
        delete.widget().deleteLater()
    
    def get_central_widget(self):
        display_type = self.get_model().get_data_info()["display"]
        database_type = self.get_model().get_data_info()["type"]

        if display_type == "Table" and (database_type == "MYSQL" or database_type == "MongoDB"):
            return TableWorkspace(self)
        elif display_type == "Text" and database_type == "MongoDB":
            return TextWorkspace(self)
        elif display_type == "Tree" and database_type == "MongoDB":
            return TreeWorkspace(self)
        elif display_type == "WEB" and database_type == "ArangoDB":
            return WebWorkspace(self)
        else:
            return TableWorkspace(self)

        
    def change_central_widget(self):
        self.delete_widget()
        self.central_workspace = None
        self.central_workspace = self.get_central_widget()
        self.layout.addWidget(self.central_workspace)
    
    def set_display_type(self, new_display):
        self.get_model().data_info["display"] = new_display

    def get_display_type(self):
        return self.get_model().get_data_info()["display"]

