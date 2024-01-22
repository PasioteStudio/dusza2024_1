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
    file.write(f"{szerzo};{megnevezes};{len(alanyok)};{len(esemenyek)}")
    for alany in alanyok:
        file.write(f"{alany}")
    for esemeny in esemenyek:
        file.write(f"{esemeny}")
    file.close()
def fogadas_leadasa():
    pont = 100
    fogado_fel = input("Fogadó fél neve: ")
    #Tétjeit le kell vonni és kiszámolni a megnyert összeget, így megkapjuk a "dinamikus" pontjait
    
    print(f"Pontod: {pont}")
        
    elerheto_jatekok=kezelo.le_van_e_zarva()
    print(elerheto_jatekok)
    #TODO: design
    kivalasztott_jatek = input("Válassz egy játékot!: ")
    while True:
        for jatek in elerheto_jatekok:
            if(kivalasztott_jatek == jatek["jatek_neve"]):
                while True:
                    kivalasztott_alany = input("Válassz egy alanyt!: ")
                    kivalasztott_esemeny = input("Válassz egy eseményt!: ")
                    if(kezelo.fogadott_e_mar()):
                        print("Már fogadtál erre!")
                        continue
                    break
                kivalasztott_ertek = input("Válassz egy értéket!: ")
                while True:
                    kivalasztott_tet = kezelo.NumInput("Válassz egy tétet!: ")
                    if(kivalasztott_tet>pont):
                        continue
                    break
                file=open("fogadasok.txt","a",encoding="utf8")
                file.write(f"{fogado_fel};{kivalasztott_jatek};{kivalasztott_tet};{kivalasztott_alany};{kivalasztott_esemeny};{kivalasztott_ertek}")
                file.close()
                break
        continue
def jatek_lezarasa():
    neved=input("Neved: ")
    jatek_megnevezese=("Lezárandó játék: ")
    for jatek in kezelo.le_van_e_zarva():
        if(jatek["szerzo"] == neved and jatek["neve"] == jatek_megnevezese):
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
                "jatek_nev":jatek["nev"],
                "eredmenyek":eredmenyek
            }
            file=open("edermenyek.txt","a",encoding="utf8")
            file.write(eredmeny_txt_be["jatek_nev"])
            szorzo=0
            for eredmeny in eredmeny_txt_be["eredmenyek"]:
                file.write(f"{eredmeny['alany']};{eredmeny['esemeny']};{eredmeny['eredmeny']};{szorzo}")
            file.close()
            kezelo.szorzo_frissitese(jatek["neve"])
            print("Siker!")
            start()
    print("Hibás!")
    start()
def lekerdezesek():
    print("1- Ranglista")
    print("2- Játék statisztika")
    print("3- Fogadási statisztika")
    print("4- Vissza")
    while True:  
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
                if(not kezelo.egyedi_jatek_nev(jatek_nev)):   
                    kezelo.fogadasi_statisztika(jatek_nev)
                    continue
                else:
                    continue
        elif(user_input == 4):
            start()
            break

def start():
    print("1- Játék létrehozása")
    print("2- Fogadás leadása")
    print("3- Játék lezárása")
    print("4- Lekérdezések")
    print("5- Kilépés")
    while True:  
        user_input = kezelo.NumInput("Válassz: ")
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
