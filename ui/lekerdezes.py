#Sigmakik
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
import kezelo
from PyQt5.QtWidgets import QLabel, QPushButton,QLineEdit,QComboBox,QScrollArea,QVBoxLayout,QGroupBox
def lekerdezes(window):
    window.layoutvisszaallitasa()
    window.ranglistaGomb=QPushButton("Ranglista",window)
    window.ranglistaGomb.clicked.connect(window.ranglista)
    window.ranglistaGomb.setObjectName("bejelentkezesGomb")
    window.ranglistaGomb.setSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
    window.mylayout.addWidget(window.ranglistaGomb,0,0,1,1,Qt.AlignmentFlag.AlignCenter)
    
    window.jatekStatisztikaGomb=QPushButton("Játék statisztika",window)
    window.jatekStatisztikaGomb.clicked.connect(window.jatek_statisztika)
    window.jatekStatisztikaGomb.setObjectName("bejelentkezesGomb")
    window.jatekStatisztikaGomb.setSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
    window.mylayout.addWidget(window.jatekStatisztikaGomb,1,0,1,1,Qt.AlignmentFlag.AlignCenter)
    
    window.FogadasiStatisztikaGomb=QPushButton("Fogadási statisztika",window)
    window.FogadasiStatisztikaGomb.clicked.connect(window.fogadasi_statisztika)
    window.FogadasiStatisztikaGomb.setObjectName("bejelentkezesGomb")
    window.FogadasiStatisztikaGomb.setSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
    window.mylayout.addWidget(window.FogadasiStatisztikaGomb,2,0,1,1,Qt.AlignmentFlag.AlignCenter)
    
    window.Vissza=QPushButton("Vissza a főoldalra",window)
    window.Vissza.setObjectName("vissza")
    window.Vissza.clicked.connect(window.main)
    window.mylayout.addWidget(window.Vissza,3,0,1,1,Qt.AlignmentFlag.AlignBottom)
def ranglista(window):
    window.layoutvisszaallitasa()
    
    window.osszesJatekosTarolo=QScrollArea(window)
    window.osszesJatekosTarolo.setWidgetResizable(True)
    window.osszesJatekosTarolo.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
    window.osszesJatekosTarolo.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    window.osszesJatekos=QVBoxLayout(window.osszesJatekosTarolo)
    window.osszesJatekosBox = QGroupBox()
    window.osszesJatekosBox.setLayout(window.osszesJatekos)
    window.osszesJatekosTarolo.setWidget(window.osszesJatekosBox)
    window.osszesJatekosTarolo.setObjectName("noBorder")
    
    window.mylayout.addWidget(window.osszesJatekosTarolo,1,0,1,1)
    window.jatekosok_label = QLabel("Összes játékos:",window.osszesJatekosTarolo)
    window.jatekosok_label.setObjectName("noBorder")
    window.jatekosok_label.setMaximumHeight(100)
    window.osszesJatekos.addWidget(window.jatekosok_label)
    
    jatekosok=kezelo.ranglista_guihoz()
    for id,jatekos in enumerate(jatekosok["nev_sorrendben"]):
        window.jatekos_label = QLabel(f"{jatekosok['igazi_helyezes'][id]}. helyen: {jatekos}, {jatekosok['pontszam_sorrendben'][id]} ponttal",window.osszesJatekosTarolo)
        window.jatekos_label.setMaximumHeight(100)
        if id==0:
            window.jatekos_label.setObjectName("arany")
        else:
            window.jatekos_label.setObjectName("feher")
        window.osszesJatekos.addWidget(window.jatekos_label)
    window.Vissza=QPushButton("Vissza a lekérdezések oldalra",window)
    window.Vissza.clicked.connect(window.lekerdezes)
    window.Vissza.setObjectName("vissza")
    window.mylayout.addWidget(window.Vissza,2,0,1,1,Qt.AlignmentFlag.AlignBottom)
