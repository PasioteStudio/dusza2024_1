#Sigmakik
import sys
import kezelo
from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import QLabel, QApplication, QWidget,QGridLayout
from ui.koszontes import fo as koszontes
import ui.szervezo as szervezo
import ui.fogado as fogado
import ui.lekerdezes as lekerdezes
import ui.felhasznalo as felhasznalo
class MyWindow(QWidget):
    def __init__(self):
        self.resizeWidgets=[]
        self.profilok=[]
        with open('forrasok/stilusok/gui.css', 'r') as file:
            css = file.read()
        self.foCSS=css
        super().__init__()
        self.initUI()
    def initUI(self):
        # Layout létrehozása
        self.mylayout = QGridLayout(self)  
        self.mylayout.setObjectName("container")
        # Layout hozzáadása a main window-hoz
        self.setLayout(self.mylayout)
        #Köszöntés oldal
        self.main()
        # Képernyő méretei és pozíciója
        xCoord = 100
        yCoord = 100
        winWidht = 300
        winHeight = 150
        self.setGeometry(xCoord, yCoord, winWidht, winHeight)
        # Képernyő címe
        self.setWindowTitle('Fogadás managger 2000')
        icon_path="forrasok/kepek/icon.jpg"
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.showMaximized() 
    def main(self):
        koszontes(self)
    def lekerdezes(self):
        lekerdezes.lekerdezes(self)
    def regisztracios_oldal(self):
        felhasznalo.regisztracios_oldal(self)
    def bejelentkezes_oldal(self):
        felhasznalo.bejelentkezes_oldal(self)
    def szervezo_oldal(self,felhasznalonev):
        szervezo.szervezo_oldal(self,felhasznalonev)
    def fogado_oldal(self,felhasznalonev:str):
        fogado.fogado_oldal(self,felhasznalonev)
    def jatek_letrehozasa(self,felhasznalonev:str):
        szervezo.jatek_letrehozasa(self,felhasznalonev)
    def bejelentkezett_oldal(self,felhasznalonev:str):
        felhasznalo.bejelentkezett_oldal(self,felhasznalonev)
    def fogadas_leadasa(self,felhasznalonev:str):
        fogado.fogadas_leadasa(self,felhasznalonev)
    def lezaras(self,felhasznalonev):
        szervezo.lezaras(self,felhasznalonev)
    def ranglista(self):
        lekerdezes.ranglista(self)
    def jatek_statisztika(self):
        lekerdezes.jatek_statisztika(self)
    def fogadasi_statisztika(self):
        lekerdezes.fogadasi_statisztika(self)
    def profil_beallitasok(self,felhasznalonev:str):
        felhasznalo.profil_beallitasok(self,felhasznalonev)
    def layoutvisszaallitasa(self):
        self.resizeWidgets=[]
        self.setStyleSheet(self.foCSS)
        while self.mylayout.count():
            child = self.mylayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        if len(self.profilok) > 0:
            while self.profilok[0].count():
                child2 = self.profilok[0].takeAt(0)
                if child2.widget():
                    child2.widget().deleteLater()
    def mindig_latszik_belepve(self, felhasznalonev:str):
        nev=kezelo.felhasznalo_neve(felhasznalonev)
        pont=int(kezelo.dinamikusPontSzamolás(felhasznalonev))
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
        
        self.profil=QGridLayout(self)
        self.profil.addWidget(self.kep,1,0,2,1,QtCore.Qt.AlignmentFlag.AlignCenter)
        self.profil.addWidget(self.hatter2,0,0,9,1)
        self.profil.addWidget(self.pont,3,0,1,1,QtCore.Qt.AlignmentFlag.AlignBottom)
        self.profil.addWidget(self.felhasznalonev,4,0,1,1,QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.profil.addWidget(self.nev,5,0,1,1,QtCore.Qt.AlignmentFlag.AlignTop)
        self.profil.addWidget(self.ures,6,0,3,1)
        
        self.profilok = []
        self.profilok.append(self.profil)
        self.mylayout.addLayout(self.profil,0,0,8,1)
        self.hatter2.show()
        self.hatter2.lower()
        return nev
    def resizeEvent(self, event):
        self.mivek=[int(self.frameGeometry().size().width()/2)]
        for element in self.resizeWidgets:
            element["elem"].setFixedWidth(self.mivek[element["mive"]])
        QWidget.resizeEvent(self, event)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # képernyő létrehozása
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())