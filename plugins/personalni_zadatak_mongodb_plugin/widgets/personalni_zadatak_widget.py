from PySide6 import QtWidgets

import sys
sys.path.append(".")

import datetime

from databases.databaseFactory import DatabaseFactory
from databases.metadata_handler.metadata_factory import MetadataFactory


class PersonalniZadatakWidget(QtWidgets.QDialog):
    # FIXME: postaviti relativnu putanju
    config_path = "configuration.json"
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMaximumWidth(600)
        self.setMaximumHeight(600)
        self._layout = QtWidgets.QVBoxLayout()
        


        # self._widget = QtWidgets.QWidget()
        self._drzava_layout = QtWidgets.QHBoxLayout()
        self._drzava_label = QtWidgets.QLabel("Drzava isporucioca:")
        self._drzava = QtWidgets.QLineEdit()
        self._drzava.setFixedHeight(50)
        self._drzava.setFixedWidth(500)
        self._drzava.setMaxLength(4)
        self._drzava_layout.addWidget(self._drzava_label)
        self._drzava_layout.addWidget(self._drzava)

        self._ps_layout = QtWidgets.QHBoxLayout()
        self._ps_label = QtWidgets.QLabel("Poslovni subjekat ID:")
        self._ps = QtWidgets.QSpinBox()
        self._ps.setFixedHeight(50)
        self._ps.setFixedWidth(500)
        self._ps.setMinimum(0)
        self._ps.setMaximum(999999999)
        self._ps_layout.addWidget(self._ps_label)
        self._ps_layout.addWidget(self._ps)

        self._tip_layout = QtWidgets.QHBoxLayout()
        self._tip_label = QtWidgets.QLabel("Tip:")
        self._tip = QtWidgets.QLineEdit()
        self._tip.setFixedHeight(50)
        self._tip.setFixedWidth(500)
        self._tip.setMaxLength(1)
        self._tip_layout.addWidget(self._tip_label)
        self._tip_layout.addWidget(self._tip)

        # self._status = QtWidgets.QPlainTextEdit("RADI")
        # self._status.setEnabled(False)
        # self._status.setFixedHeight(150)
        self._status = QtWidgets.QWidget()
        self._status.setFixedHeight(100)

        self._dodaj = QtWidgets.QPushButton("Dodaj")
        self._dodaj.setFixedHeight(75)
        self._dodaj.clicked.connect(lambda : self.dodaj_u_mongo())
        self._populate_layout()
        self.setLayout(self._layout)
        self.setWindowTitle("Personalni zadatak Isporuceno MongoDB")
        self.resize(600, 600)


    def _populate_layout(self):
        # self._layout.addWidget(QtWidgets.QLabel("Dodavanje podataka iz mysql-a u MongoDB."))
        self._layout.addLayout(self._drzava_layout)
        self._layout.addLayout(self._ps_layout)
        self._layout.addLayout(self._tip_layout)
        self._layout.addWidget(self._status)
        self._layout.addWidget(self._dodaj)
        # self._layout.addWidget(self._name_label)
        # self._layout.addWidget(QtWidgets.QLabel(""))
        # self._layout.addWidget(self._authors_label)
        # self._layout.addWidget(QtWidgets.QLabel("Aleksandar Tadic"))
        # self._layout.addWidget(self._version_label)
        # self._layout.addWidget(QtWidgets.QLabel("1.0.0"))

    def dodaj_u_mongo(self):
        mysql = DatabaseFactory().get_database("MYSQL", {
            "host":"localhost",
            "port": 3306,
            "user": "root",
            "password": "root",
            "database": "2023_nosql_baza_cinjenica"
        })
        mongodb = DatabaseFactory().get_database("MongoDB", {
            "host":"localhost",
            "port": 27017,
            "user": "root",
            "password": "root",
            "database": "rukovalac_heterogenim_skladistima"
        })
        mongo_metadata = MetadataFactory.get_metadata_handler("MongoDB")
        metadata = mongo_metadata.get_metadata("METADATA")[0]
        drzava_value = self._drzava.text()
        ps_value = str(self._ps.value())
        tip_value = self._tip.text()
        procedure = mysql.personalni_zadatak(drzava_value, ps_value, tip_value)

        if len(procedure) == 0:
            self.message("Trazeni parametri ne postoje, pokušajte ponovo sa drugačijim parametrima!")
            return


        # POVEZATI PROCEDURU SA META
        # IMPORTOVATI DATETIME I DODATI U DATUM 
        # print(template)

        # popunjavanje meta opisa
        # temp = procedure[0]
        # print(temp)
        temp_meta = metadata.copy()
        isp = metadata["Isporuceno"][0].copy()
        del temp_meta["_id"]
        temp_meta["Drzava kompanije"] = procedure[0]["NAZIV_DRZAVE_ISPORUCIOCA"]
        temp_meta["Kompanija"] = procedure[0]["NAZIV_KOMPANIJE_ISPORUCIOCA"]
        temp_meta["Tip"] = procedure[0]["TIP"]
        del temp_meta["Isporuceno"][0]
        for proc in procedure:
            isporuceno = isp.copy()
            isporuceno["Plasirani van trzista drzave"] = proc["PLASIRANO_DRZAVI"]
            isporuceno["Naziv"] = proc["SPR_NAZIV"]
            isporuceno["Kataloski broj"] = proc["SPR_KATBR"]
            isporuceno["Oznaka verzije"] = proc["VER_OZNAKA"]
            isporuceno["Plasman konfiguracije"]["Poslovna godina"] = str(proc["PLA_GODINA"])
            isporuceno["Plasman konfiguracije"]["Broj plasmana"] = proc["PLA_BROJ_PLASMANA"]
            isporuceno["Plasman konfiguracije"]["Investitor drzava"] = proc["DRZAVA_INVESTITOR"]
            isporuceno["Plasman konfiguracije"]["Datum ugovora"] = self.get_date(proc["PLA_DATUM_UG"])
            isporuceno["Redni broj"] = str(proc["PPL_RBR"])
            isporuceno["Planirano"] = self.get_date(proc["PPL_PLANIRANO"])
            isporuceno["Realizovano"] = self.get_date(proc["PPL_REALIZOVANO"])
            isporuceno["Adresa"] = proc["PS_ADRESA"]
            isporuceno["Web adresa"] = proc["PS_WWW"]
            temp_meta["Isporuceno"].append(isporuceno)
        temp_meta["Datum"] = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

        # Insert u MongoDB
        mongodb.insert("personalni_zadatak", temp_meta)

        self.message("Dodavanje završeno!")

    def get_date(self, date):
        try:
            datum = datetime.datetime.strptime(str(date), "%Y-%m-%d").date()
            
            datum = datum.strftime("%d.%m.%Y")
        except Exception:
            datum = None
        return datum

    def message(self, message):
        message_box = QtWidgets.QMessageBox()
        message_box.setText(message)
        message_box.exec()
        return