def jatek_statisztika(window):
    window.layoutvisszaallitasa()
    
    window.osszesJatekTarolo=QScrollArea(window)
    window.osszesJatekTarolo.setWidgetResizable(True)
    window.osszesJatekTarolo.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
    window.osszesJatekTarolo.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    window.osszesJatek=QVBoxLayout(window.osszesJatekTarolo)
    window.osszesJatekBox = QGroupBox()
    window.osszesJatekBox.setLayout(window.osszesJatek)
    window.osszesJatekTarolo.setWidget(window.osszesJatekBox)
    window.osszesJatekTarolo.setObjectName("noBorder")
    
    window.mylayout.addWidget(window.osszesJatekTarolo,1,0,1,1)
    window.jatekok_label = QLabel("Összes játék:",window.osszesJatekTarolo)
    window.jatekok_label.setMaximumHeight(100)
    window.jatekok_label.setObjectName("noBorder")
    window.osszesJatek.addWidget(window.jatekok_label)
    
    jatekok = kezelo.jatek_statisztika_guihoz()
    for jatek in jatekok:
        window.jatek_label = QLabel(f"{jatek['jatek_neve']}-ban/-ben\n{jatek['fogadasok_szama']}db fogadása van\n{jatek['nyeremenyek_osszpontszama']} összpontszáma van a nyereményeknek a játékhoz",window.osszesJatekTarolo)
        window.jatek_label.setMaximumHeight(200)
        window.jatek_label.setObjectName("jatekstatisztika_label")
        window.osszesJatek.addWidget(window.jatek_label)
    window.Vissza=QPushButton("Vissza a lekérdezések oldalra",window)
    window.Vissza.setObjectName("vissza")
    window.Vissza.clicked.connect(window.lekerdezes)
    window.mylayout.addWidget(window.Vissza,2,0,1,1,Qt.AlignmentFlag.AlignBottom)
def fogadasi_statisztika(window):
    window.layoutvisszaallitasa()
    
    window.kivalasztott_jatek=QComboBox(window)
    window.kivalasztott_jatek.addItems(kezelo.osszesJatek())
    window.kivalasztott_jatek.currentIndexChanged.connect(lambda:kezelo.fogadasiStatisztikaKivalasztottjatekInputahoz(window.kivalasztott_jatek,window.osszesAlanyEsemeny,window.osszesAlanyEsemenyTarolo))
    window.kivalasztott_jatek.setCurrentIndex(0)
    window.mylayout.addWidget(window.kivalasztott_jatek,0,0,1,1)
    
    window.osszesAlanyEsemenyTarolo=QScrollArea(window)
    window.osszesAlanyEsemenyTarolo.setWidgetResizable(True)
    window.osszesAlanyEsemenyTarolo.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
    window.osszesAlanyEsemenyTarolo.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    window.osszesAlanyEsemeny=QVBoxLayout(window.osszesAlanyEsemenyTarolo)
    window.osszesAlanyEsemenyBox = QGroupBox()
    window.osszesAlanyEsemenyBox.setLayout(window.osszesAlanyEsemeny)
    window.osszesAlanyEsemenyTarolo.setWidget(window.osszesAlanyEsemenyBox)
    window.osszesAlanyEsemenyTarolo.setObjectName("noBorder")
    
    window.mylayout.addWidget(window.osszesAlanyEsemenyTarolo,1,0,1,1)
    window.alanyEsemeny_label = QLabel("Összes alany és esemény:",window.osszesAlanyEsemenyTarolo)
    window.alanyEsemeny_label.setMaximumHeight(100)
    window.osszesAlanyEsemeny.addWidget(window.alanyEsemeny_label)
    
    kezelo.fogadasiStatisztikaKivalasztottjatekInputahoz(window.kivalasztott_jatek,window.osszesAlanyEsemeny,window.osszesAlanyEsemenyTarolo)
    window.Vissza=QPushButton("Vissza a lekérdezések oldalra",window)
    window.Vissza.setObjectName("vissza")
    window.Vissza.clicked.connect(window.lekerdezes)
    window.mylayout.addWidget(window.Vissza,2,0,1,1,Qt.AlignmentFlag.AlignBottom)