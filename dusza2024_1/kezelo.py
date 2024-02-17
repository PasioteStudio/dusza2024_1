#Sigmakik
import hashlib
from PyQt5.QtWidgets import QLineEdit,QGridLayout,QWidget,QGroupBox,QComboBox,QLabel,QVBoxLayout,QScrollArea
def szorzo_frissitese(jatek_neve:str):
    fajl=open("fogadasok.txt","r",encoding="utf8")
    sorok=fajl.readlines()
    fajl.close()
    fogadasok={}
    for sor in sorok:
        reszek=sor.strip().split(";")
        if(reszek[1]==jatek_neve):
            fogadasok[reszek[3]+reszek[4]]=0
    for sor in sorok:
        reszek=sor.strip().split(";")
        if(reszek[1]==jatek_neve):
            fogadasok[reszek[3]+reszek[4]]+=1
    #Ki olvastuk a fogadasok.txt fájlból, hogy mennyi fogadás van egy-egy alany és eseményen az adott játékban

    
    fajl2=open("eredmenyek.txt","r",encoding="utf8")
    sorok2=fajl2.readlines()
    fajl2.close()
    talalt=False
    #Végigmegyünk az eredmenyek.txt fájlon, hogy a szorzó képletével végigszámolva beírjuk azt
    for id,sor2 in enumerate(sorok2):
        reszek2=sor2.strip().split(";")
        if(talalt):
            if reszek2[0]+reszek2[1] in fogadasok.keys():
                k=fogadasok[reszek2[0]+reszek2[1]]
                szorzo= round(1 + (5/(2 ** k - 1)),2)
            else:
                k=0
                szorzo=0
            if(k==0):
                szorzo=0
            
            atirni_egy_sort("eredmenyek.txt",id,f"{reszek2[0]};{reszek2[1]};{reszek2[2]};{szorzo}\n")
        if(jatek_neve == reszek2[0]):
            if not len(reszek2) > 1:
                talalt=True
def ranglista():
    jatekosok={
        "pontszam_sorrendben":[], #Ide tesszük bele az összes játékos összesített pontszámát. (Azért kell külön, hogy a sort() funkciót és a reverse() funkciót lehessen könnyedén használni. )
        "nev_sorrendben":[], #Ide tesszük majd bele úgy a játékosok nevét, hogy a hozzá tartozó pontszámmal megegyező indexen legyen. (pl: 50pont a 3. indexen van, akkor a játékos neve is ott lesz)
        "igazi_helyezes":[], #a tényleges helyezés, nem az index (pl ha ugyanaz a pontszáma van több játékosnak, akkor ők azonos helyen (pl 2.-2.), az utánuk lévő nem egyből fog jönni (pl nem 3., hanem 4. lesz))
        "ideiglenes_nev_es_pontszam":[]#Objektumok, amik tartalmazzák a nevet és a hozzátartozó pontot, ennek a segítségével lehet hozzárendelni a nevet a pontokhoz
    }
    fajl=open("fogadasok.txt","r",encoding="utf8")
    sorok=fajl.readlines()
    fajl.close()
    #Végigmegyünk a fogadásokon és kiszámoljuk a játékosok pontszámát, majd az összes adat, amit tudunk a jatekosok objektumhoz adunk (pontszam és ideiglenes_nev_es_pontszam)
    for sor in sorok:
        reszek=sor.strip().split(";")
        if(not {"nev":reszek[0],"pont":dinamikusPontSzamolás(reszek[0])} in jatekosok["ideiglenes_nev_es_pontszam"]):
            pont=round(dinamikusPontSzamolás(reszek[0]))
            jatekosok["pontszam_sorrendben"].append(pont)
            jatekosok["ideiglenes_nev_es_pontszam"].append({
                "nev":reszek[0],
                "pont":pont
            })
    #Sorrendbe rendezzük a pontokat és megfordítjuk, hogy csökkenő sorrenben legyen.
    jatekosok["pontszam_sorrendben"].sort()
    jatekosok["pontszam_sorrendben"].reverse()
    #Végigmegyünk a pontokon (csökkenő sorrendben) és hozzárendeljük mindegyikhez a megfelelő játékost.
    for pont in jatekosok["pontszam_sorrendben"]:
        for jatekos in jatekosok["ideiglenes_nev_es_pontszam"]:
            if(not jatekos["nev"] in jatekosok["nev_sorrendben"]):
                if(jatekos["pont"]==pont):
                    jatekosok["nev_sorrendben"].append(jatekos["nev"])
                    break
    #Végigmegyünk a névsorrenden és megnézzük, hogyha megegyezik a pontszáma az előzővel, akkor meg kell egyeznie a helyezése is az előzőével és a sorozatot növeljük, hogy a következő, akinek nem annyi a pontja az sokkal kisebb helyezést érjen el.
    sorozat=0
    for id,jatekos in enumerate(jatekosok["nev_sorrendben"]):
        if id == 0:
            jatekosok["igazi_helyezes"].append(1)
        else:
            if jatekosok["pontszam_sorrendben"][id] == jatekosok["pontszam_sorrendben"][id-1]:
                jatekosok["igazi_helyezes"].append(jatekosok["igazi_helyezes"][id-1])
                sorozat+=1
            else:
                jatekosok["igazi_helyezes"].append(jatekosok["igazi_helyezes"][id-1]+1+sorozat)
                sorozat=0
    #Kiírjuk
    for id,jatekos in enumerate(jatekosok["nev_sorrendben"]):
        print(f"{jatekosok['igazi_helyezes'][id]}. helyen: {jatekos}, {jatekosok['pontszam_sorrendben'][id]} ponttal")
    pass
