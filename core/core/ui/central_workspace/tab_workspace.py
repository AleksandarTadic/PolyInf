from PySide6 import QtWidgets, QtGui, QtCore
from .central_workspace import CentralWorkspaceWidget
from core.design_patterns.observer.observer import Observer

class TabWorkspace(QtWidgets.QTabWidget, Observer):
    def __init__(self, parent=None):
        super(TabWorkspace, self).__init__()
        self.main_window = parent
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.delete_tab)
        

    def check_tabs(self, new_tab, type):
        for i in range(self.count()):
            if self.widget(i).property("tab_path") == new_tab+type:
                self.setCurrentIndex(i)
                return True

    def get_tab_contexts(self):
        tab_contexts = []
        for i in range(self.count()):
            temp_context = {
                "credentials": self.widget(i).workspace_model.credentials,
                "data_info": self.widget(i).workspace_model.data_info
            }
            tab_contexts.append(temp_context)
        tab_contexts = tab_contexts[::-1]
        workspace_context = {
            "current_index": self.currentIndex(),
            "tab_widgets": tab_contexts
        }
        return workspace_context

    def delete_tab(self, index):
        widget = self.widget(index)
        self.main_window.status_bar.show_status("Zatvorili", str(self.widget(index).property("tab_path")).split(".")[-1])
        if widget is not None:
            widget.deleteLater()
        self.removeTab(index)

    def add_tab_widget(self, data_info, credentials):
        if self.check_tabs(credentials["database"] + "." + data_info["title"],  " - " + data_info["type"]):
            return

        central_workspace = CentralWorkspaceWidget(self.main_window, data_info, credentials)
        central_workspace.setProperty("tab_path",credentials["database"] + "." +  data_info["title"] + " - " + data_info["type"]) # podesavanje property prilikom provere
        self.insertTab(0, central_workspace, QtGui.QIcon(data_info["icon"]), data_info["title"] + " - " + data_info["type"])
        self.setCurrentIndex(0)

        self.main_window.status_bar.show_status("Otvorili", data_info["title"] + " - " + data_info["type"])

    def restore_state(self):
        if "TAB_WIDGETS" in self.main_window.contexts.workspace_contexts:
            tabs = self.main_window.contexts.workspace_contexts["TAB_WIDGETS"]
            tab_widget = tabs["tab_widgets"]
            if tab_widget != None:
                for tab in tab_widget:
                    self.add_tab_widget(tab["data_info"], tab["credentials"])
                self.setCurrentIndex(self.main_window.contexts.workspace_contexts["TAB_WIDGETS"]["current_index"])

    def update(self, event, **kwargs):
        if event == "ADD_TAB":
            self.add_tab_widget(kwargs["data_info"], kwargs["credentials"])
        elif event == "ADD_TABS":
            for tab in kwargs["tabs"]:
                self.add_tab_widget(tab["data_info"], tab["credentials"])
