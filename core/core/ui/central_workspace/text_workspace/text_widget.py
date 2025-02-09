from PySide6 import QtWidgets, QtGui, QtCore
from databases.databaseFactory import DatabaseFactory

from ....ui.toolbar.standard_text_toolbar_builder import StandardTextToolbarDirector
from ....ui.toolbar.command.invoker import Invoker
from ....design_patterns.observer.observer import Observer
from ...toolbar.command.change_display_type_command import ChangeDisplayTypeCommand
from .text_model import TextModel

class TextWidget(QtWidgets.QWidget, Observer):
    def __init__(self, parent, model):
        super().__init__()
        self.central_workspace = parent.central_workspace
        self.workspace = parent
        self.model = model
        self.layout = QtWidgets.QVBoxLayout()

        INVOKER = Invoker()
        CHANGE_DISPLAY_TYPE = ChangeDisplayTypeCommand(self.central_workspace)
        INVOKER.register("CHANGE_DISPLAY_TYPE", CHANGE_DISPLAY_TYPE)

        self.toolbar = StandardTextToolbarDirector().construct(self.central_workspace, INVOKER)
        self.layout.addWidget(self.toolbar)

        self.text_document = QtWidgets.QTextEdit()
        self.text_document.setReadOnly(True)

        self.layout.addWidget(self.text_document)
        self.setLayout(self.layout)

    def update(self, event, **kwargs):
        if event == "UPDATE":
            self.text_document.setHtml(kwargs["text"])