def jatek_statisztika():
    fajl=open("jatekok.txt","r",encoding="utf8")
    sorok = fajl.readlines()
    fajl.close()
    for sor in sorok:
        reszek=sor.strip().split(";")
        if len(reszek) > 1:
            fogadasok_szama=0
            feltett_tetek_osszpontszama=0
            nyeremenyek_osszpontszama=0
            megnezett_alany_esemeny=[]
            jatek_nev=reszek[1]
            fajl2=open("fogadasok.txt","r",encoding="utf8")
            sorok2=fajl2.readlines()
            fajl2.close()
            for sor2 in sorok2:
                reszek2=sor2.strip().split(";")
                if(reszek2[1] == jatek_nev):
                    fogadasok_szama+=1
                    feltett_tetek_osszpontszama+=int(reszek2[2])
                    if(not f"{reszek2[3]}{reszek2[4]}" in megnezett_alany_esemeny):
                        nyeremenyek_osszpontszama+=haVanoszpontszamEgyJatekhoz(jatek_nev,reszek2[3],reszek2[4])
                        megnezett_alany_esemeny.append(f"{reszek2[3]}{reszek2[4]}")
            print(f"{jatek_nev}-ban/-ben")
            print(f"    {fogadasok_szama}db fogadása van")
            print(f"    {feltett_tetek_osszpontszama} összpontszáma van a feltett téteknek a játékhoz")
            print(f"    {nyeremenyek_osszpontszama} összpontszáma van a nyereményeknek a játékhoz")
            
        else:
            continue
    pass
def fogadasi_statisztika(jatek_nev_megadott:str):
    fajl=open("jatekok.txt","r",encoding="utf8")
    sorok = fajl.readlines()
    fajl.close()
    talalt=False
    alanyok=[]
    alanyok_szama=0
    esemenyek=[]
    esemenyek_szama=0
    print(f"{jatek_nev_megadott}-hoz statisztikák: ")
    for sor in sorok:
        reszek=sor.strip().split(";")
        if len(reszek) > 1:
            if(reszek[1] == jatek_nev_megadott):
                talalt=True
                alanyok_szama=int(reszek[2])
                esemenyek_szama=int(reszek[3])
        else:
            if(talalt):
                if(len(alanyok)<alanyok_szama):
                    alanyok.append(reszek[0])
                elif(len(esemenyek)<esemenyek_szama):
                    esemenyek.append(reszek[0])
                if(len(esemenyek)==esemenyek_szama):
                    #Ez az utolsó sora a játéknak a jatekok.txt-ben
                    talalt=False
                    fajl2=open("fogadasok.txt","r",encoding="utf8")
                    sorok2=fajl2.readlines()
                    fajl2.close()
                    for alany in alanyok:
                        for esemeny in esemenyek:
                            fogadasok_szama=0
                            feltett_tetek_osszpontszama=0
                            nyeremenyek_osszpontszama=haVanoszpontszamEgyJatekhoz(jatek_nev_megadott,alany,esemeny)
                            for sor2 in sorok2:
                                reszek2=sor2.strip().split(";")
                                if(reszek2[1] == jatek_nev_megadott and reszek2[3] == alany and reszek2[4] == esemeny):
                                    fogadasok_szama+=1
                                    feltett_tetek_osszpontszama+=int(reszek2[2])
                            print(f"    {alany}+{esemeny}-hez/höz adatok:")
                            print(f"        fogadások száma:{fogadasok_szama}")
                            print(f"        feltett tétek összpontszáma:{feltett_tetek_osszpontszama}")
                            print(f"        nyeremények összpontszáma:{nyeremenyek_osszpontszama}")
    pass
