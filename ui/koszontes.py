#Sigmakik
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5 import QtCore
def fo(window):
    window.layoutvisszaallitasa()
    # CreateGomb létrehozása
    window.bejelentkezesGomb = QPushButton('Bejelentkezés', window)
    window.bejelentkezesGomb.clicked.connect(window.bejelentkezes_oldal)
    window.bejelentkezesGomb.setObjectName("bejelentkezesGomb")

    window.regisztraciosGomb = QPushButton('Még nincs fiókom', window)
    window.regisztraciosGomb.clicked.connect(window.regisztracios_oldal)
    window.regisztraciosGomb.setObjectName("vissza")
    
    window.lekerdezesGomb = QPushButton('Lekérdezések', window)
    window.lekerdezesGomb.clicked.connect(window.lekerdezes)
    window.lekerdezesGomb.setObjectName("vissza")

    window.koszontes = QLabel('Fogadás managger 2000', window)
    window.koszontes.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    window.koszontes.setObjectName("greet")
    
    window.koszontesOutline = QLabel('Fogadás managger 2000', window)
    window.koszontesOutline.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    window.koszontesOutline.setObjectName("greetOutline")
    
    window.JatekIcon=QLabel(window)
    window.JatekIcon.setObjectName("JatekIcon")
    window.JatekIcon.setFixedHeight(500)
    window.JatekIcon.setFixedWidth(500)
    
    window.setStyleSheet(window.foCSS)
    
    window.mylayout.addWidget(window.JatekIcon,0,0,1,3,QtCore.Qt.AlignmentFlag.AlignCenter)
    window.mylayout.addWidget(window.koszontes,1,0,1,3,QtCore.Qt.AlignmentFlag.AlignCenter)
    window.mylayout.addWidget(window.koszontesOutline,1,0,1,3,QtCore.Qt.AlignmentFlag.AlignCenter)
    window.koszontes.raise_()
    window.mylayout.addWidget(window.bejelentkezesGomb,2,0,1,3,QtCore.Qt.AlignmentFlag.AlignCenter)
    window.mylayout.addWidget(window.regisztraciosGomb,3,1,1,1)
    window.mylayout.addWidget(window.lekerdezesGomb,3,2,1,1)
