from PySide6 import QtWidgets, QtGui, QtCore

from .tree_model import TreeModel
from .tree_view import TreeView

from ....toolbar.table_toolbar_director import TableToolbarDirector
from ....toolbar.subtable_toolbar_director import SubtableToolbarDirector
from ....toolbar.standard_table_toolbar_director import StandardTableToolbarDirector
from ....toolbar.command.invoker import Invoker
from ....toolbar.command.first_row_command import FirstRowCommand
from ....toolbar.command.last_row_command import LastRowCommand
from ....toolbar.command.change_display_type_command import ChangeDisplayTypeCommand
from ....toolbar.command.promote_subtable_command import PromoteSubtableCommand
from .....design_patterns.observer.observer import Observer

class TreeWidget(QtWidgets.QWidget, Observer):
    def __init__(self, parent, model, columns=None, values=None):
        super().__init__(parent)
        self.workspace = parent
        self.central_workspace = parent.central_workspace
        self.model = model
        self.layout = QtWidgets.QVBoxLayout()

        self.tree = TreeView(self)
        self.tree.setHeaderLabels(["Key", "Value", "Type"])
        database = self.model.data
        for data in database:
            document_item = QtWidgets.QTreeWidgetItem(self.tree, ["{" + str(data["_id"]) + "}", "{ " + str(len(data)) + " fields }", type(data).__name__])
            self.generate(document_item, data)

        INVOKER = Invoker()
        FIRST_ROW = FirstRowCommand(self.tree)
        LAST_ROW = LastRowCommand(self.tree)
        CHANGE_DISPLAY_TYPE = ChangeDisplayTypeCommand(self.central_workspace)
        INVOKER.register("FIRST_ROW", FIRST_ROW)
        INVOKER.register("LAST_ROW", LAST_ROW)
        INVOKER.register("CHANGE_DISPLAY_TYPE", CHANGE_DISPLAY_TYPE)
        self.toolbar = StandardTableToolbarDirector().construct(self.central_workspace, INVOKER)
            
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.tree)
        self.setLayout(self.layout)

    def update(self, event, **kwargs):
        if event == "UPDATE":
            kwargs["model"]

    def generate(self, parent, data, first_iteration=True):
        for i in data:
            temp_type = type(data[i]).__name__
            if type(data[i]) == dict:
                if first_iteration:
                    new_item = QtWidgets.QTreeWidgetItem(parent, ["{" + str(data["_id"]) + "}", "{ " + str(len(data)) + " fields }", temp_type])
                else:
                    new_item = QtWidgets.QTreeWidgetItem(parent, [str(i), "{ " + str(len(data[i])) + " fields }", temp_type])
                if type(data[i]) == dict or type(data[i]) == list:
                    self.generate(new_item, data[i], False)
            elif type(data[i]) == list:
                new_item = QtWidgets.QTreeWidgetItem(parent, [i, "[ " + str(len(data[i])) + " elements ]", temp_type])
                list_data = data[i]
                for t in range(len(list_data)):
                    new_list_item = QtWidgets.QTreeWidgetItem(new_item, [str(t), "{ " + str(len(list_data[t])) + " fields }", type(list_data[t]).__name__])
                    self.generate(new_list_item, list_data[t], False)
            else:
                temp_type = type(data[i]).__name__
                new_item = QtWidgets.QTreeWidgetItem(parent, [i, str(data[i]), temp_type])