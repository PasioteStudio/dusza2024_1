def egyedi_jatek_nev(jatek):
    file=open("jatekok.txt","r",encoding="utf8")
    lines=file.readlines()
    for line in lines:
        parts = line.strip().split(";")
        if(jatek==parts[1]):
            return False
    file.close()
    return True
def fogadott_e_mar(nev,jatek,alany,esemeny):
    file=open("fogadasok.txt","r",encoding="utf8")
    lines=file.readlines()
    for line in lines:
        parts = line.strip().split(";")
        if(nev==parts[0] and jatek == parts[1] and alany == parts[3] and esemeny == parts[4]):
            return True
    file.close()
    return False
def NumInput(bekeres):
    while True:
        user_input = input(bekeres)
        try:
            return int(user_input)
        except:
            continue
def le_van_e_zarva():
    elerheto_jatekok = []
    file=open("jatekok.txt","r",encoding="utf8")
    lines = file.readlines()
    talalt=False
    neve=""
    szervezo=""
    alanyok=[]
    alanyok_szama=0
    esemenyek=[]
    esemenyek_szama=0

    for line in lines:
        parts=line.strip().split(";")
        try:
            tmp=parts[1]
            if(eredmeny_jatekhoz(parts[1]) == {}):
                neve=parts[1]
                szervezo=parts[0]
                talalt=True
                alanyok_szama=int(parts[2])
                esemenyek_szama=int(parts[3])
        except:
            if(talalt):
                if(len(alanyok)<alanyok_szama):
                    alanyok.append(parts[0])
                if(len(esemenyek)<esemenyek_szama):
                    esemenyek.append(parts[0])
                if(len(esemenyek)==esemenyek_szama):
                    talalt=False
                    elerheto_jatekok.append({
                        "szervezo":szervezo,
                        "jatek_neve":neve,
                        "alanyok":alanyok,
                        "esemenyek":esemenyek
                    })
            continue
    file.close()
    return elerheto_jatekok
def eredmeny_jatekhoz(jatek_neve):
    file=open("eredmenyek.txt","r",encoding="utf8")
    lines = file.readlines()
    talalt=False
    eredmeny={}
    for line in lines:
        parts=line.strip().split(";")
        if(talalt):
            eredmeny[parts[0]][parts[1]]["eredmeny"] = parts[2]
            eredmeny[parts[0]][parts[1]]["szorzo"] = parts[3]
        if(jatek_neve == parts[0]):
            try:
                tmp=parts[1]
            except:
                talalt=True
        
    file.close()
    return eredmeny