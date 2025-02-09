from PySide6 import QtWidgets, QtGui
from core.ui.plugin_manager.plugin_manager import PluginManager

class MenuBar(QtWidgets.QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_window = parent

        # File menu
        self.file_menu = QtWidgets.QMenu("&File")

        self._quit = QtGui.QAction(QtGui.QIcon("resources/icons/control-power.png"), "&Quit", self)
        self._quit.setShortcut("Ctrl+Q")
        self._quit.triggered.connect(self.main_window.close)
        self.file_menu.addAction(self._quit)

        # View menu
        self.view_menu = QtWidgets.QMenu("&View", self)

        self._full_screen = QtGui.QAction("FullScreen", checkable=True)
        self._full_screen.setShortcut(QtGui.QKeySequence(QtGui.QKeySequence.FullScreen))
        # self._full_screen.setChecked(True)
        self._full_screen.triggered.connect(lambda : self.fullscreen_check())
        self.view_menu.addAction(self._full_screen)

        # Plugins menu
        self.plugins_menu = QtWidgets.QMenu("&Plugins", self)

        self._plugin_manager = QtGui.QAction(QtGui.QIcon("resources/icons/control-power.png"),"&Plugin manager", self)
        self._plugin_manager.triggered.connect(self.open_plugin_manager)
        self.plugins_menu.addAction(self._plugin_manager)

        # Help menu
        self.help_menu = QtWidgets.QMenu("&Help", self)

        self.personalni_zadaci = QtWidgets.QMenu("&Personalni zadaci", self)

        # Add menus to main menu bar
        self.addMenu(self.file_menu)
        self.addMenu(self.view_menu)
        self.addMenu(self.plugins_menu)
        self.addMenu(self.help_menu)
        self.addMenu(self.personalni_zadaci)

    def fullscreen_check(self):
        if self._full_screen.isChecked():
            return self.main_window.showFullScreen()

        return self.main_window.showNormal()
    
    def open_plugin_manager(self):
        manager = PluginManager(self.main_window, self.main_window.plugin_registry)
        manager.show()

    def add_menu_action(self, menu_name, action):
        menues = self.findChildren(QtWidgets.QMenu)
        for menu in menues:
            if menu.title() == menu_name:
                menu.addAction(action)
                break
    
    def remove_menu_action(self, menu_name, action):
        menues = self.findChildren(QtWidgets.QMenu)
        for menu in menues:
            if menu.title() == menu_name:
                menu.removeAction(action)
                break

    def add_menu(self, menu):
        self.addMenu(menu)