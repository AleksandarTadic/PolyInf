from PySide6 import QtWidgets, QtGui, QtCore

from .tree_widget.tree_widget import TreeWidget
from .tree_widget.tree_model import TreeModel

class TreeWorkspace(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.central_workspace = parent
        self.workspace = parent
        self.data_info = self.workspace.get_model().get_data_info()
        self.credentials = self.workspace.get_model().get_credentials()
        self.layout = QtWidgets.QVBoxLayout()

        self.tree_model = TreeModel(self)
        self.tree_widget = TreeWidget(self, self.tree_model)
        self.tree_model.register(self.tree_widget)

        self.layout.addWidget(self.tree_widget)
        self.setLayout(self.layout)



