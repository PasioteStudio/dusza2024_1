def start():
    print("1- Játék létrehozása")
    print("2- Fogadás leadása")
    print("3- Játék lezárása")
    print("4- Lekérdezések")
    print("5- Kilépés")
    while True:  
        user_input = NumInput("Válassz: ")
        if(user_input > 5 or user_input<1):
            continue
        elif(user_input == 1):
            jatek_letrehozasa()
            continue
        elif(user_input == 2):
            fogadas_leadasa()
            continue
        elif(user_input == 3):
            jatek_letrehozasa()
            continue
        elif(user_input == 4):
            jatek_letrehozasa()
            continue
        elif(user_input == 5):
            break
start()
def jatek_letrehozasa():
    szerzo = input("Ki a szervező? ")
    megnevezes = input("Mi a játék megnevezése? (egyedinek kell lennie) ")
    alanyok = []
    while True:
        input3 = input("Kik az alanyok? (különböznek egymástól) ")
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
    #Írja ki az összes le nem zárt játékot (és teszteljen rá)
    elerheto_jatekok=[
        {
            "neve":"asd"
        }
    ]
    kivalasztott_jatek = input("Válassz egy játékot!: ")
    while True:
        for jatek in elerheto_jatekok:
            if(kivalasztott_jatek == jatek["neve"]):
                while True:
                    kivalasztott_alany = input("Válassz egy alanyt!: ")
                    kivalasztott_esemeny = input("Válassz egy eseményt!: ")
                    if(fogadott_e_mar()):
                        print("Már fogadtál erre!")
                        continue
                    break
                kivalasztott_ertek = input("Válassz egy értéket!: ")
                while True:
                    kivalasztott_tet = NumInput("Válassz egy tétet!: ")
                    if(kivalasztott_tet>pont):
                        continue
                    break
                file=open("fogadasok.txt","a",encoding="utf8")
                file.write(f"{fogado_fel};{kivalasztott_jatek};{kivalasztott_tet};{kivalasztott_alany};{kivalasztott_esemeny};{kivalasztott_ertek}")
                file.close()
                break
        continue
def jatek_lezarasa():
            
    
a = 1 + (5/(2 ** k - 1))

def fogadott_e_mar(nev,jatek,alany,esemeny):
    file=open("fogadasok.txt","r",encoding="utf8")
    lines=file.readlines()
    for line in lines:
        parts = line.strip().split(";")
        if(nev==parts[0] and jatek == parts[1] and alany == parts[3] and esemeny == parts[4]):
            return True
    return False
    file.close()
def NumInput(bekeres):
    while True:
        user_input = input(bekeres)
        try:
            return int(user_input)
        except:
            continue