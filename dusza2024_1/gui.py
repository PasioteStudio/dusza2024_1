#Sigmakik
import sys
import kezelo

from PyQt5 import QtGui,QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout,QHBoxLayout,QGridLayout,QMainWindow,QScrollArea,QAbstractScrollArea,QGroupBox,QComboBox

class MyWindow(QWidget):
    def __init__(self):
        self.foCSS="""
            * {
                border:10px solid black;
                background-color: #666666;
                font-size:30px;
                border-radius:25px
            }
            #greet{
                font-size:100px;
            }
            #noBorder{
                border:none !important
            }
            #profilhatter{
                background-color:gold !important;
                
            }
            #profil_felhasznalonev, #profil_nev,#profil_pontszam,#ures{
                color:black;
                font-size:35px;
                border:none;
                background:none;
                margin-left: 50px;
            }
            #profil_kep{
                background: url('icon.jpg') no-repeat contain;
                border: 1px solid black;
                border-radius:150px !important;
            }
        """
        super().__init__()
        self.initUI()

    def initUI(self):
        

        # Layout létrehozása
        self.mylayout = QGridLayout(self)  
        self.mylayout.setObjectName("container")
        
        # Layout hozzáadása a main window-hoz
        self.setLayout(self.mylayout)
        
        self.main()
        

        # Képernyő méretei és pozíciója
        #self.mylayout.deleteLater()
        xCoord = 100
        yCoord = 100
        winWidht = 300
        winHeight = 150
        self.setGeometry(xCoord, yCoord, winWidht, winHeight)

        # Képernyő címe
        self.setWindowTitle('A Sorsod Borsod')
        
        icon_path="icon.jpg"
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.showMaximized() 
    
    def main(self):
        self.layoutvisszaallitasa()
        # CreateGomb létrehozása
        self.bejelentkezesGomb = QPushButton('Bejelentkezés', self)
        self.bejelentkezesGomb.clicked.connect(self.bejelentkezes_oldal)

        self.regisztraciosGomb = QPushButton('Regisztráció', self)
        self.regisztraciosGomb.clicked.connect(self.regisztracios_oldal)
        
        self.lekerdezesGomb = QPushButton('Lekérdezések', self)
        self.lekerdezesGomb.clicked.connect(self.lekerdezes)

        self.koszontes = QLabel('Üdvözöllek a fogadós játékba!', self)
        self.koszontes.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.koszontes.setObjectName("greet")
        
        
        self.setStyleSheet(self.foCSS)
        
        self.mylayout.addWidget(self.koszontes,0,0,1,3,QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mylayout.addWidget(self.bejelentkezesGomb,1,0,1,1)
        self.mylayout.addWidget(self.regisztraciosGomb,1,1,1,1)
        self.mylayout.addWidget(self.lekerdezesGomb,1,2,1,1)
    def lekerdezes(self):
        self.layoutvisszaallitasa()
        self.ranglistaGomb=QPushButton("Ranglista",self)
        self.ranglistaGomb.clicked.connect(self.ranglista)
        self.mylayout.addWidget(self.ranglistaGomb,0,0,1,1)
        
        self.jatekStatisztikaGomb=QPushButton("Játék statisztika",self)
        self.jatekStatisztikaGomb.clicked.connect(self.jatek_statisztika)
        self.mylayout.addWidget(self.jatekStatisztikaGomb,0,1,1,1)
        
        self.FogadasiStatisztikaGomb=QPushButton("Fogadási statisztika",self)
        self.FogadasiStatisztikaGomb.clicked.connect(self.fogadasi_statisztika)
        self.mylayout.addWidget(self.FogadasiStatisztikaGomb,0,2,1,1)
        
        self.Vissza=QPushButton("Vissza",self)
        self.Vissza.clicked.connect(self.main)
        self.mylayout.addWidget(self.Vissza,1,0,1,3)
    def regisztracios_oldal(self):
        self.layoutvisszaallitasa()
        self.setStyleSheet(self.foCSS+"""
                           #cim{
                               font-size:100px;
                                color:white;
                                padding-left: 100px;
                                padding-right:100px;
                                background-color:black;
                                border-radius:50px;
                                height:min-content
                           }
                           #felhasznalonev,#jelszo,#megerosito_jelszo,#error{
                                color:gold;
                                background-color:black;
                                font-weight:bold;
                                margin: 15px 0;
                                margin-left:100px;
                                font-size:35px;
                           }
                           #error{
                               margin:0 0 0 100px;
                           }
                           #jelszo_megjelenitese{
                               background-color:black
                           }
                           #regisztracioGomb{
                                color:gold;
                                background-color:black;
                                font-weight:bold;
                                font-size:75px;
                                padding: 10px 70px;
                           }
                           #vissza{
                                border:none;
                                color:black;
                                text-decoration: underline;
                           }
                           """)
        self.oldalCim=QLabel("Regisztráció",self)
        self.oldalCim.setObjectName("cim")
        
        self.input_felhasznalonev = QLineEdit(self)
        self.input_felhasznalonev.setPlaceholderText("Felhasználó neved")
        self.input_felhasznalonev.setObjectName("felhasznalonev")
        
        self.input_jelszo = QLineEdit(self)
        self.input_jelszo.setObjectName("jelszo")
        self.input_jelszo.textEdited.connect(lambda: kezelo.jelszo_rejtese(self.input_jelszo,"Jelszavad"))
        self.input_jelszo.setPlaceholderText("Jelszavad")
        self.input_jelszo.setProperty("canToggle",True)
        self.input_jelszo_megjelenitese = QPushButton('😃', self)
        self.input_jelszo_megjelenitese.setProperty("toggle","😄")
        self.input_jelszo_megjelenitese.clicked.connect(lambda: kezelo.jelszo_megjelenitese(self.input_jelszo,self.input_jelszo_megjelenitese,"Jelszavad"))
        self.input_jelszo_megjelenitese.setObjectName("jelszo_megjelenitese")
        
        self.input_megerosito_jelszo = QLineEdit(self)
        self.input_megerosito_jelszo.textEdited.connect(lambda: kezelo.jelszo_rejtese(self.input_megerosito_jelszo,"Jelszavad újra"))
        self.input_megerosito_jelszo.setPlaceholderText("Jelszavad újra")
        self.input_megerosito_jelszo.setProperty("canToggle",True)
        self.input_megerosito_jelszo.setObjectName("megerosito_jelszo")
        
        self.errorUzenet=QLabel(self)
        self.errorUzenet.setMaximumHeight(60)
        self.errorUzenet.setObjectName("error")
        self.keszGomb=QPushButton("Kész",self)
        def ErrorÜzenetek():
            valasz = kezelo.benyujtott_regisztracio(self.input_felhasznalonev,self.input_jelszo,self.input_megerosito_jelszo)
            if not valasz ==True:
                self.errorUzenet.setText(valasz)
            else:
                self.bejelentkezes_oldal()
        
        
        self.regisztraciosGomb = QPushButton('Regisztráció', self)
        self.regisztraciosGomb.clicked.connect(ErrorÜzenetek)
        self.regisztraciosGomb.setObjectName("regisztracioGomb")
        self.Vissza = QPushButton('Vissza a főoldalra', self)
        self.Vissza.clicked.connect(self.main)
        self.Vissza.setObjectName("vissza")
        
        self.ures=QWidget(self)
        self.ures.setObjectName("noBorder")
        self.resizeWidgets.append({
            "elem":self.ures,
            "mive":0
        })
        self.ures.setFixedWidth(int(self.frameGeometry().size().width()/2))
        self.mylayout.addWidget(self.oldalCim,0,0,1,2,QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop)
        self.mylayout.addWidget(self.input_felhasznalonev,1,0,1,1)
        self.mylayout.addWidget(self.input_jelszo,2,0,1,1)
        self.mylayout.addWidget(self.input_jelszo_megjelenitese,2,0,1,1,QtCore.Qt.AlignmentFlag.AlignRight)
        self.mylayout.addWidget(self.input_megerosito_jelszo,3,0,1,1)
        self.mylayout.addWidget(self.errorUzenet,4,0,1,1)
        self.mylayout.addWidget(self.ures,1,1,4,1)
        self.mylayout.addWidget(self.regisztraciosGomb,5,0,1,2,QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignBottom)
        self.mylayout.addWidget(self.Vissza,6,0,1,2,QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignBottom)
    def bejelentkezes_oldal(self):
        self.layoutvisszaallitasa()
        self.setStyleSheet(self.foCSS+"""
                    #cim{
                        font-size:100px;
                        color:white;
                        padding-left: 100px;
                        padding-right:100px;
                        background-color:black;
                        border-radius:50px;
                        height:min-content
                    }
                    #felhasznalonev,#jelszo,#megerosito_jelszo,#error{
                        color:gold;
                        background-color:black;
                        font-weight:bold;
                        margin: 15px 0;
                        margin-left:100px;
                        font-size:35px;
                    }
                    #error{
                        margin:0 0 0 100px;
                    }
                    #jelszo_megjelenitese{
                        background-color:black
                    }
                    #regisztracioGomb{
                        color:gold;
                        background-color:black;
                        font-weight:bold;
                        font-size:75px;
                        padding: 10px 70px;
                    }
                    #vissza{
                        border:none;
                        color:black;
                        text-decoration: underline;
                    }
                    """)
        # Bemeneti mező létrehozása
        self.oldalCim=QLabel("Bejelentkezés")
        self.oldalCim.setObjectName("cim")
        
        self.input_felhasznalonev = QLineEdit(self)
        self.input_felhasznalonev.setPlaceholderText("Felhasználó neved")
        self.input_felhasznalonev.setObjectName("felhasznalonev")
        
        self.input_jelszo = QLineEdit(self)
        self.input_jelszo.setPlaceholderText("Jelszavad")
        self.input_jelszo.setObjectName("jelszo")
        self.input_jelszo.textEdited.connect(lambda: kezelo.jelszo_rejtese(self.input_jelszo,"Jelszavad"))
        self.input_jelszo.setProperty("canToggle",True)
        self.input_jelszo_megjelenitese = QPushButton('😃', self)
        self.input_jelszo_megjelenitese.setProperty("toggle","😄")
        self.input_jelszo_megjelenitese.setMaximumWidth(100)
        self.input_jelszo_megjelenitese.setObjectName("jelszo_megjelenitese")
        self.input_jelszo_megjelenitese.clicked.connect(lambda: kezelo.jelszo_megjelenitese(self.input_jelszo,self.input_jelszo_megjelenitese,"Jelszavad"))
        
        self.errorUzenet=QLabel(self)
        self.errorUzenet.setMaximumHeight(60)
        self.errorUzenet.setObjectName("error")
        self.bejelentkezesGomb = QPushButton('Bejelentkezés', self)
        def ErrorUzenet():
            szotar=kezelo.benyujtott_bejelentkezes(self.input_felhasznalonev,self.input_jelszo)
            if szotar["státusz"]==True:
                felhasznalonev,nev=szotar["válasz"]
                self.bejelentkezett_oldal(felhasznalonev)
            else:
                self.errorUzenet.setText(szotar["válasz"])
        self.bejelentkezesGomb.clicked.connect(ErrorUzenet)
        self.bejelentkezesGomb.setObjectName("regisztracioGomb")#TODO
        self.Vissza = QPushButton('Vissza a főoldalra', self)
        self.Vissza.clicked.connect(self.main)
        self.Vissza.setObjectName("vissza")
        
        self.ures=QWidget(self)
        self.ures.setObjectName("noBorder")
        self.resizeWidgets.append({
            "elem":self.ures,
            "mive":0
        })
        self.ures.setFixedWidth(int(self.frameGeometry().size().width()/2))
        
        self.mylayout.addWidget(self.oldalCim,0,0,1,2,QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop)
        self.mylayout.addWidget(self.input_felhasznalonev,1,0,1,1)
        self.mylayout.addWidget(self.ures,1,1,3,1)
        self.mylayout.addWidget(self.input_jelszo,2,0,1,1)
        self.mylayout.addWidget(self.input_jelszo_megjelenitese,2,0,1,1,QtCore.Qt.AlignmentFlag.AlignRight)
        self.mylayout.addWidget(self.errorUzenet,3,0,1,1)
        self.mylayout.addWidget(self.bejelentkezesGomb,4,0,1,2,QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignBottom)
        self.mylayout.addWidget(self.Vissza,5,0,1,2,QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignBottom)
    def layoutvisszaallitasa(self):
        self.resizeWidgets=[]
        self.setStyleSheet(self.foCSS)
        while self.mylayout.count():
            child = self.mylayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    def mindig_latszik_belepve(self, felhasznalonev:str):
        nev=kezelo.felhasznalo_neve(felhasznalonev)
        pont=kezelo.dinamikusPontSzamolás(felhasznalonev)
        
        self.pont = QLabel(f"Pontszám: {pont}", self)
        self.pont.setObjectName("profil_pontszam")
        self.felhasznalonev = QLabel(f"Név: {felhasznalonev}", self)
        self.felhasznalonev.setObjectName("profil_felhasznalonev")
        self.nev = QLabel(f"Megjelenített név: {nev}", self)
        self.nev.setObjectName("profil_nev")
        self.kep = QLabel(self)
        self.kep.setObjectName("profil_kep")
        self.kep.setFixedHeight(300)
        self.kep.setFixedWidth(300)
        
        self.hatter2=QWidget(self)
        self.hatter2.setObjectName("profilhatter")
        
        self.ures=QWidget(self)
        self.ures.setObjectName("ures")
        
        
        self.mylayout.addWidget(self.kep,0,0,3,1,QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mylayout.addWidget(self.hatter2,0,0,7,1)
        self.mylayout.addWidget(self.pont,3,0,1,1,QtCore.Qt.AlignmentFlag.AlignTop)
        self.mylayout.addWidget(self.felhasznalonev,3,0,1,1,QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.mylayout.addWidget(self.nev,3,0,1,1,QtCore.Qt.AlignmentFlag.AlignBottom)
        self.mylayout.addWidget(self.ures,4,0,3,1)
        
        self.hatter2.show()
        self.hatter2.lower()
        
        return nev
    def fogado_oldal(self,felhasznalonev:str):
        self.layoutvisszaallitasa()
        self.mindig_latszik_belepve(felhasznalonev)
        
    
        self.osszesJatekTarolo=QScrollArea(self)
        self.osszesJatekTarolo.setWidgetResizable(True)
        self.osszesJatekTarolo.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.osszesJatekTarolo.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.osszesJatek=QVBoxLayout(self.osszesJatekTarolo)
        self.osszesJatekBox = QGroupBox()
        self.osszesJatekBox.setLayout(self.osszesJatek)
        self.osszesJatekTarolo.setWidget(self.osszesJatekBox)
        
        self.mylayout.addWidget(self.osszesJatekTarolo,2,1,1,1)
        self.elerheto_jatekok = QLabel("Le nem zárt játékok:",self.osszesJatekTarolo)
        self.osszesJatek.addWidget(self.elerheto_jatekok)
    
        for jatek in kezelo.le_van_e_zarva_osszes_jatekot_vissza_adja():
            
            substring1=[", "]*len(jatek["alanyok"])
            substring2=[", "]*len(jatek["esemenyek"])
            substrings=[substring1,substring2]
            self.current=0
            def orulet(x,y,melyik):
                self.current+=1
                if self.current==len(substrings[melyik]):
                    self.current=0
                    return x
                return x+y
            alanyok="".join(map(str,map(lambda x,y: orulet(x,y,0),jatek["alanyok"],substrings[0])))
            esemenyek="".join(map(str,map(lambda x,y: orulet(x,y,1),jatek["esemenyek"],substrings[1])))
            #Hozzáadom az alanyokhoz az egyes alanyt és egy vesszőt, az utolsó elemnél a vesszőt mindig elhagyom és ezt megcsinálom az eseményekkel is
            self.jatek_neve = QLabel(f"{jatek['jatek_neve']}\n{alanyok}\n{esemenyek}\n", self.osszesJatekTarolo)
            self.jatek_neve.setMaximumHeight(180)
            self.fogadasGomb = QPushButton('Fogadás', self.osszesJatekTarolo)
            self.fogadasGomb.clicked.connect(lambda: self.fogadas_leadasa(jatek,felhasznalonev))
            self.osszesJatek.addWidget(self.jatek_neve)
            self.osszesJatek.addWidget(self.fogadasGomb)
        
        self.Vissza = QPushButton('Vissza', self)
        self.Vissza.clicked.connect(lambda: self.bejelentkezett_oldal(felhasznalonev))
        self.mylayout.addWidget(self.Vissza)
    def szervezo_oldal(self,felhasznalonev:str):
        self.layoutvisszaallitasa()
        self.mindig_latszik_belepve(felhasznalonev)
        
        self.jatek_letrehozas = QPushButton('Játék létrehozása', self)
        self.jatek_letrehozas.clicked.connect(lambda: self.jatek_letrehozasa(felhasznalonev))
        self.mylayout.addWidget(self.jatek_letrehozas,1,1,1,1)
          
        self.osszesJatekTarolo=QScrollArea(self)
        self.osszesJatekTarolo.setWidgetResizable(True)
        self.osszesJatekTarolo.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.osszesJatekTarolo.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.osszesJatek=QVBoxLayout(self.osszesJatekTarolo)
        self.osszesJatekBox = QGroupBox()
        self.osszesJatekBox.setLayout(self.osszesJatek)
        self.osszesJatekTarolo.setWidget(self.osszesJatekBox)
        
        self.mylayout.addWidget(self.osszesJatekTarolo,2,1,1,1)
        self.elerheto_jatekok = QLabel("Le nem zárt játékaid:",self.osszesJatekTarolo)
        self.osszesJatek.addWidget(self.elerheto_jatekok)
        for jatek in map(lambda x: kezelo.jatekot_felhasznalo_szervezte(x,felhasznalonev), kezelo.le_van_e_zarva_osszes_jatekot_vissza_adja()):
            if jatek == None:
                continue
            
            substring1=[", "]*len(jatek["alanyok"])
            substring2=[", "]*len(jatek["esemenyek"])
            substrings=[substring1,substring2]
            self.current=0
            def orulet(x,y,melyik):
                self.current+=1
                if self.current==len(substrings[melyik]):
                    self.current=0
                    return x
                return x+y
            alanyok="".join(map(str,map(lambda x,y: orulet(x,y,0),jatek["alanyok"],substrings[0])))
            esemenyek="".join(map(str,map(lambda x,y: orulet(x,y,1),jatek["esemenyek"],substrings[1])))
            #Hozzáadom az alanyokhoz az egyes alanyt és egy vesszőt, az utolsó elemnél a vesszőt mindig elhagyom és ezt megcsinálom az eseményekkel is
            
            self.jatek_neve = QLabel(f"{jatek['jatek_neve']}\n{alanyok}\n{esemenyek}\n", self.osszesJatekTarolo)
            self.jatek_neve.setMaximumHeight(180)
            self.lezarasGomb = QPushButton('Játék lezárása', self.osszesJatekTarolo)
            self.lezarasGomb.clicked.connect(lambda: self.lezaras(jatek,felhasznalonev))
            self.osszesJatek.addWidget(self.jatek_neve)
            self.osszesJatek.addWidget(self.lezarasGomb)
        
        
        self.Vissza = QPushButton('Vissza', self)
        self.Vissza.clicked.connect(lambda: self.bejelentkezett_oldal(felhasznalonev))
        self.mylayout.addWidget(self.Vissza,3,1,1,1)
    def jatek_letrehozasa(self,felhasznalonev:str):
        self.layoutvisszaallitasa()
        self.mindig_latszik_belepve(felhasznalonev)
        
        self.megnevezes = QLabel("Mi a játék megnevezése? (egyedinek kell lennie) ",self)
        
        self.megnevezes_input=QLineEdit(self)
        self.megnevezes_input.setPlaceholderText("Megnevezése")
        self.alanyok_label = QLabel("Kik az alanyok? (különböznek egymástól)",self)
        self.esemenyek_label = QLabel("Mik az események? (különböznek egymástól)",self)
        self.mylayout.addWidget(self.megnevezes,1,1,1,1)
        self.mylayout.addWidget(self.megnevezes_input,1,2,1,1)

        alap_alanyok_szama=2
        alap_esemenyek_szama=2
        
        self.osszesAlanyTarolo=QScrollArea(self)
        self.osszesAlanyTarolo.setWidgetResizable(True)
        self.osszesAlanyTarolo.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.osszesAlanyTarolo.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.osszesEsemenyTarolo=QScrollArea(self)
        self.osszesEsemenyTarolo.setWidgetResizable(True)
        self.osszesEsemenyTarolo.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.osszesEsemenyTarolo.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        self.osszesAlany=QGridLayout(self.osszesAlanyTarolo)
        self.osszesEsemeny = QGridLayout(self.osszesEsemenyTarolo)
        
        self.osszesAlanyBox = QGroupBox()
        self.osszesAlanyBox.setLayout(self.osszesAlany)
        self.osszesAlanyTarolo.setWidget(self.osszesAlanyBox)
        
        self.osszesEsemenyBox = QGroupBox()
        self.osszesEsemenyBox.setLayout(self.osszesEsemeny)
        self.osszesEsemenyTarolo.setWidget(self.osszesEsemenyBox)

        self.alanyok_plusz=QPushButton("+",self)
        self.alanyok_plusz.setMaximumWidth(100)
        self.esemenyek_plusz=QPushButton("+",self)
        self.esemenyek_plusz.setMaximumWidth(100)
        self.alanyok_plusz.clicked.connect(lambda: kezelo.plusAlanyokésEsemenyek(1,0,self.osszesAlany,self.osszesEsemeny,self.osszesAlanyBox,self.osszesEsemenyBox))
        self.esemenyek_plusz.clicked.connect(lambda: kezelo.plusAlanyokésEsemenyek(0,1,self.osszesAlany,self.osszesEsemeny,self.osszesAlanyBox,self.osszesEsemenyBox))
        self.mylayout.addWidget(self.alanyok_label,2,1,1,1)
        self.mylayout.addWidget(self.alanyok_plusz,2,2,1,1,QtCore.Qt.AlignmentFlag.AlignRight)
        self.mylayout.addWidget(self.osszesAlanyTarolo,3,1,1,2)
        kezelo.plusAlanyokésEsemenyek(alap_alanyok_szama,0,self.osszesAlany,self.osszesEsemeny,self.osszesAlanyBox,self.osszesEsemenyBox)
        self.mylayout.addWidget(self.esemenyek_label,4,1,1,1)
        self.mylayout.addWidget(self.esemenyek_plusz,4,2,1,1,QtCore.Qt.AlignmentFlag.AlignRight)
        self.mylayout.addWidget(self.osszesEsemenyTarolo,5,1,1,2)
        kezelo.plusAlanyokésEsemenyek(0,alap_esemenyek_szama,self.osszesAlany,self.osszesEsemeny,self.osszesAlanyBox,self.osszesEsemenyBox)
        
        self.errorUzenet=QLabel(self)
        self.errorUzenet.setMaximumHeight(60)
        self.mylayout.addWidget(self.errorUzenet,6,1,1,2)
        
        self.keszGomb=QPushButton("Kész",self)
        def ErrorÜzenetek():
            valasz = kezelo.benyujtott_jatek_letrehozasa(felhasznalonev,self.megnevezes_input,self.osszesAlanyBox,self.osszesEsemenyBox)
            if not valasz ==True:
                self.errorUzenet.setText(valasz) #Error üzenet
        self.keszGomb.clicked.connect(ErrorÜzenetek)
        
        
        
        
        self.mylayout.addWidget(self.keszGomb,7,1,1,1)
        self.Vissza=QPushButton("Vissza",self)
        self.Vissza.clicked.connect(lambda: self.szervezo_oldal(felhasznalonev))
        self.mylayout.addWidget(self.Vissza,7,2,1,1)
    def lezaras(self,jatek,felhasznalonev:str):
        self.layoutvisszaallitasa()
        self.mindig_latszik_belepve(felhasznalonev)
        self.alanyok_es_esemyenek_uzenetek=[]
        for alany in jatek['alanyok']:
            for esemeny in jatek['esemenyek']: 
                self.uzenet= QLineEdit(self)
                self.uzenet.setPlaceholderText(f"{alany} és {esemeny}")
                self.uzenet.setProperty("alany",alany)
                self.uzenet.setProperty("esemeny",esemeny)
                self.alanyok_es_esemyenek_uzenetek.append(self.uzenet)
                self.mylayout.addWidget(self.uzenet)
                
        self.keszGomb=QPushButton("Kész",self)
        def CircularImport():
            kezelo.benyujtott_eredmeny(jatek,self.alanyok_es_esemyenek_uzenetek)
            self.uzenet= QLabel(f"{jatek['jatek_neve']} lezárva!",self)
            self.mylayout.addWidget(self.uzenet)
            self.szervezo_oldal(felhasznalonev)
        self.keszGomb.clicked.connect(CircularImport)

        self.mylayout.addWidget(self.keszGomb)
        self.Vissza = QPushButton("Vissza",self)
        self.Vissza.clicked.connect(lambda: self.szervezo_oldal(felhasznalonev))
        self.mylayout.addWidget(self.Vissza)
    def bejelentkezett_oldal(self,felhasznalonev:str):
        self.layoutvisszaallitasa()
        self.mindig_latszik_belepve(felhasznalonev)
        self.setStyleSheet(self.foCSS+"""
                    #cim{
                        font-size:100px;
                        color:white;
                        padding-left: 100px;
                        padding-right:100px;
                        background-color:black;
                        border-radius:50px;
                        height:min-content
                    }
                    #vissza{
                        border:none;
                        color:black;
                        text-decoration: underline;
                    }
                    #fogado,#szervezo{
                        background-color:yellow;
                        padding-top:50px;
                        padding-bottom:250px;
                        margin-top:0;
                    }
                    """)
        
        self.beallitasok=QPushButton("⚙️",self)
        self.beallitasok.clicked.connect(lambda: self.profil_beallitasok(felhasznalonev))
        
        self.szerepkor = QLabel(f"Szerepválasztás", self)
        self.szerepkor.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.szerepkor.setObjectName("cim")
        
        self.szervezo = QPushButton('Szervező', self)
        self.szervezo.clicked.connect(lambda: self.szervezo_oldal(felhasznalonev))
        self.szervezo.setObjectName("szervezo")
        
        self.fogado = QPushButton('Fogadó', self)
        self.fogado.clicked.connect(lambda: self.fogado_oldal(felhasznalonev))
        self.fogado.setObjectName("fogado")
        
        self.Vissza = QPushButton('Vissza a főoldalra', self)
        self.Vissza.clicked.connect(self.main)
        self.Vissza.setObjectName("vissza")
        
        #self.mylayout.addWidget(self.beallitasok,0,1,1,1)
        self.mylayout.addWidget(self.szerepkor,0,1,1,2)
        self.mylayout.addWidget(self.szervezo,1,1,3,1)
        self.mylayout.addWidget(self.fogado,1,2,3,1)
        self.mylayout.addWidget(self.Vissza,3,0,1,3,QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignBottom)
    def fogadas_leadasa(self,jatek:dict,felhasznalonev:str):
        self.layoutvisszaallitasa()
        self.mindig_latszik_belepve(felhasznalonev)
        
        self.kivalasztott_jatek_neve=QLabel(f"{jatek['jatek_neve']}-hoz való fogadás:",self)
        self.mylayout.addWidget(self.kivalasztott_jatek_neve,1,1,1,2)
        
        self.kivalasztott_alany=QLabel("Kiválasztandó alany:",self)
        self.kivalasztott_alany_input=QComboBox(self)
        self.kivalasztott_alany_input.addItems(jatek["alanyok"])
        self.mylayout.addWidget(self.kivalasztott_alany,2,1,1,1)
        self.mylayout.addWidget(self.kivalasztott_alany_input,2,2,1,1)
        
        self.kivalasztott_esemeny=QLabel("Kiválasztandó esemény:",self)
        self.kivalasztott_esemeny_input=QComboBox(self)
        self.kivalasztott_esemeny_input.addItems(jatek["esemenyek"])
        self.mylayout.addWidget(self.kivalasztott_esemeny,3,1,1,1)
        self.mylayout.addWidget(self.kivalasztott_esemeny_input,3,2,1,1)
        
        self.ertek=QLabel("Válassz egy értéket!",self)
        self.ertek_input=QLineEdit(self)
        self.ertek_input.setPlaceholderText("érték")
        self.mylayout.addWidget(self.ertek,4,1,1,1)
        self.mylayout.addWidget(self.ertek_input,4,2,1,1)
        
        self.tet=QLabel("Válassz egy tétet!",self)
        self.tet_input=QLineEdit(self)
        self.tet_input.setPlaceholderText("tét")
        self.mylayout.addWidget(self.tet,5,1,1,1)
        self.mylayout.addWidget(self.tet_input,5,2,1,1)
        
        self.errorUzenet=QLabel(self)
        self.mylayout.addWidget(self.errorUzenet,6,1,1,2)
        
        def ErrorÜzenetek():
            valasz = kezelo.benyujtott_fogadas(felhasznalonev,jatek,self.kivalasztott_alany_input,self.kivalasztott_esemeny_input,self.ertek_input,self.tet_input)
            if not valasz == True:
                self.errorUzenet.setText(valasz)
            else:
                self.fogado_oldal(felhasznalonev)
        
        self.fogadasGomb=QPushButton("Fogadás leadása!",self)
        self.fogadasGomb.clicked.connect(ErrorÜzenetek)
        self.mylayout.addWidget(self.fogadasGomb,7,2,1,1)
        
        self.Vissza=QPushButton("Vissza",self)
        self.Vissza.clicked.connect(lambda: self.fogado_oldal(felhasznalonev))
        self.mylayout.addWidget(self.Vissza,7,1,1,1)
    def ranglista(self):
        self.layoutvisszaallitasa()
        
        self.osszesJatekosTarolo=QScrollArea(self)
        self.osszesJatekosTarolo.setWidgetResizable(True)
        self.osszesJatekosTarolo.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.osszesJatekosTarolo.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.osszesJatekos=QVBoxLayout(self.osszesJatekosTarolo)
        self.osszesJatekosBox = QGroupBox()
        self.osszesJatekosBox.setLayout(self.osszesJatekos)
        self.osszesJatekosTarolo.setWidget(self.osszesJatekosBox)
        
        self.mylayout.addWidget(self.osszesJatekosTarolo,1,0,1,1)
        self.jatekosok_label = QLabel("Összes játékos:",self.osszesJatekosTarolo)
        self.jatekosok_label.setMaximumHeight(100)
        self.osszesJatekos.addWidget(self.jatekosok_label)
        
        jatekosok=kezelo.ranglista_guihoz()
        for id,jatekos in enumerate(jatekosok["nev_sorrendben"]):
            self.jatekos_label = QLabel(f"{jatekosok['igazi_helyezes'][id]}. helyen: {jatekos}, {jatekosok['pontszam_sorrendben'][id]} ponttal",self.osszesJatekosTarolo)
            self.jatekos_label.setMaximumHeight(100)
            self.osszesJatekos.addWidget(self.jatekos_label)
        self.Vissza=QPushButton("Vissza",self)
        self.Vissza.clicked.connect(self.lekerdezes)
        self.mylayout.addWidget(self.Vissza,2,0,1,1)
    def jatek_statisztika(self):
        self.layoutvisszaallitasa()
        
        self.osszesJatekTarolo=QScrollArea(self)
        self.osszesJatekTarolo.setWidgetResizable(True)
        self.osszesJatekTarolo.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.osszesJatekTarolo.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.osszesJatek=QVBoxLayout(self.osszesJatekTarolo)
        self.osszesJatekBox = QGroupBox()
        self.osszesJatekBox.setLayout(self.osszesJatek)
        self.osszesJatekTarolo.setWidget(self.osszesJatekBox)
        
        self.mylayout.addWidget(self.osszesJatekTarolo,1,0,1,1)
        self.jatekok_label = QLabel("Összes játék:",self.osszesJatekTarolo)
        self.jatekok_label.setMaximumHeight(100)
        self.osszesJatek.addWidget(self.jatekok_label)
        
        jatekok = kezelo.jatek_statisztika_guihoz()
        for jatek in jatekok:
            self.jatek_label = QLabel(f"{jatek['jatek_neve']}-ban/-ben\n{jatek['fogadasok_szama']}db fogadása van\n{jatek['nyeremenyek_osszpontszama']} összpontszáma van a nyereményeknek a játékhoz",self.osszesJatekTarolo)
            self.jatek_label.setMaximumHeight(200)
            self.osszesJatek.addWidget(self.jatek_label)
        self.Vissza=QPushButton("Vissza",self)
        self.Vissza.clicked.connect(self.lekerdezes)
        self.mylayout.addWidget(self.Vissza,2,0,1,1)
    def fogadasi_statisztika(self):
        self.layoutvisszaallitasa()
        
        self.kivalasztott_jatek=QComboBox(self)
        self.kivalasztott_jatek.addItems(kezelo.osszesJatek())
        self.kivalasztott_jatek.currentIndexChanged.connect(lambda:kezelo.fogadasiStatisztikaKivalasztottjatekInputahoz(self.kivalasztott_jatek,self.osszesAlanyEsemeny,self.osszesAlanyEsemenyTarolo))
        self.mylayout.addWidget(self.kivalasztott_jatek,0,0,1,1)
        
        self.osszesAlanyEsemenyTarolo=QScrollArea(self)
        self.osszesAlanyEsemenyTarolo.setWidgetResizable(True)
        self.osszesAlanyEsemenyTarolo.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.osszesAlanyEsemenyTarolo.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.osszesAlanyEsemeny=QVBoxLayout(self.osszesAlanyEsemenyTarolo)
        self.osszesAlanyEsemenyBox = QGroupBox()
        self.osszesAlanyEsemenyBox.setLayout(self.osszesAlanyEsemeny)
        self.osszesAlanyEsemenyTarolo.setWidget(self.osszesAlanyEsemenyBox)
        
        self.mylayout.addWidget(self.osszesAlanyEsemenyTarolo,1,0,1,1)
        self.alanyEsemeny_label = QLabel("Összes alany és esemény:",self.osszesAlanyEsemenyTarolo)
        self.alanyEsemeny_label.setMaximumHeight(100)
        self.osszesAlanyEsemeny.addWidget(self.alanyEsemeny_label)
        
        self.Vissza=QPushButton("Vissza",self)
        self.Vissza.clicked.connect(self.lekerdezes)
        self.mylayout.addWidget(self.Vissza,2,0,1,1)
    def profil_beallitasok(self,felhasznalonev:str):
        self.layoutvisszaallitasa()
        nev = self.mindig_latszik_belepve(felhasznalonev)
        
        self.megjelenitett_nev_label=QLabel("Megjelenített neved megváltoztatása:",self)
        self.mylayout.addWidget(self.megjelenitett_nev_label,1,0,1,1)
        
        self.megjelenitett_nev_input=QLineEdit(nev,self)
        self.megjelenitett_nev_input.setPlaceholderText("megjelenitett nev")
        self.mylayout.addWidget(self.megjelenitett_nev_input,1,1,1,1)
        
        self.errorUzenet=QLabel(self)
        self.errorUzenet.setMaximumHeight(60)
        self.mylayout.addWidget(self.errorUzenet,2,0,1,2)
        
        def ErrorÜzenetek():
            valasz = kezelo.benyujtott_profilbeallitasok(felhasznalonev,self.megjelenitett_nev_input)
            if not valasz == True:
                self.errorUzenet.setText()
            else:
                self.bejelentkezett_oldal(felhasznalonev)
        self.mentes=QPushButton("Mentés",self)
        self.mentes.clicked.connect(ErrorÜzenetek)
        self.mylayout.addWidget(self.mentes,3,1,1,1)
        
        self.Vissza=QPushButton("Vissza",self)
        self.Vissza.clicked.connect(lambda: self.bejelentkezett_oldal(felhasznalonev))
        self.mylayout.addWidget(self.Vissza,3,0,1,1)
    def resizeEvent(self, event):
        print(self.frameGeometry().size())
        self.mivek=[int(self.frameGeometry().size().width()/2)]
        print("Window has been resized")
        for element in self.resizeWidgets:
            print(len(self.resizeWidgets))
            element["elem"].setFixedWidth(self.mivek[element["mive"]])
        QWidget.resizeEvent(self, event)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # képernyő létrehozása
    window = MyWindow()
    window.show()
    
    
    sys.exit(app.exec_())
#TODO: design, ppt, dinamikus szorzó, egyéb ötletek