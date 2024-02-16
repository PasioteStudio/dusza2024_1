import sys
import kezelo

from PyQt5 import QtGui,QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout,QHBoxLayout,QGridLayout,QMainWindow,QScrollArea,QAbstractScrollArea

"""


def fogadas_leadasa():
    fogado_fel = input("Fogadó fél neve: ")
    pont = kezelo.dinamikusPontSzamolás(fogado_fel)
    print(f"Pontod: {pont}")
        
    elerheto_jatekok=kezelo.le_van_e_zarva_osszes_jatekot_vissza_adja()
    print(elerheto_jatekok)
    #TODO: design
    sikeres=False
    print(f"Pontod: {pont}")
    kivalasztott_jatek = input("Válassz egy játékot!: ")
    for jatek in elerheto_jatekok:
        if(kivalasztott_jatek == jatek["jatek_neve"]):
            while True:
                kivalasztott_alany = input("Válassz egy alanyt!: ")
                kivalasztott_esemeny = input("Válassz egy eseményt!: ")
                if(kezelo.fogadott_e_mar(fogado_fel,kivalasztott_jatek,kivalasztott_alany,kivalasztott_esemeny)):
                    print("Már fogadtál erre!")
                    continue
                break
            while True:
                kivalasztott_ertek = input("Válassz egy értéket!: ")
                if ";" in kivalasztott_ertek:
                    continue
                break
            while True:
                kivalasztott_tet = kezelo.NumInput("Válassz egy tétet!: ")
                if(kivalasztott_tet>pont):
                    print("Nincs ennyi pontod, amit feltegyél!")
                    continue
                elif(kivalasztott_tet<0):
                    print("Legalább tegyél fel valamennyit!")
                    continue
                break
            file=open("fogadasok.txt","a",encoding="utf8")
            file.write(f"{fogado_fel};{kivalasztott_jatek};{kivalasztott_tet};{kivalasztott_alany};{kivalasztott_esemeny};{kivalasztott_ertek}\n")
            file.close()
            sikeres=True
            break
    if sikeres:
        print("Sikeresen leadott fogadás!")
    else:
        print("Sikertelen fogadás (talán még/már nincs elérhető játék)!")
    pass
def lekerdezesek():
    while True:  
        print("----------")
        print("1- Ranglista")
        print("2- Játék statisztika")
        print("3- Fogadási statisztika")
        print("4- Vissza")
        user_input = kezelo.NumInput("Válassz: ")
        if(user_input > 4 or user_input<1):
            continue
        elif(user_input == 1):
            kezelo.ranglista()
            continue
        elif(user_input == 2):
            kezelo.jatek_statisztika()
            continue
        elif(user_input == 3):
            while True:
                jatek_nev=input("Kiválasztott játék: ")
                if(jatek_nev == ""):
                    break
                if(not kezelo.egyedi_jatek_nev(jatek_nev)):   
                    kezelo.fogadasi_statisztika(jatek_nev)
                    break
                else:
                    continue
        elif(user_input == 4):
            break

"""
        


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # self.setStyleSheet("background-color: red;") 
        

        # Layout létrehozása
        self.mylayout = QGridLayout(self)  
        self.mylayout.setObjectName("container")
        self.main1= """
            * {
                border:10px solid black;
                background-color: red;
                font-size:30px;
                
            }
        """
        # Layout hozzáadása a main window-hoz
        self.setLayout(self.mylayout)
        self.setStyleSheet(self.main1)
        print(self.styleSheet())
        #self.window().setStyleSheet(main)
        
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
        
        self.setStyleSheet(self.main1+
            """
            #greet{
                font-size:100px;
            }
            """
        )
        
        self.mylayout.addWidget(self.koszontes,0,0,1,3,QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mylayout.addWidget(self.bejelentkezesGomb,1,0,1,1)
        self.mylayout.addWidget(self.regisztraciosGomb,1,1,1,1)
        self.mylayout.addWidget(self.lekerdezesGomb,1,2,1,1)
    def lekerdezes(self):
        print()
    def regisztracios_oldal(self):
        self.layoutvisszaallitasa()
        self.felhasznalonev = QLabel("Add meg a felhasználóneved!", self)
        self.input_felhasznalonev = QLineEdit(self)
        self.input_felhasznalonev.setPlaceholderText("Felhasználó neved")
        
        self.jelszo = QLabel("Add meg a jelszavad!", self)
        self.input_jelszo = QLineEdit(self)
        self.input_jelszo.textEdited.connect(lambda: kezelo.jelszo_rejtese(self.input_jelszo,"Jelszavad"))
        self.input_jelszo.setPlaceholderText("Jelszavad")
        self.input_jelszo.setProperty("canToggle",True)
        self.input_jelszo_megjelenitese = QPushButton('😃', self)
        self.input_jelszo_megjelenitese.setProperty("toggle","😄")
        self.input_jelszo_megjelenitese.clicked.connect(lambda: kezelo.jelszo_megjelenitese(self.input_jelszo,self.input_jelszo_megjelenitese,"Jelszavad"))
        
        self.megerosito_jelszo = QLabel("Add meg újra a jelszavad!", self)
        self.input_megerosito_jelszo = QLineEdit(self)
        self.input_megerosito_jelszo.textChanged.connect(lambda: kezelo.jelszo_rejtese(self.input_megerosito_jelszo,"Jelszavad újra"))
        self.input_megerosito_jelszo.setPlaceholderText("Jelszavad újra")
        
        self.regisztraciosGomb = QPushButton('Regisztráció', self)
        self.regisztraciosGomb.clicked.connect(lambda: kezelo.benyujtott_regisztracio(self.input_felhasznalonev,self.input_jelszo,self.input_megerosito_jelszo))
        self.Vissza = QPushButton('Vissza', self)
        self.Vissza.clicked.connect(self.main)
        
        self.mylayout.addWidget(self.felhasznalonev,0,0,1,1)
        self.mylayout.addWidget(self.input_felhasznalonev,0,1,1,2)
        self.mylayout.addWidget(self.jelszo,1,0,1,1)
        self.mylayout.addWidget(self.input_jelszo,1,1,1,2)
        self.mylayout.addWidget(self.input_jelszo_megjelenitese,1,2,1,1)
        self.mylayout.addWidget(self.megerosito_jelszo,2,0,1,1)
        self.mylayout.addWidget(self.input_megerosito_jelszo,2,1,1,2)
        self.mylayout.addWidget(self.regisztraciosGomb,3,1,1,2)
        self.mylayout.addWidget(self.Vissza,3,0,1,1)
    def bejelentkezes_oldal(self):
        self.layoutvisszaallitasa()
            
        # Bemeneti mező létrehozása
        self.felhasznalonev = QLabel("Add meg a felhasználóneved!", self)
        self.input_felhasznalonev = QLineEdit(self)
        self.input_felhasznalonev.setPlaceholderText("Felhasználó neved")
        
        self.jelszo = QLabel("Add meg a jelszavad!", self)
        self.input_jelszo = QLineEdit(self)
        self.input_jelszo.setPlaceholderText("Jelszavad")
        self.input_jelszo.textEdited.connect(lambda: kezelo.jelszo_rejtese(self.input_jelszo,"Jelszavad"))
        self.input_jelszo.setProperty("canToggle",True)
        self.input_jelszo.setFixedWidth(1000)
        self.input_jelszo_megjelenitese = QPushButton('😃', self)
        self.input_jelszo_megjelenitese.setProperty("toggle","😄")
        self.input_jelszo_megjelenitese.setMaximumWidth(100)
        self.input_jelszo_megjelenitese.clicked.connect(lambda: kezelo.jelszo_megjelenitese(self.input_jelszo,self.input_jelszo_megjelenitese,"Jelszavad"))
        
        self.bejelentkezesGomb = QPushButton('Bejelentkezés', self)
        def kurvaAnyadCircularImport():
            felhasznalonev,nev=kezelo.benyujtott_bejelentkezes(self.input_felhasznalonev,self.input_jelszo)
            self.bejelentkezett_oldal(felhasznalonev,nev)
        self.bejelentkezesGomb.clicked.connect(kurvaAnyadCircularImport)
        self.Vissza = QPushButton('Vissza', self)
        self.Vissza.clicked.connect(self.main)
        
        self.mylayout.addWidget(self.felhasznalonev,0,0,1,1)
        self.mylayout.addWidget(self.input_felhasznalonev,0,1,1,2)
        self.mylayout.addWidget(self.jelszo,1,0,1,1)
        self.mylayout.addWidget(self.input_jelszo,1,1,1,2)
        self.mylayout.addWidget(self.input_jelszo_megjelenitese,1,2,1,1)
        self.mylayout.addWidget(self.bejelentkezesGomb,2,1,1,2)
        self.mylayout.addWidget(self.Vissza,2,0,1,1)
    def layoutvisszaallitasa(self):
        self.resizeLogin=False
        for i in reversed(range(self.mylayout.count())): 
            self.mylayout.itemAt(i).widget().deleteLater()
    def mindig_latszik_belepve(self, felhasznalonev:str,nev:str):
        pont=kezelo.dinamikusPontSzamolás(felhasznalonev)
        self.pont = QLabel(f"Pontod: {pont}\nFelhasználó Neved: {felhasznalonev}\nMegjelenített Neved: {nev}", self)
        self.mylayout.addWidget(self.pont,0,0,1,1)
    def fogado_oldal(self,felhasznalonev:str,nev:str):
        self.layoutvisszaallitasa()
        self.mindig_latszik_belepve(felhasznalonev,nev)
        
        self.elerheto_jatekok = QLabel("Le nem zárt játékok:", self)
        self.elerheto_jatekok.setStyleSheet("color:black")
        self.elerheto_jatekok.setMaximumHeight(100)
        
        self.mylayout.addWidget(self.elerheto_jatekok,1,0,1,2)
        jatekok=kezelo.le_van_e_zarva_osszes_jatekot_vissza_adja()
        for id,jatek in enumerate(jatekok):
            print("asdsa"+str(jatek))
            
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
            alanyok="".join(map(str,map(lambda x,y: orulet(x,y,0),i["alanyok"],substrings[0])))
            esemenyek="".join(map(str,map(lambda x,y: orulet(x,y,1),i["esemenyek"],substrings[1])))
            #Hozzáadom az alanyokhoz az egyes alanyt és egy vesszőt, az utolsó elemnél a vesszőt mindig elhagyom és ezt megcsinálom az eseményekkel is
            self.jatek_neve = QLabel(f"{jatek['jatek_neve']}\nAlanyok:{alanyok}\nEsemények:{esemenyek}", self)
            self.fogadasGomb = QPushButton('Fogadás', self)
            self.fogadasGomb.clicked.connect(lambda: self.fogadas(jatek))
            row=id%2
            column=int(id/2)
            if id/2!=round(id/2):
                column=int(round(id/2)-1)
            print(row)
            print(column)
            self.mylayout.addWidget(self.jatek_neve,2+row,0+column,1,1)
            self.mylayout.addWidget(self.fogadasGomb,3+row,0+column,1,1)
        
        
        self.Vissza = QPushButton('Vissza', self)
        self.Vissza.clicked.connect(lambda: self.bejelentkezett_oldal(felhasznalonev,nev))
        self.mylayout.addWidget(self.Vissza)
    def szervezo_oldal(self,felhasznalonev:str,nev:str):
        self.layoutvisszaallitasa()
        self.mindig_latszik_belepve(felhasznalonev,nev)
        
        self.jatek_letrehozas = QPushButton('Játék létrehozása', self)
        self.jatek_letrehozas.clicked.connect(lambda: self.jatek_letrehozasa(felhasznalonev,nev))
        self.mylayout.addWidget(self.jatek_letrehozas,1,0,1,1)
        
        
        self.elerheto_jatekok = QLabel("Le nem zárt játékaid:", self)
        self.elerheto_jatekok.setStyleSheet("color:red")
        
        
        self.mylayout.addWidget(self.elerheto_jatekok,2,0,1,1)
        for jatek in map(lambda x: kezelo.jatekot_felhasznalo_szervezte(x,felhasznalonev), kezelo.le_van_e_zarva_osszes_jatekot_vissza_adja()):
            if jatek == None:
                continue
            self.jatek_neve = QLabel(f"{jatek['jatek_neve']}\n{jatek['alanyok']}\n{(jatek['esemenyek'])}\n", self)
            self.lezarasGomb = QPushButton('Játék lezárása', self)
            self.lezarasGomb.clicked.connect(lambda: self.lezaras(jatek,felhasznalonev,nev))
            self.mylayout.addWidget(self.jatek_neve)
            self.mylayout.addWidget(self.lezarasGomb)
        print("asdasdsd")
        #for i in map(isUsersGame,kezelo.le_van_e_zarva_osszes_jatekot_vissza_adja())
        
        self.Vissza = QPushButton('Vissza', self)
        self.Vissza.clicked.connect(lambda: self.bejelentkezett_oldal(felhasznalonev,nev))
        self.mylayout.addWidget(self.Vissza)
    def jatek_letrehozasa_clicked(self):
        if(kezelo.egyedi_jatek_nev(self.megnevezes.text())):
            return
    def jatek_letrehozasa(self,felhasznalonev:str,nev:str):
        self.layoutvisszaallitasa()
        self.mindig_latszik_belepve(felhasznalonev,nev)
        
        self.szervezo = QLabel("Ki a szervező? ",self)
        self.szervezo_input = QLineEdit(self)
        self.szervezo_input.setPlaceholderText("szervező")
        self.mylayout.addWidget(self.szervezo,1,0,1,1)
        self.mylayout.addWidget(self.szervezo_input,1,1,1,1)
        
        self.megnevezes = QLineEdit(self)
        
        self.megnevezes.setPlaceholderText("Mi a játék megnevezése? (egyedinek kell lennie) ")
        self.alanyok_label = QLabel("Kik az alanyok? (különböznek egymástól)",self)
        self.esemenyek_label = QLabel("Mik az események? (különböznek egymástól)",self)
        self.mylayout.addWidget(self.megnevezes,2,0,1,1)
        #TODO:
        alap_alanyok_szama=2
        alap_esemenyek_szama=2
        self.osszesAlanyTarolo=QScrollArea(self)
        self.osszesAlanyTarolo.setWidgetResizable(True)
        self.osszesAlanyTarolo.setFixedHeight(200)
        self.osszesAlanyTarolo.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.osszesAlanyTarolo.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.osszesEsemenyTarolo=QScrollArea(self)
        self.osszesEsemenyTarolo.setWidgetResizable(True)
        self.osszesEsemenyTarolo.setFixedHeight(200)
        self.osszesEsemenyTarolo.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.osszesEsemenyTarolo.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.osszesAlany=QGridLayout(self.osszesAlanyTarolo)
        self.osszesEsemeny = QGridLayout(self.osszesEsemenyTarolo)

        self.alanyok_plusz=QPushButton("+",self)
        self.esemenyek_plusz=QPushButton("+",self)
        self.alanyok_plusz.clicked.connect(lambda: kezelo.plusAlanyokésEsemenyek(1,0,self.osszesAlany,self.osszesEsemeny,self.osszesAlanyTarolo,self.osszesEsemenyTarolo))
        self.esemenyek_plusz.clicked.connect(lambda: kezelo.plusAlanyokésEsemenyek(0,1,self.osszesAlany,self.osszesEsemeny,self.osszesAlanyTarolo,self.osszesEsemenyTarolo))
        self.mylayout.addWidget(self.alanyok_label,3,0,1,1)
        self.mylayout.addWidget(self.alanyok_plusz,3,1,1,1)
        self.mylayout.addWidget(self.osszesAlanyTarolo,4,0,1,1)
        kezelo.plusAlanyokésEsemenyek(alap_alanyok_szama,0,self.osszesAlany,self.osszesEsemeny,self.osszesAlanyTarolo,self.osszesEsemenyTarolo)
        self.mylayout.addWidget(self.esemenyek_label,5,0,1,1)
        self.mylayout.addWidget(self.esemenyek_plusz,5,1,1,1)
        self.mylayout.addWidget(self.osszesEsemenyTarolo,6,0,1,1)
        kezelo.plusAlanyokésEsemenyek(0,alap_esemenyek_szama,self.osszesAlany,self.osszesEsemeny,self.osszesAlanyTarolo,self.osszesEsemenyTarolo)
        
        self.keszGomb=QPushButton("Kész",self)
        self.keszGomb.clicked.connect(lambda: self.jatek_letrehozasa_clicked())
        self.mylayout.addWidget(self.keszGomb,7,0,1,1)
        self.Vissza=QPushButton("Vissza",self)
        self.Vissza.clicked.connect(lambda: self.szervezo_oldal(felhasznalonev,nev))
        self.mylayout.addWidget(self.Vissza,7,1,1,1)
        """
        
        while True:
            input3 = input("Kik az alanyok? (különböznek egymástól) ")
            if(input3 in self.osszesAlany.children()):
                print("Ő már volt!")
                continue
            if(input3 == ""):
                break
            self.alanyok.append(input3)
        esemenyek = []
        while True:
            input4 = input("Mik az események? ")
            if(input4 == ""):
                break
            esemenyek.append(input4)
        file=open("jatekok.txt","a",encoding="utf8")
        file.write(f"{self.szervezo};{self.megnevezes};{len(self.alanyok)};{len(esemenyek)}\n")
        for alany in self.alanyok:
            file.write(f"{alany}\n")
        for esemeny in esemenyek:
            file.write(f"{esemeny}\n")
        file.close()
        
        """
    def lezaras(self,jatek,felhasznalonev,nev):
        self.layoutvisszaallitasa()
        self.mindig_latszik_belepve(felhasznalonev,nev)
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
        def KurvaAnyadCircularImport():
            kezelo.benyujtott_eredmeny(jatek,self.alanyok_es_esemyenek_uzenetek)
            self.uzenet= QLabel(f"{jatek['jatek_neve']} lezárva!",self)
            self.mylayout.addWidget(self.uzenet)
            self.szervezo_oldal(felhasznalonev,nev)
        self.keszGomb.clicked.connect(KurvaAnyadCircularImport)

        self.mylayout.addWidget(self.keszGomb)
        self.Vissza = QPushButton("Vissza",self)
        self.Vissza.clicked.connect(lambda: self.szervezo_oldal(felhasznalonev,nev))
        self.mylayout.addWidget(self.Vissza)
    def fogadas(self,jatek):
        print(f"{jatek} fogadva!")
    def bejelentkezett_oldal(self,felhasznalonev:str,nev:str):
        self.layoutvisszaallitasa()
        self.mindig_latszik_belepve(felhasznalonev,nev)
        
        self.szerepkor = QLabel(f"Válaszd ki a szerepköröd!", self)
        self.szerepkor.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        self.szervezo = QPushButton('Szervező', self)
        self.szervezo.clicked.connect(lambda: self.szervezo_oldal(felhasznalonev,nev))
        self.szervezo.setObjectName("szervezo")
        
        self.fogado = QPushButton('Fogadó', self)
        self.fogado.clicked.connect(lambda: self.fogado_oldal(felhasznalonev,nev))
        self.fogado.setObjectName("fogado")
        
        self.Vissza = QPushButton('Vissza a menübe', self)
        self.Vissza.clicked.connect(self.main)
        
        
        self.setStyleSheet(self.main1+
        """
        #fogado,#szervezo{
            height:300px;
            background-color:yellow
        }
        """
        )
        self.mylayout.addWidget(self.szerepkor,1,0,1,2)
        self.mylayout.addWidget(self.szervezo,2,0,1,1)
        self.mylayout.addWidget(self.fogado,2,1,1,1)
        self.mylayout.addWidget(self.Vissza,3,0,1,2)
    def resizeEvent(self, event):
        print("Window has been resized")
        QWidget.resizeEvent(self, event)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # képernyő létrehozása
    window = MyWindow()
    window.show()
    
    
    sys.exit(app.exec_())