def egyedi_jatek_nev(jatek_neve:str)->bool:
    fajl=open("jatekok.txt","r",encoding="utf8")
    sorok=fajl.readlines()
    fajl.close()
    for sor in sorok:
        reszek = sor.strip().split(";")
        if len(reszek) > 1:
            if(jatek_neve==reszek[1]):
                return False
    return True
def fogadott_e_mar(nev:str,jatek_neve:str,alany:str,esemeny:str)->bool:
    fajl=open("fogadasok.txt","r",encoding="utf8")
    sorok=fajl.readlines()
    fajl.close()
    for sor in sorok:
        reszek = sor.strip().split(";")
        if(nev==reszek[0] and jatek_neve == reszek[1] and alany == reszek[3] and esemeny == reszek[4]):
            return True
    return False
def Szam_e(bekeres):
    while True:
        user_input = input(bekeres)
        if user_input.isnumeric():
            return int(user_input)
        else:
            continue
def le_van_e_zarva_osszes_jatekot_vissza_adja()->list:
    elerheto_jatekok = []
    fajl=open("jatekok.txt","r",encoding="utf8")
    sorok = fajl.readlines()
    fajl.close()
    talalt=False
    neve=""
    szervezo=""
    alanyok=[]
    alanyok_szama=0
    esemenyek=[]
    esemenyek_szama=0

    for sor in sorok:
        reszek=sor.strip().split(";")
        if len(reszek) > 1:
            if(eredmeny_jatekhoz(reszek[1]) == {}):
                #Csak azokat a játékokat nézi, ahol nincs eredmény és ez az első sora a játéknak a jatekok.txt-be, ez tartalmazza a nevét, az alanyok számát, stb.
                neve=reszek[1]
                szervezo=reszek[0]
                talalt=True
                alanyok_szama=int(reszek[2])
                esemenyek_szama=int(reszek[3])
        else:
            if(talalt):
                if(len(alanyok)<alanyok_szama):
                    alanyok.append(reszek[0])
                elif(len(esemenyek)<esemenyek_szama):
                    esemenyek.append(reszek[0])
                if(len(esemenyek)==esemenyek_szama):
                    talalt=False
                    elerheto_jatekok.append({
                        "szervezo":szervezo,
                        "jatek_neve":neve,
                        "alanyok":alanyok,
                        "esemenyek":esemenyek
                    })
                    esemenyek=[]
                    alanyok=[]
    return elerheto_jatekok
def eredmeny_jatekhoz(jatek_neve:str):
    fajl=open("eredmenyek.txt","r",encoding="utf8")
    sorok = fajl.readlines()
    fajl.close()
    talalt=False
    valaha_talalt=False
    eredmeny={}
    for sor in sorok:
        reszek=sor.strip().split(";")
        if(talalt):
            alany={
                reszek[0]:
                {reszek[1]:{"eredmeny":reszek[2],
                            "szorzo":float(reszek[3])
                }}
            }
            if(reszek[0] in eredmeny.keys()):
                belso_alany={**eredmeny[reszek[0]], **alany[reszek[0]]}
                
                eredmeny = {**eredmeny, **{
                    reszek[0]:belso_alany
                }}
            else:
                eredmeny = {**eredmeny, **alany}
        if(jatek_neve == reszek[0]):
            if not len(reszek) > 1:
                talalt=True
                valaha_talalt=True
        
    if(not valaha_talalt):
        eredmeny = {}
    return eredmeny
def atirni_egy_sort(fajl_neve,hanyadik,sor):
    fajl=open(fajl_neve,"r",encoding="utf8")
    sorok=fajl.readlines()
    sorok[hanyadik]=sor
    fajl.close()
    fajl=open(fajl_neve,"w",encoding="utf8")
    fajl.write("".join(sorok))
    fajl.close()
def dinamikusPontSzamolás(fogado_fel:str):
    alap_pont=100
    fajl=open("fogadasok.txt","r",encoding="utf8")
    sorok=fajl.readlines()
    fajl.close()
    for sor in sorok:
        reszek=sor.strip().split(";")
        if(reszek[0]==fogado_fel):
            alap_pont-=int(reszek[2])
            eredmeny_ha_van = eredmeny_jatekhoz(reszek[1])
            if(eredmeny_ha_van!={}):
                if(eredmeny_ha_van[reszek[3]][reszek[4]]["eredmeny"] == reszek[5]):   
                    alap_pont+=round(int(reszek[2])*eredmeny_ha_van[reszek[3]][reszek[4]]["szorzo"],2)
    return alap_pont
