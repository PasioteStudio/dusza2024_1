def szorzo_frissitese(jatek_neve):
    file=open("fogadasok.txt","r",encoding="utf8")
    lines=file.readlines()
    fogadasok={}
    for line in lines:
        parts=line.strip().split(";")
        if(parts[1]==jatek_neve):
            fogadasok[parts[3]+parts[4]]+=1
    file.close()
    
    file2=open("eredmenyek.txt","wr",encoding="utf8")
    lines2=file2.readlines()
    talalt=False
    for line2 in lines2:
        parts2=line2.strip().split(";")
        if(talalt):
            k=fogadasok[parts2[0]+parts2[1]]
            szorzo= 1 + (5/(2 ** k - 1))
            if(k==0):
                szorzo=0
            rewrite_a_line("eredmenyek.txt",0,f"{parts2[0]};{parts2[1]};{parts2[2]};{szorzo}")
        if(jatek_neve == parts[0]):
            try:
                tmp=parts[1]
            except:
                talalt=True
    file2.close()
def ranglista():
    return
def jatek_statisztika():
    file=open("jatekok.txt","r",encoding="utf8")
    lines = file.readlines()
    for line in lines:
        parts=line.strip().split(";")
        try:
            fogadasok_szama=0
            feltett_tetek_osszpontszama=0
            nyeremenyek_osszpontszama=0
            jatek_nev=parts[1]
            file2=open("fogadasok.txt","r",encoding="utf8")
            lines2=file2.readlines()
            for line2 in lines2:
                parts2=line2.strip().split(";")
                if(parts2[1] == jatek_nev):
                    fogadasok_szama+=1
                    feltett_tetek_osszpontszama+=parts2[2]
                    if(eredmeny_jatekhoz(jatek_nev) != {}):
                        nyeremenyek_osszpontszama+=0
                        #TODO
            print(f"{jatek_nev}-ban/-ben")
            print(f"{fogadasok_szama}db fogadása van")
            print(f"{feltett_tetek_osszpontszama} összpontszáma van a feltett téteknek a játékhoz")
            print(f"{nyeremenyek_osszpontszama} összpontszáma van a nyereményeknek a játékhoz")
            
            file2.close()
        except:
            continue
    file.close()
def fogadasi_statisztika(jatek_nev_megadott):
    file=open("jatekok.txt","r",encoding="utf8")
    lines = file.readlines()
    talalt=False
    neve=""
    szervezo=""
    alanyok=[]
    alanyok_szama=0
    esemenyek=[]
    esemenyek_szama=0
    print(f"{jatek_nev_megadott}-hoz statisztikák: ")
    for line in lines:
        parts=line.strip().split(";")
        try:
            tmp=parts[1]
            if(parts[1] == jatek_nev_megadott):
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
                    file2=open("fogadasok.txt","r",encoding="utf8")
                    lines2=file2.readlines()
                    for alany in alanyok:
                        for esemeny in esemenyek:
                            fogadasok_szama=0
                            feltett_tetek_osszpontszama=0
                            nyeremenyek_osszpontszama=0
                            for line2 in lines2:
                                parts2=line2.strip().split(";")
                                if(parts2[1] == jatek_nev_megadott and parts2[3] == alany and parts2[4] == esemeny):
                                    fogadasok_szama+=1
                                    feltett_tetek_osszpontszama+=parts2[2]
                                    nyeremenyek_osszpontszama+=0
                                    #TODO:
                            print(f"    {alany}+{esemeny}-hez/höz adatok:")
                            print(f"        fogadások száma:{fogadasok_szama}")
                            print(f"        feltett tétek összpontszáma:{feltett_tetek_osszpontszama}")
                            print(f"        nyeremények összpontszáma:{nyeremenyek_osszpontszama}")
                    file2.close()
    file.close()
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
def rewrite_a_line(file_name,nth,line):
    file=open(file_name,"wr",encoding="utf8")
    original_lines=file.readlines()
    original_lines[nth]=line
    file.write(original_lines)
    file.close()