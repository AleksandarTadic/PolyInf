from core.design_patterns.observer.observer import Observer
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import Slot

from core.ui.central_workspace.central_workspace import CentralWorkspaceWidget
class DockView(QtWidgets.QDockWidget, Observer):
    def __init__(self, parent, title, model) -> None:
        super().__init__(parent)
        self.main_window = parent
        self.model = model

        self.metadatas = []

        self.setWindowTitle(title)
        self.setMinimumWidth(280)

    def display(self, metadatas):

        self.metadatas = metadatas

        self.dock_tab = QtWidgets.QTabWidget()
        try:
            for meta in metadatas:
                dock_tree = QtWidgets.QTreeWidget()
                dock_tree.setHeaderLabels([meta["tip_naziv"]])
                top_item = QtWidgets.QTreeWidgetItem([meta["naziv"]])
                top_item.setIcon(0, QtGui.QIcon(meta["ikonica"]))
                self.generate_tree(dock_tree, top_item, meta, meta["podaci"])

                dock_tree.addTopLevelItem(top_item)
                self.dock_tab.addTab(dock_tree, QtGui.QIcon(meta["ikonica"]), meta["tip"])
                self.dock_tab.setCurrentIndex(0)
                dock_tree.expandAll()
        except Exception as e:
            print(e)
        
        self.setWidget(self.dock_tab)
        toggle_database_dock_action = self.toggleViewAction()
        self.main_window.menu_bar.view_menu.addAction(toggle_database_dock_action)

    def generate_tree(self, parent, top_item, meta, data, repeat=None):
        for paket in data["paketi"]:
            new_item = QtWidgets.QTreeWidgetItem([paket["naziv"]])
            new_item.setIcon(0, QtGui.QIcon(meta["ikonica"]))
            if "paketi" in paket:
                self.generate_tree(parent, new_item, meta, paket, True)
            if paket["tabele"] is not None:
                for tabela in paket["tabele"]:
                    child_item = QtWidgets.QTreeWidgetItem([tabela["label"]])
                    child_item.setData(0, QtCore.Qt.UserRole, tabela["kod"])
                    child_item.setData(1, QtCore.Qt.UserRole, tabela["label"])
                    child_item.setData(2, QtCore.Qt.UserRole, meta["tip"])
                    child_item.setData(3, QtCore.Qt.UserRole, meta["baza"])
                    child_item.setIcon(0, QtGui.QIcon(meta["ikonica"]))
                    new_item.addChild(child_item)
            top_item.addChild(new_item)
        if repeat != True:
            parent.itemClicked.connect(self.onItemClicked)               

    @Slot(QtWidgets.QTreeWidgetItem, int)
    def onItemClicked(self, it, col):
        current_type = it.treeWidget().parent().parent()
        cr_index = current_type.currentIndex()
        current_type = current_type.tabText(cr_index)

        self.main_window.communication_service.notify("ADD_TAD", )

        if(current_type != None and it.childCount() == 0):
            credentials = it.data(3, QtCore.Qt.UserRole)
            data_info = {
                "type": it.data(2, QtCore.Qt.UserRole),
                "name": it.data(0, QtCore.Qt.UserRole),
                "title": it.data(1, QtCore.Qt.UserRole),
                "display": self.get_database_display_type(current_type),
                "icon": self.get_database_icon(current_type)
            }
            if credentials != None:
                self.main_window.communication_service.notify("ADD_TAB", data_info=data_info, credentials=credentials)

    def get_database_icon(self, type):
        if type == "MYSQL":
            return "resources/icons/mysql.png"
        elif type == "MongoDB":
            return "resources/icons/mongo.png"
        elif type == "ArangoDB":
            return "resources/icons/arango.png"
        else:
            return None

    def get_database_display_type(self, type):
        if type == "MYSQL":
            return "Table"
        elif type == "MongoDB":
            return "Text"
        elif type == "ArangoDB":
            return "WEB"
    
    def update(self, event, **kwargs):
        if event == "DISPLAY":
            self.display(kwargs["message"])