def haVanoszpontszamEgyJatekhoz(jatek_nev:str,alany:str,esemeny:str):
    osszpontszam=0
    havaneredmeny=eredmeny_jatekhoz(jatek_nev)
    if(havaneredmeny!={}):
        fajl=open("fogadasok.txt","r",encoding="utf8")
        sorok=fajl.readlines()
        fajl.close()
        for sor in sorok:
            reszek=sor.strip().split(";")
            if(reszek[1] == jatek_nev and reszek[3] == alany and reszek[4] == esemeny and reszek[5] == havaneredmeny[alany][esemeny]["eredmeny"]):
                osszpontszam+=havaneredmeny[alany][esemeny]["szorzo"]*int(reszek[2])
    return osszpontszam


min_jelszo_hossz=8
max_nev_hossz=15
min_nev_hossz=4
max_felhasznalonev_hossz=15
min_felhasznalonev_hossz=4
max_jateknev_hossz=50
max_alany_hossz=25
max_esemeny_hossz=25


def jelszo_rejtese(input:QLineEdit,kezdeti_felirat:str):
    print(input.text())
    sorozat=0
    if input.placeholderText() == kezdeti_felirat:
        input.setPlaceholderText("")
    if not input.property("canToggle"):
        input.setPlaceholderText(input.text())
        return
    if len(input.text()) == 0:
        input.setPlaceholderText(kezdeti_felirat)
    else:
        szoveg=input.text()
        felirat=input.placeholderText()
        valtozas=""
        for id,karakter in enumerate(szoveg):
            if len(szoveg)<len(felirat):
                felirat_lesz=""
                for idx,i in enumerate(felirat):
                    if not idx == input.cursorPosition():
                        felirat_lesz+=i
                valtozas=felirat_lesz
            else:
                if karakter == "*":
                    if id-sorozat < len(felirat) and id-sorozat > -1:#felhasználó csillagot(*) tett a jelszavába
                        valtozas+=felirat[id-sorozat]
                else:
                    sorozat=1
                    valtozas+=karakter
        input.setPlaceholderText(valtozas)
        input.setText(szovegKicsereleseCsillagokra(input.placeholderText()))
def jelszo_megjelenitese(input:QLineEdit,valtoGomb,kezdeti_felirat):
    jelenlegiMod = valtoGomb.property("toggle")
    if jelenlegiMod == "😄":
        valtoGomb.setProperty("toggle","😃")
        input.setProperty("canToggle",False)
        #Látni akarja
    elif jelenlegiMod == "😃":
        valtoGomb.setProperty("toggle","😄")
        input.setProperty("canToggle",True)
        #Elrejteni
    valtoGomb.setText(jelenlegiMod)
    felirat=input.placeholderText()
    input.setText(felirat)
    jelszo_rejtese(input,kezdeti_felirat)
def jelszo_titkositasa(jelszo:str)->str:
    # Create a SHA-256 hash object
    hash_object = hashlib.sha256()
    # Convert the password to bytes and hash it
    hash_object.update(jelszo.encode())
    # Get the hex digest of the hash
    hash_password = hash_object.hexdigest()
    return hash_password
def jelszo_helyes_e(jelszo:str,titkositott_jelszo:str)->bool:
    hash_object = hashlib.sha256()
    hash_object.update(jelszo.encode())
    # Get the hex digest of the hash
    hash_password = hash_object.hexdigest()
    return hash_password == titkositott_jelszo
def szovegKicsereleseCsillagokra(szoveg:str):
    return "*"*len(szoveg)
def jatekot_felhasznalo_szervezte(jatek:dict,felhasznalo_neve:str):
    if jatek["szervezo"] == felhasznalo_neve:
        return jatek
    return None      
