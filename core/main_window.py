from PySide6 import QtWidgets, QtGui, QtCore
from core.ui.menu_bar import MenuBar
from core.ui.plugin_manager.plugin_manager import PluginManager
from core.ui.dock_widget.dock_view import DockView
from core.ui.dock_widget.dock_model import DockModel
from core.ui.status_bar.status_bar import StatusBar
from core.communication.communication_service import CommunicationService
from core.ui.central_workspace.tab_workspace import TabWorkspace

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, config, context, parent=None):
        super(MainWindow, self).__init__()
        self.config = config # Konfiguracija
        self.contexts = context # Context
        self.setWindowTitle(self.config.title)
        self.setWindowIcon(QtGui.QIcon(self.config.icon))
        self.resize(self.config.width, self.config.height)
        if self.config.maximized:
            self.showMaximized()
        # self.isFullScreen
        # self.showMaximized() 
        # self.isMaximized
        # registar plugin-ova
        self.plugin_registry = None

        # COMMUNICATION SERVICE
        self.communication_service = CommunicationService()

        # Central widget
        # self.central_widget = QtWidgets.QTabWidget(self)
        self.central_widget = TabWorkspace(self)
        self.communication_service.attach(self.central_widget)

        # Menu Bar
        self.menu_bar = MenuBar(self)
        # Status Bar
        self.status_bar = StatusBar(self)
        #Model delegat Observer
        self.database_dock_model = DockModel()
        self.database_dock = DockView(self, "Skladišta podataka", self.database_dock_model)
        self.database_dock_model.register(self.database_dock)
        self.database_dock_model.display()

        # COMMUNICATION SERVICE
        self.communication_service.attach(self.database_dock)

        # QMainWindow add
        self.setMenuBar(self.menu_bar)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.database_dock)
        self.setCentralWidget(self.central_widget)
        self.central_widget.restore_state()

        self.setStatusBar(self.status_bar)

    def add_plugin_registry(self, registry):
        self.plugin_registry = registry


    def open_plugin_manager(self):
        manager = PluginManager(self, self.plugin_registry)
        manager.show()
