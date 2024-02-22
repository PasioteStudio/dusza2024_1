#Sigmakik
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout,QScrollArea,QGroupBox,QLineEdit,QGridLayout
import kezelo
def szervezo_oldal(window,felhasznalonev:str):
        window.layoutvisszaallitasa()
        window.mindig_latszik_belepve(felhasznalonev)
        
        window.jatek_letrehozas = QPushButton('Játék létrehozása', window)
        window.jatek_letrehozas.clicked.connect(lambda: window.jatek_letrehozasa(felhasznalonev))
        window.jatek_letrehozas.setObjectName("jatekLetrehozasGomb")
        window.mylayout.addWidget(window.jatek_letrehozas,1,1,1,1)
          
        window.osszesJatekTarolo=QScrollArea(window)
        window.osszesJatekTarolo.setWidgetResizable(True)
        window.osszesJatekTarolo.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        window.osszesJatekTarolo.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        window.osszesJatek=QVBoxLayout(window.osszesJatekTarolo)
        window.osszesJatekBox = QGroupBox()
        window.osszesJatekBox.setLayout(window.osszesJatek)
        window.osszesJatekTarolo.setWidget(window.osszesJatekBox)
        window.osszesJatekTarolo.setObjectName("jatek_tarolo")
        
        window.mylayout.addWidget(window.osszesJatekTarolo,2,1,1,1)
        window.elerheto_jatekok = QLabel("Le nem zárt játékaid:",window.osszesJatekTarolo)
        window.elerheto_jatekok.setObjectName("elerheto")
        window.osszesJatek.addWidget(window.elerheto_jatekok)
        for jatek in map(lambda x: kezelo.jatekot_felhasznalo_szervezte(x,felhasznalonev), kezelo.le_van_e_zarva_osszes_jatekot_vissza_adja()):
            if jatek == None:
                continue
            
            substring1=[", "]*len(jatek["alanyok"])
            substring2=[", "]*len(jatek["esemenyek"])
            substrings=[substring1,substring2]
            window.current=0
            def orulet(x,y,melyik):
                window.current+=1
                if window.current==len(substrings[melyik]):
                    window.current=0
                    return x
                return x+y
            alanyok="".join(map(str,map(lambda x,y: orulet(x,y,0),jatek["alanyok"],substrings[0])))
            esemenyek="".join(map(str,map(lambda x,y: orulet(x,y,1),jatek["esemenyek"],substrings[1])))
            #Hozzáadom az alanyokhoz az egyes alanyt és egy vesszőt, az utolsó elemnél a vesszőt mindig elhagyom és ezt megcsinálom az eseményekkel is
            
            window.jatek_neve = QLabel(f"{jatek['jatek_neve']}\n{alanyok}\n{esemenyek}\n", window.osszesJatekTarolo)
            window.jatek_neve.setMaximumHeight(180)
            window.jatek_neve.setObjectName("jatek")
            lezarasGomb = QPushButton('Játék lezárása', window.osszesJatekTarolo)
            lezarasGomb.setProperty("jatek",jatek["jatek_neve"])
            lezarasGomb.clicked.connect(lambda: window.lezaras(felhasznalonev))
            lezarasGomb.setObjectName("lezarasGomb")
            window.osszesJatek.addWidget(window.jatek_neve)
            window.osszesJatek.addWidget(lezarasGomb)
        
        window.Vissza = QPushButton('Vissza a szerepválasztáshoz', window)
        window.Vissza.setObjectName("vissza")
        window.Vissza.clicked.connect(lambda: window.bejelentkezett_oldal(felhasznalonev))
        window.mylayout.addWidget(window.Vissza,3,1,1,1)
def lezaras(window,felhasznalonev:str):
    window.layoutvisszaallitasa()
    window.mindig_latszik_belepve(felhasznalonev)

    def jatekneve():  
        for jatek2 in map(lambda x: kezelo.jatekot_felhasznalo_szervezte(x,felhasznalonev), kezelo.le_van_e_zarva_osszes_jatekot_vissza_adja()):
            if jatek2["jatek_neve"]==window.sender().property("jatek"):
                return jatek2
    jatek = jatekneve()
    window.jatek_neve=QLabel(f"{jatek['jatek_neve']}-hoz való eredmények:")
    window.jatek_neve.setObjectName("jatekNeve")
    window.alanyok_es_esemyenek_uzenetek=[]
    for alany in jatek['alanyok']:
        for esemeny in jatek['esemenyek']: 
            window.uzenet= QLineEdit(window)
            window.uzenet_label=QLabel(f"{alany} és {esemeny}-hoz/höz eredmény:",window)
            window.uzenet.setPlaceholderText(f"{alany} és {esemeny}")
            window.uzenet.setProperty("alany",alany)
            window.uzenet.setProperty("esemeny",esemeny)
            window.uzenet.setObjectName("alany")
            window.uzenet_label.setObjectName("MentesGomb")
            window.alanyok_es_esemyenek_uzenetek.append(window.uzenet)
            window.mylayout.addWidget(window.uzenet,len(window.alanyok_es_esemyenek_uzenetek),2,1,1)
            window.mylayout.addWidget(window.uzenet_label,len(window.alanyok_es_esemyenek_uzenetek),1,1,1)
    window.keszGomb=QPushButton("Kész",window)
    def CircularImport():
        kezelo.benyujtott_eredmeny(jatek,window.alanyok_es_esemyenek_uzenetek)
        window.uzenet= QLabel(f"{jatek['jatek_neve']} lezárva!",window)
        window.mylayout.addWidget(window.uzenet)
        window.szervezo_oldal(felhasznalonev)
    window.keszGomb.clicked.connect(CircularImport)
    window.keszGomb.setObjectName("MentesGomb")
    window.mylayout.addWidget(window.jatek_neve,0,1,1,2)
    alja=1+len(window.alanyok_es_esemyenek_uzenetek)
    if alja < 7:
        alja=7
    window.mylayout.addWidget(window.keszGomb,alja,2,1,1,Qt.AlignmentFlag.AlignBottom)
    window.Vissza = QPushButton("Vissza a szervező oldalra",window)
    window.Vissza.clicked.connect(lambda: window.szervezo_oldal(felhasznalonev))
    window.Vissza.setObjectName("vissza")
    window.mylayout.addWidget(window.Vissza,alja,1,1,1,Qt.AlignmentFlag.AlignBottom)
