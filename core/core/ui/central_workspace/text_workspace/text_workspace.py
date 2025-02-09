from PySide6 import QtWidgets, QtGui, QtCore

from .text_model import TextModel
from .text_widget import TextWidget

class TextWorkspace(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.central_workspace = parent
        self.workspace = parent
        self.data_info = self.workspace.get_model().get_data_info()
        self.credentials = self.workspace.get_model().get_credentials()
        self.layout = QtWidgets.QVBoxLayout()

        self.text_model = TextModel(self)
        self.text_widget = TextWidget(self, self.text_model)
        self.text_model.register(self.text_widget)
        self.text_model.update()

        
        self.layout.addWidget(self.text_widget)
        self.setLayout(self.layout)
