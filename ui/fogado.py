#Sigmakik
from PyQt5.QtCore import Qt
import kezelo
from PyQt5.QtWidgets import QLabel, QPushButton,QLineEdit,QComboBox,QScrollArea,QVBoxLayout,QGroupBox
def fogadas_leadasa(window,felhasznalonev:str):
        window.layoutvisszaallitasa()
        window.mindig_latszik_belepve(felhasznalonev)
        
        def jatekneve():
            for jatek2 in kezelo.le_van_e_zarva_osszes_jatekot_vissza_adja():
                if jatek2["jatek_neve"] == window.sender().property("jatek"):
                    return jatek2
        jatek=jatekneve()
        window.kivalasztott_jatek_neve=QLabel(f"{jatek['jatek_neve']}-hoz való fogadás:",window)
        window.mylayout.addWidget(window.kivalasztott_jatek_neve,0,1,1,2)
        window.kivalasztott_jatek_neve.setObjectName("fogadasi_statisztika_cim")
        
        window.kivalasztott_alany=QLabel("Kiválasztandó alany:",window)
        window.kivalasztott_alany_input=QComboBox(window)
        window.kivalasztott_alany_input.setObjectName("feherBg")
        window.kivalasztott_alany_input.addItems(jatek["alanyok"])
        window.kivalasztott_alany.setObjectName("alany")
        window.mylayout.addWidget(window.kivalasztott_alany,1,1,1,1)
        window.mylayout.addWidget(window.kivalasztott_alany_input,1,2,1,1)
        
        window.kivalasztott_esemeny=QLabel("Kiválasztandó esemény:",window)
        window.kivalasztott_esemeny.setObjectName("alany")
        window.kivalasztott_esemeny_input=QComboBox(window)
        window.kivalasztott_esemeny_input.setObjectName("feherBg")
        window.kivalasztott_esemeny_input.addItems(jatek["esemenyek"])
        window.mylayout.addWidget(window.kivalasztott_esemeny,2,1,1,1)
        window.mylayout.addWidget(window.kivalasztott_esemeny_input,2,2,1,1)
        
        window.ertek=QLabel("Válassz egy értéket!",window)
        window.ertek.setObjectName("alany")
        window.ertek_input=QLineEdit(window)
        window.ertek_input.setObjectName("feherBg")
        window.ertek_input.setPlaceholderText("érték")
        window.mylayout.addWidget(window.ertek,3,1,1,1)
        window.mylayout.addWidget(window.ertek_input,3,2,1,1)
        
        window.tet=QLabel("Válassz egy tétet!",window)
        window.tet.setObjectName("alany")
        window.tet_input=QLineEdit(window)
        window.tet_input.setObjectName("feherBg")
        window.tet_input.setPlaceholderText("tét")
        window.mylayout.addWidget(window.tet,4,1,1,1)
        window.mylayout.addWidget(window.tet_input,4,2,1,1)
        
        window.errorUzenet=QLabel(window)
        window.mylayout.addWidget(window.errorUzenet,5,1,1,2)
        
        def ErrorÜzenetek():
            valasz = kezelo.benyujtott_fogadas(felhasznalonev,jatek,window.kivalasztott_alany_input,window.kivalasztott_esemeny_input,window.ertek_input,window.tet_input)
            if not valasz == True:
                window.errorUzenet.setText(valasz)
            else:
                window.fogado_oldal(felhasznalonev)
        
        window.fogadasGomb=QPushButton("Fogadás leadása!",window)
        window.fogadasGomb.clicked.connect(ErrorÜzenetek)
        window.fogadasGomb.setObjectName("MentesGomb")
        window.mylayout.addWidget(window.fogadasGomb,6,2,1,1)
        
        window.Vissza=QPushButton("Vissza a fogadásokhoz",window)
        window.Vissza.setObjectName("vissza")
        window.Vissza.clicked.connect(lambda: window.fogado_oldal(felhasznalonev))
        window.mylayout.addWidget(window.Vissza,6,1,1,1)
def fogado_oldal(window,felhasznalonev:str):
    window.layoutvisszaallitasa()
    window.mindig_latszik_belepve(felhasznalonev)


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
    window.elerheto_jatekok = QLabel("Le nem zárt játékok:",window.osszesJatekTarolo)
    window.elerheto_jatekok.setObjectName("elerheto")
    window.osszesJatek.addWidget(window.elerheto_jatekok)

    for jatek in kezelo.le_van_e_zarva_osszes_jatekot_vissza_adja():
        
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
        window.fogadasGomb = QPushButton('Fogadás', window.osszesJatekTarolo)
        window.fogadasGomb.setProperty("jatek",jatek["jatek_neve"])
        window.fogadasGomb.clicked.connect(lambda: window.fogadas_leadasa(felhasznalonev))
        window.fogadasGomb.setObjectName("fogadasGomb")
        window.osszesJatek.addWidget(window.jatek_neve)
        window.osszesJatek.addWidget(window.fogadasGomb)

    window.Vissza = QPushButton('Vissza a szerepválasztáshoz', window)
    window.Vissza.setObjectName("vissza")
    window.Vissza.clicked.connect(lambda: window.bejelentkezett_oldal(felhasznalonev))
    window.mylayout.addWidget(window.Vissza,3,1,1,1)