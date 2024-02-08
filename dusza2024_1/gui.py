import sys
import kezelo
import hashlib
from colorama import Fore, Back, Style
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout

def hashPassword(password:str)->str:
    # Create a SHA-256 hash object
    hash_object = hashlib.sha256()
    # Convert the password to bytes and hash it
    hash_object.update(password.encode())
    # Get the hex digest of the hash
    hash_password = hash_object.hexdigest()
    return hash_password
def isPasswordValid(password:str,password_hash:str)->bool:
    hash_object = hashlib.sha256()
    hash_object.update(password.encode())
    # Get the hex digest of the hash
    hash_password = hash_object.hexdigest()
    return hash_password == password_hash

def monddHogyHello():
    return 'Üdvözöllek a fogadós játékba!'
def isUsersGame(games,username):
    print(games)
    print(username)
    if games["szervezo"] == username:
        print(games)
        return games
    return None
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # self.setStyleSheet("background-color: red;") 
        

        # Layout létrehozása
        self.mylayout = QVBoxLayout()
        
        
        self.main()

        # Layout hozzáadása a main window-hoz
        self.setLayout(self.mylayout)

        # Képernyő méretei és pozíciója
        #self.mylayout.deleteLater()
        xCoord = 100
        yCoord = 100
        winWidht = 300
        winHeight = 150
        self.setGeometry(xCoord, yCoord, winWidht, winHeight)

        # Képernyő címe
        self.setWindowTitle('A Sorsod Borsod')
    def main(self):
        self.resetLayout()
        # CreateGomb létrehozása
        self.loginButton = QPushButton('Bejelentkezés', self)
        self.loginButton.clicked.connect(self.on_login_button_clicked)

        self.registerButton = QPushButton('Regisztráció', self)
        self.registerButton.clicked.connect(self.on_register_button_clicked)

        self.greet = QLabel(monddHogyHello(), self)

        self.mylayout.addWidget(self.greet)
        self.mylayout.addWidget(self.loginButton)
        self.mylayout.addWidget(self.registerButton)
    def on_register_button_clicked(self):
        self.resetLayout()
        self.username = QLabel("Add meg a felhasználóneved!", self)
        self.input_username = QLineEdit(self)
        self.input_username.setPlaceholderText("Felhasználó neved")
        
        self.password = QLabel("Add meg a jelszavad!", self)
        self.input_password = QLineEdit(self)
        self.input_password.setPlaceholderText("Jelszavad")
        
        self.confirm_password = QLabel("Add meg újra a jelszavad!", self)
        self.input_confirm_password = QLineEdit(self)
        self.input_confirm_password.setPlaceholderText("Jelszavad újra")
        
        def register_submitted():
            username = self.input_username.text()#Egyedi
            file = open("users.txt","r",encoding="utf8")
            lines=file.readlines()
            file.close()
            unique=True
            for line in lines:
                parts=line.strip().split(";")
                if parts[0]==username:
                    unique=False
            if not unique:
                print("A felhasználónév foglalt!")
                return
            password = self.input_password.text()
            if password != self.input_confirm_password.text():
                print("Nem egyezik meg a jelszó!")
                return
            file = open("users.txt","a",encoding="utf8")
            file.write(f"{username};{hashPassword(password)};{username}\n")
            file.close()
        self.registerButton = QPushButton('Regisztráció', self)
        self.registerButton.clicked.connect(register_submitted)
        
        
        self.back = QPushButton('Vissza', self)
        self.back.clicked.connect(self.main)
        
        self.mylayout.addWidget(self.username)
        self.mylayout.addWidget(self.input_username)
        self.mylayout.addWidget(self.password)
        self.mylayout.addWidget(self.input_password)
        self.mylayout.addWidget(self.confirm_password)
        self.mylayout.addWidget(self.input_confirm_password)
        self.mylayout.addWidget(self.registerButton)
        self.mylayout.addWidget(self.back)
    def on_login_button_clicked(self):
        self.resetLayout()
            
        # Bemeneti mező létrehozása
        self.username = QLabel("Add meg a felhasználóneved!", self)
        self.input_username = QLineEdit(self)
        self.input_username.setPlaceholderText("Felhasználó neved")
        
        self.password = QLabel("Add meg a jelszavad!", self)
        self.input_password = QLineEdit(self)
        self.input_password.setPlaceholderText("jelszavad")
        
        self.loginButton = QPushButton('Bejelentkezés', self)
        self.loginButton.clicked.connect(self.on_login_clicked)
        
        self.back = QPushButton('Vissza', self)
        self.back.clicked.connect(self.main)
        self.mylayout.addWidget(self.username)
        self.mylayout.addWidget(self.input_username)
        self.mylayout.addWidget(self.password)
        self.mylayout.addWidget(self.input_password)
        self.mylayout.addWidget(self.loginButton)
        self.mylayout.addWidget(self.back)
        
    def on_login_clicked(self):
        username = self.input_username.text()
        print("Felh:", username)
        password = hashPassword(self.input_password.text())
        print("Jelsz:", password)
        f=open("users.txt","r",encoding="utf8")
        lines=f.readlines()
        f.close()
        talalt=False
        name=""
        for line in lines:
            parts=line.strip().split(";")
            if username == parts[0] and password == parts[1]:
                print("Bejelentkeztél")
                print(kezelo.dinamikusPontSzamolás(username))
                name=parts[2]
                talalt=True
        if not talalt:
            print("Nincs ilyen felhasználónév vagy jelszó!")
        else:
            self.login_page(username,name)
        
    def resetLayout(self):
        for i in reversed(range(self.mylayout.count())): 
            self.mylayout.itemAt(i).widget().deleteLater()
    def always_visible_loggedin(self, username, name):
        point=kezelo.dinamikusPontSzamolás(username)
        self.point = QLabel(f"Pontod: {point}", self)
        self.username = QLabel(f"Felhasználó Neved: {username}", self)
        self.name = QLabel(f"Megjelenített Neved: {name}", self)
        
        self.mylayout.addWidget(self.username)
        self.mylayout.addWidget(self.name)
        self.mylayout.addWidget(self.point)
    def fogado_page(self,username,name):
        self.resetLayout()
        self.always_visible_loggedin(username,name)
        
        self.games_in_playing = QLabel("Le nem zárt játékok:", self)
        self.games_in_playing.setStyleSheet("color:red")
        
        self.mylayout.addWidget(self.games_in_playing)
        for i in kezelo.le_van_e_zarva_osszes_jatekot_vissza_adja():
            self.jatek_neve = QLabel(i['jatek_neve'], self)
            self.alanyok = QLabel(str(i['alanyok']), self)
            self.esemenyek = QLabel(str(i['esemenyek']), self)
            self.fogadas_button = QPushButton('Fogadás', self)
            self.fogadas_button.clicked.connect(lambda: self.fogadas(i))
            self.mylayout.addWidget(self.jatek_neve)
            self.mylayout.addWidget(self.alanyok)
            self.mylayout.addWidget(self.esemenyek)
            self.mylayout.addWidget(self.fogadas_button)
        print("asdasdsd")
        
        back = QPushButton('Vissza', self)
        back.clicked.connect(lambda: self.login_page(username,name))
        self.mylayout.addWidget(back)
    def szervezo_page(self,username,name):
        self.resetLayout()
        self.always_visible_loggedin(username,name)
        
        self.create_game = QPushButton('Játék létrehozása', self)
        self.create_game.clicked.connect(self.main)
        self.mylayout.addWidget(self.create_game)
        
        self.games_in_playing = QLabel("Le nem zárt játékok:", self)
        self.games_in_playing.setStyleSheet("color:red")
        
        
        self.mylayout.addWidget(self.games_in_playing)
        for i in map(lambda x: isUsersGame(x,username=username), kezelo.le_van_e_zarva_osszes_jatekot_vissza_adja()):
            if i == None:
                continue
            self.jatek_neve = QLabel(i['jatek_neve'], self)
            self.alanyok = QLabel(str(i['alanyok']), self)
            self.esemenyek = QLabel(str(i['esemenyek']), self)
            self.lezaras_button = QPushButton('Játék lezárása', self)
            self.lezaras_button.clicked.connect(lambda: self.lezaras(i))
            self.mylayout.addWidget(self.jatek_neve)
            self.mylayout.addWidget(self.alanyok)
            self.mylayout.addWidget(self.esemenyek)
            self.mylayout.addWidget(self.lezaras_button)
        print("asdasdsd")
        #for i in map(isUsersGame,kezelo.le_van_e_zarva_osszes_jatekot_vissza_adja())
        
        back = QPushButton('Vissza', self)
        back.clicked.connect(lambda: self.login_page(username,name))
        self.mylayout.addWidget(back)
    def lezaras(self,jatek):
        print(f"{jatek} lezárva!")
    def fogadas(self,jatek):
        print(f"{jatek} fogadva!")
    def login_page(self,username,name):
        self.resetLayout()
        self.always_visible_loggedin(username,name)
        
        self.role = QLabel(f"Válaszd ki a szerepköröd!", self)
        
        self.szervezo = QPushButton('Szervező', self)
        self.szervezo.clicked.connect(lambda: self.szervezo_page(username,name))
        
        self.fogado = QPushButton('Fogadó', self)
        self.fogado.clicked.connect(lambda: self.fogado_page(username,name))
        
        self.back = QPushButton('Vissza a menübe', self)
        self.back.clicked.connect(self.main)
        
        self.mylayout.addWidget(self.role)
        self.mylayout.addWidget(self.szervezo)
        self.mylayout.addWidget(self.fogado)
        self.mylayout.addWidget(self.back)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # képernyő létrehozása
    window = MyWindow()
    window.show()
    
    sys.exit(app.exec_())