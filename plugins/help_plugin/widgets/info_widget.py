from PySide6 import QtWidgets


class InfoWidget(QtWidgets.QDialog):
    # FIXME: postaviti relativnu putanju
    config_path = "configuration.json"
    def __init__(self, parent=None):
        super().__init__(parent)
        self._layout = QtWidgets.QVBoxLayout()
 

        self._populate_layout()
        self.setLayout(self._layout)
        self.setWindowTitle("O rukovaocu heterogenim skladistima")
        self.resize(350, 200)


    def _populate_layout(self):
        self._name_layout = QtWidgets.QHBoxLayout()
        self._name_layout.addWidget(QtWidgets.QLabel("Name:"))
        self._name_layout.addWidget(QtWidgets.QLabel("Rukovalac heterogenim skladistima dokumentima"))
        self._layout.addLayout(self._name_layout)
        self._author_layout = QtWidgets.QHBoxLayout()
        self._author_layout.addWidget(QtWidgets.QLabel("Authors:"))
        self._author_layout.addWidget(QtWidgets.QLabel("Aleksandra Tadic"))
        self._layout.addLayout(self._author_layout)
        self._version_layout = QtWidgets.QHBoxLayout()
        self._version_layout.addWidget(QtWidgets.QLabel("Version:"))
        self._version_layout.addWidget(QtWidgets.QLabel("1.0.0B"))
        self._layout.addLayout(self._version_layout)