def benyujtott_regisztracio(felhasznalo_nev_input:QLineEdit,jelszo_input:QLineEdit,megerosito_jelszo_input:QLineEdit ):
    felhasznalo_nev = felhasznalo_nev_input.text()
    if len(felhasznalo_nev)<min_felhasznalonev_hossz:
        return f"Túl rövid felhasznalónév, min: {min_felhasznalonev_hossz}"
    elif len(felhasznalo_nev)>max_felhasznalonev_hossz:
        return f"Túl hosszú felhasznalónév, max: {max_felhasznalonev_hossz}"
    fajl = open("felhasznalok.txt","r",encoding="utf8")
    sorok=fajl.readlines()
    fajl.close()
    egyedi=True
    for sor in sorok:
        reszek=sor.strip().split(";")
        if reszek[0]==felhasznalo_nev:
            egyedi=False
    if not egyedi:
        return "A felhasználónév foglalt!"
    if "*" in jelszo_input.text():
        jelszo = jelszo_input.placeholderText()
    else:
        jelszo = jelszo_input.text()
    if len(jelszo)<min_jelszo_hossz:
        return f"Túl rövid jelszó (min:{min_jelszo_hossz})"
    if jelszo != megerosito_jelszo_input.placeholderText():
        return "Nem egyezik meg a jelszó!"
    fajl = open("felhasznalok.txt","a",encoding="utf8")
    fajl.write(f"{felhasznalo_nev};{jelszo_titkositasa(jelszo)};{felhasznalo_nev}\n") #TODO: IMPORTANT az 0. a felhasznalonev, megváltoztathatatlan, a 2. a megjelenített név
    fajl.close()
    return True
def benyujtott_bejelentkezes(input_felhasznalonev:QLineEdit,input_jelszo:QLineEdit):
    felhasznalonev = input_felhasznalonev.text()
    print("Felh:", felhasznalonev)
    if input_jelszo.text().find("*") == -1:
        jelszo = jelszo_titkositasa(input_jelszo.text())
    else:
        jelszo = jelszo_titkositasa(input_jelszo.placeholderText())
    print("Jelsz:", jelszo)
    fajl=open("felhasznalok.txt","r",encoding="utf8")
    sorok=fajl.readlines()
    fajl.close()
    talalt=False
    nev=""
    for sor in sorok:
        reszek=sor.strip().split(";")
        if felhasznalonev == reszek[0] and jelszo == reszek[1]:
            print("Bejelentkeztél")
            print(dinamikusPontSzamolás(felhasznalonev))
            nev=reszek[2]
            talalt=True
    if not talalt:
        return {"státusz":False,"válasz":"Nincs ilyen felhasználónév vagy jelszó!"}
    else:
        return {"státusz":True,"válasz":[felhasznalonev,nev]}
def benyujtott_eredmeny(jatek:dict,alanyok_es_esemyenek_messages:list):
    eredmenyek = []
    for message in alanyok_es_esemyenek_messages:
        eredmenyek.append({
        "alany":message.property("alany"),
        "esemeny":message.property("esemeny"),
        "eredmeny":message.text()
        })
    eredmeny_txt_be={
        "jatek_nev":jatek["jatek_neve"],
        "eredmenyek":eredmenyek
    }
    fajl=open("eredmenyek.txt","a",encoding="utf8")
    fajl.write(eredmeny_txt_be["jatek_nev"]+"\n")
    szorzo=0
    for eredmeny in eredmeny_txt_be["eredmenyek"]:
        fajl.write(f"{eredmeny['alany']};{eredmeny['esemeny']};{eredmeny['eredmeny']};{szorzo}\n")
    fajl.close()
    szorzo_frissitese(jatek["jatek_neve"])
    return jatek
def plusAlanyokésEsemenyek(plusz_alany:int,plusz_esemeny:int,osszesAlany:QGridLayout,osszesEsemeny:QGridLayout,alanyTarolo:QWidget,esemenyTarolo:QWidget):
    
    for i in range(plusz_alany):
        hany=len(alanyTarolo.children())-1
        sor=int(hany/4)
        oszlop=hany%4
        #Kiszámoljuk a sort és oszlopot, hogy ne egymás alá, de kettessével mellé is tegye
        print(f"{sor},{oszlop},{hany},{len(alanyTarolo.children())}")
        uj_alany= QLineEdit(alanyTarolo)
        uj_alany.setPlaceholderText(f"alany")
        uj_alany.setFixedHeight(100)
        osszesAlany.addWidget(uj_alany,sor,oszlop,1,1)
    for i in range(plusz_esemeny):
        hany=len(esemenyTarolo.children())-1
        sor=int(hany/4)
        oszlop=hany%4
        
        uj_esemeny= QLineEdit(esemenyTarolo)
        uj_esemeny.setPlaceholderText(f"esemény")
        uj_esemeny.setFixedHeight(100)
        osszesEsemeny.addWidget(uj_esemeny,sor,oszlop,1,1)
