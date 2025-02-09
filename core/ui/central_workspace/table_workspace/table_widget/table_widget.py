from PySide6 import QtWidgets, QtGui, QtCore

from .table_model import TableModel
from .table_view import TableView

from ....toolbar.table_toolbar_director import TableToolbarDirector
from ....toolbar.subtable_toolbar_director import SubtableToolbarDirector
from ....toolbar.standard_table_toolbar_director import StandardTableToolbarDirector
from ....toolbar.command.invoker import Invoker
from ....toolbar.command.first_row_command import FirstRowCommand
from ....toolbar.command.last_row_command import LastRowCommand
from ....toolbar.command.change_display_type_command import ChangeDisplayTypeCommand
from ....toolbar.command.promote_subtable_command import PromoteSubtableCommand
from .....design_patterns.observer.observer import Observer

class TableWidget(QtWidgets.QWidget, Observer):
    def __init__(self, parent, data_info, credentials, columns=None, values=None, subtable=False):
        super().__init__(parent)
        self.workspace = parent
        self.central_workspace = parent.central_workspace
        self.data_info = data_info
        self.credentials = credentials
        self.columns = columns
        self.values = values
        self.subtable = subtable
        self.layout = QtWidgets.QVBoxLayout()

        self.table = TableView(self)
        self.model = TableModel(self, self.columns, self.values)
        self.table.setModel(self.model)

        INVOKER = Invoker()
        FIRST_ROW = FirstRowCommand(self.table)
        LAST_ROW = LastRowCommand(self.table)
        INVOKER.register("FIRST_ROW", FIRST_ROW)
        INVOKER.register("LAST_ROW", LAST_ROW)
        if not subtable and (self.data_info["type"] == "MYSQL"):
            self.toolbar = TableToolbarDirector().construct(self.central_workspace, INVOKER)
        elif subtable and self.data_info["type"] == "MYSQL":
            PROMOTE_SUBTABLE = PromoteSubtableCommand(self.table)
            INVOKER.register("PROMOTE_SUBTABLE", PROMOTE_SUBTABLE)
            self.toolbar = SubtableToolbarDirector().construct(self.central_workspace, INVOKER)
        elif self.data_info["type"] == "MongoDB":
            CHANGE_DISPLAY_TYPE = ChangeDisplayTypeCommand(self.central_workspace)
            INVOKER.register("CHANGE_DISPLAY_TYPE", CHANGE_DISPLAY_TYPE)
            self.toolbar = StandardTableToolbarDirector().construct(self.central_workspace, INVOKER)
            
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

    def update(self, event, **kwargs):
        if event == "UPDATE":
            kwargs["model"]