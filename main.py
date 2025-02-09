import sys
import json
from PySide6 import QtWidgets, QtCore

from core.main_window import MainWindow
from core.config.configuration import Configuration
from core.config.app_context import AppContext
from plugin_framework.plugin_registry import PluginRegistry

class Main(QtWidgets.QApplication):
    def __init__(self):
        sys.argv += ['-platform', 'windows:darkmode=2']
        super().__init__(sys.argv)
        self.setStyle('Fusion')

        self.configuration = Configuration.load_configuration()
        self.context = AppContext.load_context(self.configuration.context_path)
        self.main_window = MainWindow(self.configuration, self.context)

        self.plugin_registry = PluginRegistry(self.configuration.plugins_path, self.main_window, self.context.activated_plugins)
        self.main_window.add_plugin_registry(self.plugin_registry)

        self.aboutToQuit.connect(lambda : self.on_exit())

        self.start()

    def start(self):
        self.main_window.show()

    def on_exit(self):
        self.configuration.save_configuration(self.main_window)
        self.context.save_context(self.main_window)
    
if __name__ == "__main__":
    main = Main()
    sys.exit(main.exec())


