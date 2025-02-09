from PySide6 import QtWidgets, QtGui, QtCore

from .table_widget.table_widget import TableWidget

class TableWorkspace(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.central_workspace = parent
        self.workspace = parent
        self.data_info = self.workspace.get_model().get_data_info()
        self.credentials = self.workspace.get_model().get_credentials()
        self.layout = QtWidgets.QVBoxLayout()

        self.tableWidget = TableWidget(self, self.data_info, self.credentials)

        self.layout.addWidget(self.tableWidget)
        if self.data_info["type"] == "MYSQL" and len(self.tableWidget.model.metadata.get_metadata(self.data_info["name"])["linked_keys"]) > 0:
            self.tableWidget.table.clicked.connect(self.show_tabs)

        self.setLayout(self.layout)

    def create_tab_widget(self):
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setTabsClosable(False)
        self.tab_widget.tabCloseRequested.connect(self.delete_tab)

    def show_tabs(self, index):
        if hasattr(self, "tab_widget"):
            self.close_all_tabs()
        else:
            self.create_tab_widget()
            self.layout.addWidget(self.tab_widget)

        selected_row_model = self.tableWidget.model.rows[index.row()]
        linked_tables = self.tableWidget.model.metadata.get_metadata(self.data_info["name"])["linked_keys"]

        for subtable in linked_tables:
            filtered = []
            for i in range(len(subtable["foreign_key"])):
                if subtable["foreign_key"][i] in selected_row_model:
                    filtered.append(selected_row_model[subtable["foreign_key"][i]])
            new_data_info = self.data_info.copy()
            new_data_info["title"] = subtable["title"]
            new_data_info["name"] = subtable["name"]

            subtableWidget = TableWidget(self, new_data_info, self.credentials, subtable["primary_key"], filtered, True)
            self.tab_widget.addTab(subtableWidget, QtGui.QIcon(new_data_info["icon"]), new_data_info["title"] + " - " + new_data_info["type"])

    def close_all_tabs(self):
        count = self.tab_widget.count()
        for i in range(count):
            self.tab_widget.removeTab(0)

    def delete_tab(self, index):
        self.tab_widget.removeTab(index)
        
    def get_current_widget(self):
        return self.tab_widget.currentIndex()
    
    def delete_widget(self, index):
        delete = self.layout.takeAt(index)
        delete.widget().deleteLater()