def jatek_letrehozasa(window,felhasznalonev:str):
    window.layoutvisszaallitasa()
    window.mindig_latszik_belepve(felhasznalonev)
    
    window.megnevezes = QLabel("Mi a játék megnevezése? (egyedinek kell lennie) ",window)
    window.megnevezes.setObjectName("noBorder")
    
    window.megnevezes_input=QLineEdit(window)
    window.megnevezes_input.setPlaceholderText("Megnevezése")
    window.alanyok_label = QLabel("Kik az alanyok? (különböznek egymástól)",window)
    window.alanyok_label.setObjectName("noBorder")
    window.esemenyek_label = QLabel("Mik az események? (különböznek egymástól)",window)
    window.esemenyek_label.setObjectName("noBorder")
    window.mylayout.addWidget(window.megnevezes,1,1,1,1)
    window.mylayout.addWidget(window.megnevezes_input,1,2,1,1)

    alap_alanyok_szama=2
    alap_esemenyek_szama=2
    
    window.osszesAlanyTarolo=QScrollArea(window)
    window.osszesAlanyTarolo.setWidgetResizable(True)
    window.osszesAlanyTarolo.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
    window.osszesAlanyTarolo.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    window.osszesEsemenyTarolo=QScrollArea(window)
    window.osszesEsemenyTarolo.setWidgetResizable(True)
    window.osszesEsemenyTarolo.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
    window.osszesEsemenyTarolo.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    
    window.osszesAlany=QGridLayout(window.osszesAlanyTarolo)
    window.osszesEsemeny = QGridLayout(window.osszesEsemenyTarolo)
    
    window.osszesAlanyBox = QGroupBox()
    window.osszesAlanyBox.setLayout(window.osszesAlany)
    window.osszesAlanyTarolo.setWidget(window.osszesAlanyBox)
    
    window.osszesEsemenyBox = QGroupBox()
    window.osszesEsemenyBox.setLayout(window.osszesEsemeny)
    window.osszesEsemenyTarolo.setWidget(window.osszesEsemenyBox)

    window.alanyok_plusz=QPushButton("+",window)
    window.alanyok_plusz.setMaximumWidth(100)
    window.alanyok_plusz.setObjectName("noBorder")
    window.esemenyek_plusz=QPushButton("+",window)
    window.esemenyek_plusz.setMaximumWidth(100)
    window.esemenyek_plusz.setObjectName("noBorder")
    window.alanyok_plusz.clicked.connect(lambda: kezelo.plusAlanyokésEsemenyek(1,0,window.osszesAlany,window.osszesEsemeny,window.osszesAlanyBox,window.osszesEsemenyBox))
    window.esemenyek_plusz.clicked.connect(lambda: kezelo.plusAlanyokésEsemenyek(0,1,window.osszesAlany,window.osszesEsemeny,window.osszesAlanyBox,window.osszesEsemenyBox))
    window.mylayout.addWidget(window.alanyok_label,2,1,1,1)
    window.mylayout.addWidget(window.alanyok_plusz,2,2,1,1,Qt.AlignmentFlag.AlignRight)
    window.mylayout.addWidget(window.osszesAlanyTarolo,3,1,1,2)
    window.osszesAlanyTarolo.setObjectName("noBorder")
    kezelo.plusAlanyokésEsemenyek(alap_alanyok_szama,0,window.osszesAlany,window.osszesEsemeny,window.osszesAlanyBox,window.osszesEsemenyBox)
    window.mylayout.addWidget(window.esemenyek_label,4,1,1,1)
    window.mylayout.addWidget(window.esemenyek_plusz,4,2,1,1,Qt.AlignmentFlag.AlignRight)
    window.mylayout.addWidget(window.osszesEsemenyTarolo,5,1,1,2)
    window.osszesEsemenyTarolo.setObjectName("noBorder")
    kezelo.plusAlanyokésEsemenyek(0,alap_esemenyek_szama,window.osszesAlany,window.osszesEsemeny,window.osszesAlanyBox,window.osszesEsemenyBox)
    
    window.errorUzenet=QLabel(window)
    window.errorUzenet.setMaximumHeight(60)
    window.mylayout.addWidget(window.errorUzenet,6,1,1,2)
    
    window.keszGomb=QPushButton("Játék létrehozása",window)
    def ErrorÜzenetek():
        valasz = kezelo.benyujtott_jatek_letrehozasa(felhasznalonev,window.megnevezes_input,window.osszesAlanyBox,window.osszesEsemenyBox)
        if not valasz ==True:
            window.errorUzenet.setText(valasz)
        else:
            window.szervezo_oldal(felhasznalonev)
    window.keszGomb.clicked.connect(ErrorÜzenetek)
    window.keszGomb.setObjectName("jatekLetrehozasGomb")
    
    
    
    window.mylayout.addWidget(window.keszGomb,7,1,1,1)
    window.Vissza=QPushButton("Vissza a szervező oldalra",window)
    window.Vissza.setObjectName("vissza")
    window.Vissza.clicked.connect(lambda: window.szervezo_oldal(felhasznalonev))
    window.mylayout.addWidget(window.Vissza,7,2,1,1)