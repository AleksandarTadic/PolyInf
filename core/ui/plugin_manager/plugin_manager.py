from PySide6 import QtWidgets
from .plugin_manager_model import PluginManagerModel

class PluginManager(QtWidgets.QDialog):
    def __init__(self, parent=None, plugin_registry=None):
        super().__init__(parent)
        self.plugin_registry = plugin_registry
        self.activate_button = QtWidgets.QPushButton("Activate", self)
        self.deactivate_button = QtWidgets.QPushButton("Deactivate", self)
        self.button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Close, self)
        self.table_view = QtWidgets.QTableView(self)
        self.table_view.horizontalHeader().setStretchLastSection(True)
        self.widget_layout = QtWidgets.QGridLayout(self)
        self.plugin_model = None

        self.table_view.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self._create_model()

        self._bind_actions()
        self._populate_layout()
        self.setLayout(self.widget_layout)

        self.setWindowTitle("Upravljanje dodacima")
        self.resize(800, 500)

    def _refresh_data(self):
        self.plugin_model.refresh()

    def _bind_actions(self):
        self.activate_button.clicked.connect(self.activate_plugin)
        self.deactivate_button.clicked.connect(self.deactivate_plugin)
        self.button_box.rejected.connect(self.close)

    def _populate_layout(self):
        self.widget_layout.addWidget(self.activate_button, 0, 0)
        self.widget_layout.addWidget(self.deactivate_button, 0, 1)
        self.widget_layout.addWidget(self.table_view, 1, 0, 1, 2)
        self.widget_layout.addWidget(self.button_box, 3, 0, 1, 2)

    def _create_model(self):
        self.plugin_model = PluginManagerModel(None, self.plugin_registry._plugins)
        self.table_view.setModel(self.plugin_model)

    def list_plugins(self):
        for plugin in self.plugin_registry._plugins:
            print(plugin.name)

    def activate_plugin(self):
        selected_indexes = self.table_view.selectedIndexes()
        element = self.plugin_model.get_element(selected_indexes[0])
        for i in element.plugin_specification.dependencies:
            for plugin in self.plugin_registry._plugins:
                if plugin.plugin_specification.id == i.id and plugin.plugin_specification.version >= i.version:
                    self.plugin_registry.activate(i.id)
        self.plugin_registry.activate(element.plugin_specification.id)
        self._refresh_data()

    def deactivate_plugin(self):
        selected_indexes = self.table_view.selectedIndexes()
        element = self.plugin_model.get_element(selected_indexes[0])
        for i in element.plugin_specification.dependencies:
            self.plugin_registry.deactivate(i.id)
        self.plugin_registry.deactivate(element.plugin_specification.id)
        self._refresh_data()