def benyujtott_jatek_letrehozasa(felhasznalonev:str,megnevezes_input:QLineEdit,osszesAlany:QGroupBox,osszesEsemeny:QGroupBox):   
    if not egyedi_jatek_nev(megnevezes_input.text()):
        return "Nem egyedi játék név!!"
    if len(megnevezes_input.text())>max_jateknev_hossz:
        return f"Túl hosszú játéknév!({max_jateknev_hossz})"
    alanyok=[]
    #Az első a grid layout, ezt figyelmen kívül kell hagyni!
    for alany in osszesAlany.children():
        if type(alany) == QGridLayout:
            continue
        if alany.text() not in alanyok and alany.text() != "":
            if len(alany.text())>max_alany_hossz:
                return f"{alany.text()} alany túl hosszú!({max_alany_hossz})"
            else:
                alanyok.append(alany.text())
        elif alany.text() in alanyok and alany.text() != "":
            return f"{alany.text()} már volt!"
    if len(alanyok)<2:
        return "Kevesebb, mint 2 alany!"
    esemenyek = []
    #Az első a grid layout, ezt figyelmen kívül kell hagyni!
    for esemeny in osszesEsemeny.children():
        if type(esemeny) == QGridLayout:
            continue
        if esemeny.text() not in esemenyek and esemeny.text() != "":
            if len(esemeny.text())>max_esemeny_hossz:
                return f"{esemeny.text()} esemény túl hosszú!({max_esemeny_hossz})"
            else:
                esemenyek.append(esemeny.text())
        elif esemeny.text() in esemenyek and esemeny.text() != "":
            return f"{esemeny.text()} már volt!"
    if len(esemenyek)<2:
        return "Kevesebb, mint 2 esemény!"
    fajl=open("jatekok.txt","a",encoding="utf8")
    fajl.write(f"{felhasznalonev};{megnevezes_input.text()};{len(alanyok)};{len(esemenyek)}\n")
    for alany in alanyok:
        fajl.write(f"{alany}\n")
    for esemeny in esemenyek:
        fajl.write(f"{esemeny}\n")
    fajl.close()
    return True
def benyujtott_fogadas(felhasznalonev:str,jatek:dict,kivalasztott_alany_input:QComboBox,kivalasztott_esemeny_input:QComboBox,ertek_input:QLineEdit,tet_input:QLineEdit):
    pont=dinamikusPontSzamolás(felhasznalonev)
    if not tet_input.text().isnumeric():
        return "A tétnek számnak kell lennie!"
    if fogadott_e_mar(felhasznalonev,jatek["jatek_neve"],kivalasztott_alany_input.currentText(),kivalasztott_esemeny_input.currentText()):
        return "Már fogadtál erre a játékra!"
    if ";" in ertek_input.text():
        return 'Nem lehet ";"-nak szerepelnie az értékben!'
    if(int(tet_input.text())>pont):
        return f"Nincs {int(tet_input.text())} pontod!"
    elif(int(tet_input.text())<0):
        return "Legalább tegyél fel valamennyi pontot!"
    file=open("fogadasok.txt","a",encoding="utf8")
    file.write(f"{felhasznalonev};{jatek['jatek_neve']};{int(tet_input.text())};{kivalasztott_alany_input.currentText()};{kivalasztott_esemeny_input.currentText()};{ertek_input.text()}\n")
    file.close()
    return True
