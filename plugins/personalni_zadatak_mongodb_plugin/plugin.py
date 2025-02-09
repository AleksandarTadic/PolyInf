from PySide6 import QtGui
from plugin_framework.extension import Extension
from .widgets.personalni_zadatak_widget import PersonalniZadatakWidget


class Plugin(Extension):
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije
        """
        super().__init__(specification, iface)
        self.widget = PersonalniZadatakWidget(iface)
        self.open_action = QtGui.QAction("&Isporuceno Zadatak MongoDB")
        self.open_action.triggered.connect(self.open)

    def activate(self):
        self.iface.menu_bar.add_menu_action("&Personalni zadaci", self.open_action)
        self.activated = True

    def deactivate(self):
        self.iface.menu_bar.remove_menu_action("&Personalni zadaci", self.open_action)
        self.activated = False

    def open(self):
        self.widget.show()