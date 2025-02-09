from PySide6 import QtWidgets
from pyArango.collection import Field, Collection, Edges
from pyArango.graph import Graph, EdgeDefinition
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
        self.setMaximumHeight(300)
        self._layout = QtWidgets.QVBoxLayout()
        
        self._status = QtWidgets.QWidget()
        self._status.setFixedHeight(100)

        self._dodaj = QtWidgets.QPushButton("Dodaj")
        self._dodaj.setFixedHeight(75)
        self._dodaj.clicked.connect(lambda : self.dodaj_u_arango())
        self._populate_layout()
        self.setLayout(self._layout)
        self.setWindowTitle("Personalni zadatak Isporuceno ArangoDB")
        self.resize(600, 300)


    def _populate_layout(self):
        self._layout.addWidget(QtWidgets.QLabel("Dodavanje podataka iz mysql-a u ArangoDB. Prilikom dodavanja kreiraju se potrebne kolekcije, dokumenti, nodovi i veze...\n\t\t Database: personalni_zadatak_isporuceno"))
        self._layout.addWidget(self._status)
        self._layout.addWidget(self._dodaj)


    def dodaj_u_arango(self):
        mysql = DatabaseFactory().get_database("MYSQL", {
            "host":"localhost",
            "port": 3306,
            "user": "root",
            "password": "root",
            "database": "2023_nosql_baza_cinjenica"
        })
        arangodb = DatabaseFactory().get_database("ArangoDB", {
            "host":"localhost",
            "port": 8529,
            "user": "root",
            "password": "root",
            "database": "personalni_zadatak_isporuceno"
        })

        procedure = mysql.personalni_zadatak_arango()
        if len(procedure) == 0:
            self.message("Podaci ne postoje!")
            return
   
        connection = arangodb.get_connection()
        db = None
        try:
            db = connection.createDatabase(name="personalni_zadatak_isporuceno")
        except:
            db = connection["personalni_zadatak_isporuceno"]
        db.dropAllCollections() 
        db.reload()
        try:
            db.createCollection(name="Isporuceno")
        except:
            pass
        try:
            db.createCollection(name="Tip")
        except:
            pass
        try:
            db.createCollection(name="Plasirano_U_Drzavu")
        except:
            pass
        # EDGES
        try:
            db.createCollection(name="Isporuceno_Tip", className='Edges')
        except:
            pass
        try:
            db.createCollection(name="Isporuceno_Plasirano_U_Drzavu", className='Edges')
        except:
            pass
        # Collection
        isporuceno_collection = db["Isporuceno"]
        tip_collection = db["Tip"]
        pla_dr_collection = db["Plasirano_U_Drzavu"]
        #Edges
        isporuceno_tip_edge = db["Isporuceno_Tip"]
        isporuceno_pla_dr_edge = db["Isporuceno_Plasirano_U_Drzavu"]

        for data in procedure:
            # Isporuceno
            isporuceno_key = str(str(data["DR_OZNAKA"]) + str(data["PLASMAN_ID"]) + str(data["PLA_GODINA"]) + str(data["PLA_BROJ_PLASMANA"])
            + str(data["PPL_RBR"]) + str(data["SOF_DR_OZNAKA"]) + str(data["POS_PS_ID"]) + str(data["SPR_KATBR"]) + str(data["TIP"])
            + str(data["VER_OZNAKA"]) + str(data["KONF_ID"]) + str(data["POS_DR_OZNAKA"]) + str(data["PS_ID"]))
            isporuceno_document = None
            try:
                isporuceno_document = isporuceno_collection[isporuceno_key]
            except:
                isporuceno_document = isporuceno_collection.createDocument()
                isporuceno_document._key = isporuceno_key
            # Data
            isporuceno_document["Naziv_Drzave_Isporucioca"] = data["NAZIV_DRZAVE_ISPORUCIOCA"]
            isporuceno_document["Naziv_Kompanije_Isporucioca"] = data["NAZIV_KOMPANIJE_ISPORUCIOCA"]
            isporuceno_document["Naziv_Drzave_Isporucioca"] = data["NAZIV_DRZAVE_ISPORUCIOCA"]
            isporuceno_document["Naziv_Proizvoda"] = data["SPR_NAZIV"]
            isporuceno_document["Poslovni_Subjekat_Naziv"] = data["PS_NAZIV"]
            isporuceno_document["Poslovni_Subjekat_Adresa"] = data["PS_ADRESA"]
            isporuceno_document["Poslovni_Subjekat_Web_Sajt"] = data["PS_WWW"]
            isporuceno_document["Drzava_Investitor"] = data["DRZAVA_INVESTITOR"]
            isporuceno_document["Datum_Ugovora"] = self.get_date(data["PLA_DATUM_UG"])
            isporuceno_document["Planirano"] = self.get_date(data["PPL_PLANIRANO"])
            isporuceno_document["Realizovano"] = self.get_date(data["PPL_REALIZOVANO"])
            isporuceno_document.save()

            # Tip
            tip_document = None
            try:
                tip_document = tip_collection[data["TIP"]]
            except:
                tip_document = tip_collection.createDocument()
                tip_document._key = data["TIP"]
            # Data
            tip_document.save()

            # Plasirano u drzavu
            pla_dr_document = None
            try:
                pla_dr_document = pla_dr_collection[data["DR_OZNAKA"]]
            except:
                pla_dr_document = pla_dr_collection.createDocument()
                pla_dr_document._key = data["DR_OZNAKA"]
            # Data
            pla_dr_document["Drzava"] = data["PLASIRANO_DRZAVI"]
            pla_dr_document.save()

            #EDGES
            #TIP
            isporuceno_tip_edge_document = None
            isporuceno_tip_edge_attributes = {"_key": str(isporuceno_key+data["TIP"]),
                   "_from": "Isporuceno/" + isporuceno_key,
                   "_to": "Tip/" + data["TIP"]}
            try:
                isporuceno_tip_edge_document = isporuceno_tip_edge.createDocument(isporuceno_tip_edge_attributes)
                isporuceno_tip_edge_document.save()
            except:
                pass

            # Plasirano u drzavu
            isporuceno_pla_dr_edge_document = None
            isporuceno_pla_dr_edge_attributes = {"_key": str(isporuceno_key+data["DR_OZNAKA"]),
                   "_from": "Isporuceno/" + isporuceno_key,
                   "_to": "Plasirano_U_Drzavu/" + data["DR_OZNAKA"]}
            try:
                isporuceno_pla_dr_edge_document = isporuceno_pla_dr_edge.createDocument(isporuceno_pla_dr_edge_attributes)
                isporuceno_pla_dr_edge_document.save()
            except:
                pass

        class Tip(Collection):
            _fields = {
                "name": Field()
            }

        class Isporuceno(Collection):
            _fields = {
                "name": Field()
            }

        class Plasirano_U_Drzavu(Collection):
            _fields = {
                "name": Field()
            }

        class Isporuceno_Plasirano_U_Drzavu(Edges):
            _fields = {
                "type": Field()
            }

        class Isporuceno_Tip(Edges):
            _fields = {
                "type": Field()
            }

        class Personalni_Zadatak_Graf(Graph) :
            _edgeDefinitions = (EdgeDefinition ('Isporuceno_Plasirano_U_Drzavu',
                                                fromCollections = ["Isporuceno"],
                                                toCollections = ["Plasirano_U_Drzavu"]),
                                EdgeDefinition ('Isporuceno_Tip',
                                                fromCollections = ["Isporuceno"],
                                                toCollections = ["Tip"]))
            _orphanedCollections = []
    
        db.createGraph(name="Personalni_Zadatak_Graf", createCollections=False)
        
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