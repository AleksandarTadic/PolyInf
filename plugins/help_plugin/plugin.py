from PySide6 import QtGui
from plugin_framework.extension import Extension
from .widgets.info_widget import InfoWidget


class Plugin(Extension):
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije
        """
        super().__init__(specification, iface)
        # TODO: ukoliko u nekom plugin-u treba sacuvati referencu na iface, napraviti atribut
        self.widget = InfoWidget(iface)
        self.open_action = QtGui.QAction("&About")
        self.open_action.triggered.connect(self.open)

    def activate(self):
        self.iface.menu_bar.add_menu_action("&Help", self.open_action)
        self.activated = True

    def deactivate(self):
        self.iface.menu_bar.remove_menu_action("&Help", self.open_action)
        self.activated = False

    def open(self):
        self.widget.show()