def ranglista_guihoz():
    jatekosok={
        "pontszam_sorrendben":[], #Ide tesszük bele az összes játékos összesített pontszámát. (Azért kell külön, hogy a sort() funkciót és a reverse() funkciót lehessen könnyedén használni. )
        "nev_sorrendben":[], #Ide tesszük majd bele úgy a játékosok nevét, hogy a hozzá tartozó pontszámmal megegyező indexen legyen. (pl: 50pont a 3. indexen van, akkor a játékos neve is ott lesz)
        "igazi_helyezes":[], #a tényleges helyezés, nem az index (pl ha ugyanaz a pontszáma van több játékosnak, akkor ők azonos helyen (pl 2.-2.), az utánuk lévő nem egyből fog jönni (pl nem 3., hanem 4. lesz))
        "ideiglenes_nev_es_pontszam":[]#Objektumok, amik tartalmazzák a nevet és a hozzátartozó pontot, ennek a segítségével lehet hozzárendelni a nevet a pontokhoz
    }
    fajl=open("fogadasok.txt","r",encoding="utf8")
    sorok=fajl.readlines()
    fajl.close()
    #Végigmegyünk a fogadásokon és kiszámoljuk a játékosok pontszámát, majd az összes adat, amit tudunk a jatekosok objektumhoz adunk (pontszam és ideiglenes_nev_es_pontszam)
    for sor in sorok:
        reszek=sor.strip().split(";")
        if(not {"nev":reszek[0],"pont":dinamikusPontSzamolás(reszek[0])} in jatekosok["ideiglenes_nev_es_pontszam"]):
            pont=round(dinamikusPontSzamolás(reszek[0]))
            jatekosok["pontszam_sorrendben"].append(pont)
            jatekos_neve = felhasznalo_neve(reszek[0])#Hamisat visszaadhat, de akkor valaki kézzel belenyúlt a fájlokba
            if jatekos_neve == False:
                continue
            
            jatekosok["ideiglenes_nev_es_pontszam"].append({
                "nev":jatekos_neve,
                "pont":pont
            })
    #Sorrendbe rendezzük a pontokat és megfordítjuk, hogy csökkenő sorrenben legyen.
    jatekosok["pontszam_sorrendben"].sort()
    jatekosok["pontszam_sorrendben"].reverse()
    #Végigmegyünk a pontokon (csökkenő sorrendben) és hozzárendeljük mindegyikhez a megfelelő játékost.
    for pont in jatekosok["pontszam_sorrendben"]:
        for jatekos in jatekosok["ideiglenes_nev_es_pontszam"]:
            if(not jatekos["nev"] in jatekosok["nev_sorrendben"]):
                if(jatekos["pont"]==pont):
                    jatekosok["nev_sorrendben"].append(jatekos["nev"])
                    break
    #Végigmegyünk a névsorrenden és megnézzük, hogyha megegyezik a pontszáma az előzővel, akkor meg kell egyeznie a helyezése is az előzőével és a sorozatot növeljük, hogy a következő, akinek nem annyi a pontja az sokkal kisebb helyezést érjen el.
    sorozat=0
    for id,jatekos in enumerate(jatekosok["nev_sorrendben"]):
        if id == 0:
            jatekosok["igazi_helyezes"].append(1)
        else:
            if jatekosok["pontszam_sorrendben"][id] == jatekosok["pontszam_sorrendben"][id-1]:
                jatekosok["igazi_helyezes"].append(jatekosok["igazi_helyezes"][id-1])
                sorozat+=1
            else:
                jatekosok["igazi_helyezes"].append(jatekosok["igazi_helyezes"][id-1]+1+sorozat)
                sorozat=0
    return jatekosok
def jatek_statisztika_guihoz():
    fajl=open("jatekok.txt","r",encoding="utf8")
    sorok = fajl.readlines()
    fajl.close()
    jatekok=[]
    for sor in sorok:
        reszek=sor.strip().split(";")
        if len(reszek) > 1:
            fogadasok_szama=0
            feltett_tetek_osszpontszama=0
            nyeremenyek_osszpontszama=0
            megnezett_alany_esemeny=[]
            jatek_nev=reszek[1]
            fajl2=open("fogadasok.txt","r",encoding="utf8")
            sorok2=fajl2.readlines()
            fajl2.close()
            for sor2 in sorok2:
                reszek2=sor2.strip().split(";")
                if(reszek2[1] == jatek_nev):
                    fogadasok_szama+=1
                    feltett_tetek_osszpontszama+=int(reszek2[2])
                    if(not f"{reszek2[3]}{reszek2[4]}" in megnezett_alany_esemeny):
                        nyeremenyek_osszpontszama+=haVanoszpontszamEgyJatekhoz(jatek_nev,reszek2[3],reszek2[4])
                        megnezett_alany_esemeny.append(f"{reszek2[3]}{reszek2[4]}")
            jatekok.append({
                "jatek_neve":jatek_nev,
                "fogadasok_szama":fogadasok_szama,
                "feltett_tetek_osszpontszama":feltett_tetek_osszpontszama,
                "nyeremenyek_osszpontszama":nyeremenyek_osszpontszama
            })
        else:
            continue
    return jatekok
