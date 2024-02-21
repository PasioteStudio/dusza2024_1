#Sigmakik
import kezelo as kezelo
def jatek_letrehozasa():
    szerzo = input("Ki a szervező? ")
    while True:
        megnevezes = input("Mi a játék megnevezése? (egyedinek kell lennie) ")
        if(kezelo.egyedi_jatek_nev(megnevezes)):
            break
        continue
    alanyok = []
    while True:
        input3 = input("Kik az alanyok? (különböznek egymástól) ")
        if(input3 in alanyok):
            print("Ő már volt!")
            continue
        if(input3 == ""):
            break
        alanyok.append(input3)
    esemenyek = []
    while True:
        input4 = input("Mik az események? ")
        if(input4 == ""):
            break
        esemenyek.append(input4)
    file=open("jatekok.txt","a",encoding="utf8")
    file.write(f"{szerzo};{megnevezes};{len(alanyok)};{len(esemenyek)}\n")
    for alany in alanyok:
        file.write(f"{alany}\n")
    for esemeny in esemenyek:
        file.write(f"{esemeny}\n")
    file.close()
def fogadas_leadasa():
    fogado_fel = input("Fogadó fél neve: ")
    pont = kezelo.dinamikusPontSzamolás(fogado_fel)
    print(f"Pontod: {pont}")
        
    elerheto_jatekok=kezelo.le_van_e_zarva_osszes_jatekot_vissza_adja()
    print(elerheto_jatekok)

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
                kivalasztott_tet = kezelo.Szam_e("Válassz egy tétet!: ")
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
def jatek_lezarasa():
    neved=input("Neved: ")
    jatek_megnevezese=input("Lezárandó játék: ")
    siker=False
    for jatek in kezelo.le_van_e_zarva_osszes_jatekot_vissza_adja():
        if(jatek["szervezo"] == neved and jatek["jatek_neve"] == jatek_megnevezese):
            eredmenyek = []
            for alany in jatek['alanyok']:
                for esemeny in jatek['esemenyek']:    
                    eredmeny = input(f"{alany}-nak/-nek a(z) {esemeny}-ban/ben eredménye: ")
                    eredmenyek.append({
                        "alany":alany,
                        "esemeny":esemeny,
                        "eredmeny":eredmeny
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
            siker=True
    
    if siker:
        print("Siker!")
    else:
        print("Hibás!")
    pass
def lekerdezesek():
    while True:  
        print("----------")
        print("1- Ranglista")
        print("2- Játék statisztika")
        print("3- Fogadási statisztika")
        print("4- Vissza")
        user_input = kezelo.Szam_e("Válassz: ")
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

def start():
    while True:  
        print("----------")
        print("1- Játék létrehozása")
        print("2- Fogadás leadása")
        print("3- Játék lezárása")
        print("4- Lekérdezések")
        print("5- Kilépés")
        user_input = kezelo.Szam_e("Válassz: ")
        if(user_input > 5 or user_input<1):
            continue
        elif(user_input == 1):
            jatek_letrehozasa()
            continue
        elif(user_input == 2):
            fogadas_leadasa()
            continue
        elif(user_input == 3):
            jatek_lezarasa()
            continue
        elif(user_input == 4):
            lekerdezesek()
            continue
        elif(user_input == 5):
            break
start()
