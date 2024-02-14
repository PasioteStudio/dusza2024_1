import sys
import kezelo
import hashlib
from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout,QHBoxLayout,QGridLayout,QMainWindow

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
        
def passwordHidden(input,initialPlaceholder):
    
    streak=0
    if input.placeholderText() == initialPlaceholder:
        input.setPlaceholderText("")
    if not input.property("canToggle"):
        input.setPlaceholderText(input.text())
        return
    if len(input.text()) == 0:
            input.setPlaceholderText(initialPlaceholder)
    else:
        text=input.text()
        placeholder=input.placeholderText()
        changed=""
        for id,char in enumerate(text):
            if len(text)<len(placeholder):
                willbe_placeholder=""
                for idx,i in enumerate(placeholder):
                    if not idx == input.cursorPosition():
                        willbe_placeholder+=i
                changed=willbe_placeholder
            else:
                if char == "*":
                    if id-streak < len(placeholder) and id-streak > -1:#user put * in password
                        changed+=placeholder[id-streak]
                else:
                    streak=1
                    changed+=char
        input.setPlaceholderText(changed)
        input.setText(replaceTextWithStars(input.placeholderText()))

def togglePassword(input,currentButton,initialPlaceholder):
    currentmode = currentButton.property("toggle")
    if currentmode == "😄":
        currentButton.setProperty("toggle","😃")
        input.setProperty("canToggle",False)
        #Látni akarja
    elif currentmode == "😃":
        currentButton.setProperty("toggle","😄")
        input.setProperty("canToggle",True)
        #Elrejteni
    currentButton.setText(currentmode)
    placeholder=input.placeholderText()
    input.setText(placeholder)
    passwordHidden(input,initialPlaceholder)
        
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
def replaceTextWithStars(text):
    return "*"*len(text)
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
        self.resetLayout()
        # CreateGomb létrehozása
        self.loginButton = QPushButton('Bejelentkezés', self)
        self.loginButton.clicked.connect(self.on_login_button_clicked)

        self.registerButton = QPushButton('Regisztráció', self)
        self.registerButton.clicked.connect(self.on_register_button_clicked)
        
        self.lekerdezesButton = QPushButton('Lekérdezések', self)
        self.lekerdezesButton.clicked.connect(self.lekerdezes)

        self.greet = QLabel('Üdvözöllek a fogadós játékba!', self)
        self.greet.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.greet.setObjectName("greet")
        
        self.setStyleSheet(self.main1+
            """
            #greet{
                font-size:100px;
            }
            """
        )
        
        self.mylayout.addWidget(self.greet,0,0,1,3,QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mylayout.addWidget(self.loginButton,1,0,1,1)
        self.mylayout.addWidget(self.registerButton,1,1,1,1)
        self.mylayout.addWidget(self.lekerdezesButton,1,2,1,1)
    def lekerdezes(self):
        print()
    def on_register_button_clicked(self):
        self.resetLayout()
        self.username = QLabel("Add meg a felhasználóneved!", self)
        self.input_username = QLineEdit(self)
        self.input_username.setPlaceholderText("Felhasználó neved")
        
        self.password = QLabel("Add meg a jelszavad!", self)
        self.input_password = QLineEdit(self)
        
        
        self.input_password.textEdited.connect(lambda: passwordHidden(self.input_password,"Jelszavad"))
        self.input_password.setPlaceholderText("Jelszavad")
        self.input_password.setProperty("canToggle",True)
        self.input_password_toggle = QPushButton('😃', self)
        
        self.input_password_toggle.setProperty("toggle","😄")
        
        self.input_password_toggle.clicked.connect(lambda: togglePassword(self.input_password,self.input_password_toggle,"Jelszavad"))
        

        self.confirm_password = QLabel("Add meg újra a jelszavad!", self)
        self.input_confirm_password = QLineEdit(self)
        self.input_confirm_password.textChanged.connect(lambda: passwordHidden(self.input_confirm_password,"Jelszavad újra"))
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
        
        self.mylayout.addWidget(self.username,0,0,1,1)
        self.mylayout.addWidget(self.input_username,0,1,1,2)
        self.mylayout.addWidget(self.password,1,0,1,1)
        self.mylayout.addWidget(self.input_password,1,1,1,2)
        self.mylayout.addWidget(self.input_password_toggle,1,2,1,1)
        self.mylayout.addWidget(self.confirm_password,2,0,1,1)
        self.mylayout.addWidget(self.input_confirm_password,2,1,1,2)
        self.mylayout.addWidget(self.registerButton,3,1,1,2)
        self.mylayout.addWidget(self.back,3,0,1,1)
    
    def on_login_button_clicked(self):
        self.resetLayout()
            
        # Bemeneti mező létrehozása
        self.username = QLabel("Add meg a felhasználóneved!", self)
        self.input_username = QLineEdit(self)
        self.input_username.setPlaceholderText("Felhasználó neved")
        
        
        
        self.password = QLabel("Add meg a jelszavad!", self)
        self.input_password = QLineEdit(self)
        self.input_password.setPlaceholderText("Jelszavad")
        
        self.input_password.textEdited.connect(lambda: passwordHidden(self.input_password,"Jelszavad"))
        self.input_password.setProperty("canToggle",True)
        self.input_password.setFixedWidth(1000)
        
        self.input_password_toggle = QPushButton('😃', self)
        
        self.input_password_toggle.setProperty("toggle","😄")
        self.input_password_toggle.setMaximumWidth(100)
        
        self.input_password_toggle.clicked.connect(lambda: togglePassword(self.input_password,self.input_password_toggle,"Jelszavad"))
        
        
        self.loginButton = QPushButton('Bejelentkezés', self)
        self.loginButton.clicked.connect(self.on_login_clicked)
        
        self.back = QPushButton('Vissza', self)
        self.back.clicked.connect(self.main)
        
        self.resizeLogin=True
        
        #self.showMinimized() 
        #self.showNormal() 
        #self.showMaximized() 
        
        self.mylayout.addWidget(self.username,0,0,1,1)
        self.mylayout.addWidget(self.input_username,0,1,1,2)
        self.mylayout.addWidget(self.password,1,0,1,1)
        self.mylayout.addWidget(self.input_password,1,1,1,2)
        self.mylayout.addWidget(self.input_password_toggle,1,2,1,1)
        self.mylayout.addWidget(self.loginButton,2,1,1,2)
        self.mylayout.addWidget(self.back,2,0,1,1)
        
    def on_login_clicked(self):
        username = self.input_username.text()
        print("Felh:", username)
        if self.input_password.text().find("*") == -1:
            password = hashPassword(self.input_password.text())
        else:
            password = hashPassword(self.input_password.placeholderText())
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
        self.resizeLogin=False
        for i in reversed(range(self.mylayout.count())): 
            self.mylayout.itemAt(i).widget().deleteLater()
    def always_visible_loggedin(self, username, name):
        point=kezelo.dinamikusPontSzamolás(username)
        self.point = QLabel(f"Pontod: {point}\nFelhasználó Neved: {username}\nMegjelenített Neved: {name}", self)
        #self.username = QLabel(f"Felhasználó Neved: {username}", self)
        #self.name = QLabel(f"Megjelenített Neved: {name}", self)
        
        #self.mylayout.addWidget(self.username)
        #self.mylayout.addWidget(self.name)
        self.mylayout.addWidget(self.point,0,0,1,1)
    def fogado_page(self,username,name):
        self.resetLayout()
        self.always_visible_loggedin(username,name)
        
        self.games_in_playing = QLabel("Le nem zárt játékok:", self)
        self.games_in_playing.setStyleSheet("color:black")
        self.games_in_playing.setMaximumHeight(100)
        
        self.mylayout.addWidget(self.games_in_playing,1,0,1,2)
        jatekok=kezelo.le_van_e_zarva_osszes_jatekot_vissza_adja()
        for id,i in enumerate(jatekok):
            print("asdsa"+str(i))
            
            substring1=[", "]*len(i["alanyok"])
            substring2=[", "]*len(i["esemenyek"])
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
            self.jatek_neve = QLabel(f"{i['jatek_neve']}\nAlanyok:{alanyok}\nEsemények:{esemenyek}", self)
            self.fogadas_button = QPushButton('Fogadás', self)
            self.fogadas_button.clicked.connect(lambda: self.fogadas(i))
            row=id%2
            column=int(id/2)
            if id/2!=round(id/2):
                column=int(round(id/2)-1)
            print(row)
            print(column)
            self.mylayout.addWidget(self.jatek_neve,2+row,0+column,1,1)
            self.mylayout.addWidget(self.fogadas_button,3+row,0+column,1,1)
        
        
        back = QPushButton('Vissza', self)
        back.clicked.connect(lambda: self.login_page(username,name))
        self.mylayout.addWidget(back)
    def szervezo_page(self,username,name):
        self.resetLayout()
        self.always_visible_loggedin(username,name)
        
        self.create_game = QPushButton('Játék létrehozása', self)
        self.create_game.clicked.connect(self.main)#TODO
        self.mylayout.addWidget(self.create_game,1,0,1,1)
        
        
        self.games_in_playing = QLabel("Le nem zárt játékaid:", self)
        self.games_in_playing.setStyleSheet("color:red")
        
        
        self.mylayout.addWidget(self.games_in_playing,2,0,1,1)
        for i in map(lambda x: isUsersGame(x,username=username), kezelo.le_van_e_zarva_osszes_jatekot_vissza_adja()):
            if i == None:
                continue
            self.jatek_neve = QLabel(f"{i['jatek_neve']}\n{i['alanyok']}\n{(i['esemenyek'])}\n", self)
            self.lezaras_button = QPushButton('Játék lezárása', self)
            self.lezaras_button.clicked.connect(lambda: self.lezaras(i,username,name))
            self.mylayout.addWidget(self.jatek_neve)
            self.mylayout.addWidget(self.lezaras_button)
        print("asdasdsd")
        #for i in map(isUsersGame,kezelo.le_van_e_zarva_osszes_jatekot_vissza_adja())
        
        back = QPushButton('Vissza', self)
        back.clicked.connect(lambda: self.login_page(username,name))
        self.mylayout.addWidget(back)
    def eredmeny(self,jatek,username,name):
        eredmenyek = []
        for message in self.alanyok_es_esemyenek_messages:
            print(message.property("esemeny"))
            print(message.property("alany"))
            print(message.text())
            eredmenyek.append({
            "alany":message.property("alany"),
            "esemeny":message.property("esemeny"),
            "eredmeny":message.text()
            })
        eredmeny_txt_be={
            "jatek_nev":jatek["jatek_neve"],
            "eredmenyek":eredmenyek
        }
        file=open("eredmenyek.txt","a",encoding="utf8")
        file.write(eredmeny_txt_be["jatek_nev"]+"\n")
        szorzo=0
        for eredmeny in eredmeny_txt_be["eredmenyek"]:
            file.write(f"{eredmeny['alany']};{eredmeny['esemeny']};{eredmeny['eredmeny']};{szorzo}\n")
        file.close()
        kezelo.szorzo_frissitese(jatek["jatek_neve"])
        self.message= QLabel(f"{jatek['jatek_neve']} lezárva!",self)
        self.mylayout.addWidget(self.message)
        self.szervezo_page(username,name)
    def jatek_letrehozasa_clicked(self):
        if(kezelo.egyedi_jatek_nev(self.megnevezes.text())):
            return
    def jatek_letrehozasa(self):
        self.szervezo = QLabel("Ki a szervező? ",self)
        self.szervezo_input = QLineEdit(self)
        self.szervezo_input.setPlaceholderText("szervező")
        
        self.megnevezes = QLineEdit(self)
        self.megnevezes.setPlaceholderText("Mi a játék megnevezése? (egyedinek kell lennie) ")
        self.alanyok = []
        self.esemenyek = []
        self.alanyok_label = QLabel("Kik az alanyok? (különböznek egymástól)",self)
        #TODO:
        self.def_alanyok_szama=2
        self.def_esemenyek_szama=2
        def plusAlanyokésEsemenyek(plusz_alany,plusz_esemeny):
            if plusz_alany == 1:
                self.new_alany= QLineEdit(self)
                self.new_alany.setPlaceholderText(f"alany")
                self.alanyok.append(self.new_alany)
            if plusz_esemeny == 1:
                self.new_esemeny= QLineEdit(self)
                self.new_esemeny.setPlaceholderText(f"alany")
                self.esemenyek.append(self.new_esemeny)
            current
        self.alanyok_plus=QPushButton("+",self)
        self.alanyok_plus.clicked.connect(lambda: plusAlanyokésEsemenyek(1,0))
        while True:
            input3 = input("Kik az alanyok? (különböznek egymástól) ")
            if(input3 in self.alanyok):
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
    def lezaras(self,jatek,username,name):
        self.resetLayout()
        self.always_visible_loggedin(username,name)
        self.alanyok_es_esemyenek_messages=[]
        for alany in jatek['alanyok']:
            for esemeny in jatek['esemenyek']: 
                print("sdsd")   
                self.message= QLineEdit(self)
                self.message.setPlaceholderText(f"{alany} és {esemeny}")
                print(alany)
                self.message.setProperty("alany",alany)
                self.message.setProperty("esemeny",esemeny)
                self.alanyok_es_esemyenek_messages.append(self.message)
                print(self.message.property("alany"))
                self.mylayout.addWidget(self.message)
                
        self.keszButton=QPushButton("Kész",self)
        self.keszButton.clicked.connect(lambda: self.eredmeny(jatek,username,name))
        self.mylayout.addWidget(self.keszButton)
        self.back = QPushButton("Vissza",self)
        self.back.clicked.connect(lambda: self.szervezo_page(username,name))
        self.mylayout.addWidget(self.back)
    def fogadas(self,jatek):
        print(f"{jatek} fogadva!")
    def login_page(self,username,name):
        self.resetLayout()
        self.always_visible_loggedin(username,name)
        
        self.role = QLabel(f"Válaszd ki a szerepköröd!", self)
        self.role.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        self.szervezo = QPushButton('Szervező', self)
        self.szervezo.clicked.connect(lambda: self.szervezo_page(username,name))
        self.szervezo.setObjectName("szervezo")
        
        self.fogado = QPushButton('Fogadó', self)
        self.fogado.clicked.connect(lambda: self.fogado_page(username,name))
        self.fogado.setObjectName("fogado")
        
        self.back = QPushButton('Vissza a menübe', self)
        self.back.clicked.connect(self.main)
        
        
        self.setStyleSheet(self.main1+
        """
        #fogado,#szervezo{
            height:300px;
            background-color:yellow
        }
        """
        )
        self.mylayout.addWidget(self.role,1,0,1,2)
        self.mylayout.addWidget(self.szervezo,2,0,1,1)
        self.mylayout.addWidget(self.fogado,2,1,1,1)
        self.mylayout.addWidget(self.back,3,0,1,2)
    def resizeAWidget(self):
        print(self.resizeLogin)
        if self.resizeLogin:
            self.input_password.setFixedWidth(self.input_username.geometry().width()-self.input_password_toggle.geometry().width())
    def resizeEvent(self, event):
        print("Window has been resized")
        self.resizeAWidget()
        QWidget.resizeEvent(self, event)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # képernyő létrehozása
    window = MyWindow()
    window.show()
    
    
    sys.exit(app.exec_())