def fogadasi_statisztika_guihoz(jatek_nev_megadott:str):
    fajl=open("jatekok.txt","r",encoding="utf8")
    sorok = fajl.readlines()
    fajl.close()
    talalt=False
    alanyok=[]
    alanyok_szama=0
    esemenyek=[]
    esemenyek_szama=0
    
    jatek=[]
    
    
    for sor in sorok:
        reszek=sor.strip().split(";")
        if len(reszek) > 1:
            if(reszek[1] == jatek_nev_megadott):
                talalt=True
                alanyok_szama=int(reszek[2])
                esemenyek_szama=int(reszek[3])
        else:
            if(talalt):
                if(len(alanyok)<alanyok_szama):
                    alanyok.append(reszek[0])
                elif(len(esemenyek)<esemenyek_szama):
                    esemenyek.append(reszek[0])
                if(len(esemenyek)==esemenyek_szama):
                    #Ez az utolsó sora a játéknak a jatekok.txt-ben
                    talalt=False
                    fajl2=open("fogadasok.txt","r",encoding="utf8")
                    sorok2=fajl2.readlines()
                    fajl2.close()
                    for alany in alanyok:
                        for esemeny in esemenyek:
                            fogadasok_szama=0
                            feltett_tetek_osszpontszama=0
                            nyeremenyek_osszpontszama=haVanoszpontszamEgyJatekhoz(jatek_nev_megadott,alany,esemeny)
                            for sor2 in sorok2:
                                reszek2=sor2.strip().split(";")
                                if(reszek2[1] == jatek_nev_megadott and reszek2[3] == alany and reszek2[4] == esemeny):
                                    fogadasok_szama+=1
                                    feltett_tetek_osszpontszama+=int(reszek2[2])
                            jatek.append({
                                "alany":alany,
                                "esemeny":esemeny,
                                "fogadasok_szama":fogadasok_szama,
                                "feltett_tetek_osszpontszama":feltett_tetek_osszpontszama,
                                "nyeremenyek_osszpontszama":nyeremenyek_osszpontszama
                            })
                            
    return jatek
def osszesJatek():
    fajl=open("jatekok.txt","r",encoding="utf8")
    sorok=fajl.readlines()
    fajl.close()
    jatekok=[]
    for sor in sorok:
        reszek=sor.strip().split(";")
        if len(reszek)>1:
            jatekok.append(reszek[1])
    return jatekok
def fogadasiStatisztikaKivalasztottjatekInputahoz(kivalasztott_jatek_input:QComboBox,osszesAlanyEsemeny:QVBoxLayout,osszesAlanyEsemenyTarolo:QScrollArea):
    for i in reversed(range(osszesAlanyEsemeny.count())): 
            osszesAlanyEsemeny.itemAt(i).widget().deleteLater()
    jatek=fogadasi_statisztika_guihoz(kivalasztott_jatek_input.currentText())
    jatek_neve=QLabel(f"{kivalasztott_jatek_input.currentText()}-hoz statisztikák: ",osszesAlanyEsemenyTarolo)
    osszesAlanyEsemeny.addWidget(jatek_neve)
    for alany_es_esemenyek in jatek:
        alany_es_esemenyek_label = QLabel(f"{alany_es_esemenyek['alany']}+{alany_es_esemenyek['esemeny']}-hez/höz adatok:\nfogadások száma:{alany_es_esemenyek['fogadasok_szama']}\nfeltett tétek összpontszáma:{alany_es_esemenyek['feltett_tetek_osszpontszama']}\nnyeremények összpontszáma:{alany_es_esemenyek['nyeremenyek_osszpontszama']}",osszesAlanyEsemenyTarolo)
        alany_es_esemenyek_label.setMaximumHeight(300)
        osszesAlanyEsemeny.addWidget(alany_es_esemenyek_label)
def felhasznalo_neve(felhasznalonev:str):
    fajl=open("felhasznalok.txt","r",encoding="utf8")
    sorok=fajl.readlines()
    fajl.close()
    for sor in sorok:
        reszek=sor.strip().split(";")
        if reszek[0] == felhasznalonev:
            return reszek[2]
    return False
def benyujtott_profilbeallitasok(felhasznalonev:str,megjelenitett_nev_input:QLineEdit):
    if len(megjelenitett_nev_input.text())>max_nev_hossz:
        return "Túl hosszú név!"
    elif len(megjelenitett_nev_input.text())<min_nev_hossz:
        return "Túl rövid név!"
    fajl=open("felhasznalok.txt","r",encoding="utf8")
    sorok=fajl.readlines()
    fajl.close()
    for id,sor in enumerate(sorok):
        reszek=sor.strip().split(";")
        if reszek[0] == felhasznalonev:
            atirni_egy_sort("felhasznalok.txt",id,f"{reszek[0]};{reszek[1]};{megjelenitett_nev_input.text()}")
            return True
    return "Valami nem jó!"
