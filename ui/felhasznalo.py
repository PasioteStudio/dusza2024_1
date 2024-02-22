#Sigmakik
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
import kezelo
from PyQt5.QtWidgets import QLabel, QPushButton,QLineEdit,QComboBox,QScrollArea,QVBoxLayout,QGroupBox,QWidget
def profil_beallitasok(window,felhasznalonev:str):
    window.layoutvisszaallitasa()
    nev = window.mindig_latszik_belepve(felhasznalonev)
    
    window.megjelenitett_nev_label=QLabel("Megjelenített neved megváltoztatása:",window)
    window.megjelenitett_nev_label.setObjectName("noBorder")
    window.mylayout.addWidget(window.megjelenitett_nev_label,1,1,1,1)
    
    window.megjelenitett_nev_input=QLineEdit(nev,window)
    window.megjelenitett_nev_input.setPlaceholderText("megjelenitett nev")
    window.mylayout.addWidget(window.megjelenitett_nev_input,1,2,1,1)
    
    window.errorUzenet=QLabel(window)
    window.errorUzenet.setMaximumHeight(60)
    window.errorUzenet.setObjectName("noBorder")
    window.mylayout.addWidget(window.errorUzenet,2,1,1,2)
    
    def ErrorÜzenetek():
        valasz = kezelo.benyujtott_profilbeallitasok(felhasznalonev,window.megjelenitett_nev_input)
        if not valasz == True:
            window.errorUzenet.setText()
        else:
            window.bejelentkezett_oldal(felhasznalonev)
    window.mentes=QPushButton("Mentés",window)
    window.mentes.setObjectName("MentesGomb")
    window.mentes.clicked.connect(ErrorÜzenetek)
    window.mylayout.addWidget(window.mentes,3,2,5,1,Qt.AlignmentFlag.AlignBottom)
    
    window.Vissza=QPushButton("Vissza a szerepválasztáshoz",window)
    window.Vissza.setObjectName("vissza")
    window.Vissza.clicked.connect(lambda: window.bejelentkezett_oldal(felhasznalonev))
    window.mylayout.addWidget(window.Vissza,3,1,5,1,Qt.AlignmentFlag.AlignBottom)
def bejelentkezett_oldal(window,felhasznalonev:str):
    window.layoutvisszaallitasa()
    window.mindig_latszik_belepve(felhasznalonev)
    
    window.beallitasok=QPushButton("⚙️",window)
    window.beallitasok.setObjectName("beallitasok")
    window.beallitasok.clicked.connect(lambda: window.profil_beallitasok(felhasznalonev))
    
    window.szerepkor = QLabel(f"Szerepválasztás", window)
    window.szerepkor.setAlignment(Qt.AlignmentFlag.AlignCenter)
    window.szerepkor.setObjectName("szerepvalasztas")
    
    window.szervezo = QPushButton('Szervező', window)
    window.szervezo.clicked.connect(lambda: window.szervezo_oldal(felhasznalonev))
    window.szervezo.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
    window.szervezo.setObjectName("szervezo")
    
    window.fogado = QPushButton('Fogadó', window)
    window.fogado.clicked.connect(lambda: window.fogado_oldal(felhasznalonev))
    window.fogado.setObjectName("fogado")
    window.fogado.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
    
    window.Vissza = QPushButton('Vissza a főoldalra', window)
    window.Vissza.clicked.connect(window.main)
    window.Vissza.setObjectName("vissza")
    
    window.mylayout.addWidget(window.beallitasok,0,2,1,1,Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
    window.beallitasok.raise_()
    window.mylayout.addWidget(window.szerepkor,0,1,1,2)
    window.mylayout.addWidget(window.szervezo,1,1,7,1)
    window.mylayout.addWidget(window.fogado,1,2,7,1)
    window.mylayout.addWidget(window.Vissza,7,0,1,3,Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
def bejelentkezes_oldal(window):
    window.layoutvisszaallitasa()
    # Bemeneti mező létrehozása
    window.oldalCim=QLabel("Bejelentkezés")
    window.oldalCim.setObjectName("cim")
    
    window.input_felhasznalonev = QLineEdit(window)
    window.input_felhasznalonev.setPlaceholderText("Felhasználó neved")
    window.input_felhasznalonev.setObjectName("felhasznalonev")
    
    window.input_jelszo = QLineEdit(window)
    window.input_jelszo.setPlaceholderText("Jelszavad")
    window.input_jelszo.setObjectName("jelszo")
    window.input_jelszo.textEdited.connect(lambda: kezelo.jelszo_rejtese(window.input_jelszo,"Jelszavad"))
    window.input_jelszo.setProperty("canToggle",True)
    window.input_jelszo_megjelenitese = QPushButton('😃', window)
    window.input_jelszo_megjelenitese.setProperty("toggle","😄")
    window.input_jelszo_megjelenitese.setMaximumWidth(100)
    window.input_jelszo_megjelenitese.setObjectName("jelszo_megjelenitese")
    window.input_jelszo_megjelenitese.clicked.connect(lambda: kezelo.jelszo_megjelenitese(window.input_jelszo,window.input_jelszo_megjelenitese,"Jelszavad"))
    
    window.errorUzenet=QLabel(window)
    window.errorUzenet.setMaximumHeight(60)
    window.errorUzenet.setObjectName("error")
    window.bejelentkezesGomb = QPushButton('Bejelentkezés', window)
    
    def ErrorUzenet():
        szotar=kezelo.benyujtott_bejelentkezes(window.input_felhasznalonev,window.input_jelszo)
        if szotar["státusz"]==True:
            felhasznalonev,nev=szotar["válasz"]
            window.bejelentkezett_oldal(felhasznalonev)
        else:
            window.errorUzenet.setText(szotar["válasz"])
            
    window.bejelentkezesGomb.clicked.connect(ErrorUzenet)
    window.bejelentkezesGomb.setObjectName("bejelentkezesGomb")
    window.Vissza = QPushButton('Vissza a főoldalra', window)
    window.Vissza.clicked.connect(window.main)
    window.Vissza.setObjectName("vissza")
    
    window.ures=QWidget(window)
    window.ures.setObjectName("noBorder")
    window.resizeWidgets.append({
        "elem":window.ures,
        "mive":0
    })
    window.ures.setFixedWidth(int(window.frameGeometry().size().width()/2))
    
    window.mylayout.addWidget(window.oldalCim,0,0,1,2,Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
    window.mylayout.addWidget(window.input_felhasznalonev,1,0,1,1)
    window.mylayout.addWidget(window.ures,1,1,3,1)
    window.mylayout.addWidget(window.input_jelszo,2,0,1,1)
    window.mylayout.addWidget(window.input_jelszo_megjelenitese,2,0,1,1,Qt.AlignmentFlag.AlignRight)
    window.mylayout.addWidget(window.errorUzenet,3,0,1,1)
    window.mylayout.addWidget(window.bejelentkezesGomb,4,0,1,2,Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
    window.mylayout.addWidget(window.Vissza,5,0,1,2,Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
def regisztracios_oldal(window):
    window.layoutvisszaallitasa()
    window.oldalCim=QLabel("Regisztráció",window)
    window.oldalCim.setObjectName("cim")
    
    window.input_felhasznalonev = QLineEdit(window)
    window.input_felhasznalonev.setPlaceholderText("Felhasználó neved")
    window.input_felhasznalonev.setObjectName("felhasznalonev")
    
    window.input_jelszo = QLineEdit(window)
    window.input_jelszo.setObjectName("jelszo")
    window.input_jelszo.textEdited.connect(lambda: kezelo.jelszo_rejtese(window.input_jelszo,"Jelszavad"))
    window.input_jelszo.setPlaceholderText("Jelszavad")
    window.input_jelszo.setProperty("canToggle",True)
    window.input_jelszo_megjelenitese = QPushButton('😃', window)
    window.input_jelszo_megjelenitese.setProperty("toggle","😄")
    window.input_jelszo_megjelenitese.clicked.connect(lambda: kezelo.jelszo_megjelenitese(window.input_jelszo,window.input_jelszo_megjelenitese,"Jelszavad"))
    window.input_jelszo_megjelenitese.setObjectName("jelszo_megjelenitese")
    
    window.input_megerosito_jelszo = QLineEdit(window)
    window.input_megerosito_jelszo.textEdited.connect(lambda: kezelo.jelszo_rejtese(window.input_megerosito_jelszo,"Jelszavad újra"))
    window.input_megerosito_jelszo.setPlaceholderText("Jelszavad újra")
    window.input_megerosito_jelszo.setProperty("canToggle",True)
    window.input_megerosito_jelszo.setObjectName("megerosito_jelszo")
    
    window.errorUzenet=QLabel(window)
    window.errorUzenet.setMaximumHeight(60)
    window.errorUzenet.setObjectName("error")
    window.keszGomb=QPushButton("Kész",window)
    def ErrorÜzenetek():
        valasz = kezelo.benyujtott_regisztracio(window.input_felhasznalonev,window.input_jelszo,window.input_megerosito_jelszo)
        if not valasz ==True:
            window.errorUzenet.setText(valasz)
        else:
            window.bejelentkezes_oldal()
    
    
    window.regisztraciosGomb = QPushButton('Regisztráció', window)
    window.regisztraciosGomb.clicked.connect(ErrorÜzenetek)
    window.regisztraciosGomb.setObjectName("regisztracioGomb")
    window.Vissza = QPushButton('Vissza a főoldalra', window)
    window.Vissza.clicked.connect(window.main)
    window.Vissza.setObjectName("vissza")
    
    window.ures=QWidget(window)
    window.ures.setObjectName("noBorder")
    window.resizeWidgets.append({
        "elem":window.ures,
        "mive":0
    })
    window.ures.setFixedWidth(int(window.frameGeometry().size().width()/2))
    window.mylayout.addWidget(window.oldalCim,0,0,1,2,Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
    window.mylayout.addWidget(window.input_felhasznalonev,1,0,1,1)
    window.mylayout.addWidget(window.input_jelszo,2,0,1,1)
    window.mylayout.addWidget(window.input_jelszo_megjelenitese,2,0,1,1,Qt.AlignmentFlag.AlignRight)
    window.mylayout.addWidget(window.input_megerosito_jelszo,3,0,1,1)
    window.mylayout.addWidget(window.errorUzenet,4,0,1,1)
    window.mylayout.addWidget(window.ures,1,1,4,1)
    window.mylayout.addWidget(window.regisztraciosGomb,5,0,1,2,Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
    window.mylayout.addWidget(window.Vissza,6,0,1,2,Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)