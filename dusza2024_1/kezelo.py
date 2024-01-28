#Sigmakik
def szorzo_frissitese(jatek_neve):
    file=open("fogadasok.txt","r",encoding="utf8")
    lines=file.readlines()
    fogadasok={}
    for line in lines:
        parts=line.strip().split(";")
        if(parts[1]==jatek_neve):
            fogadasok[parts[3]+parts[4]]=0
    for line in lines:
        parts=line.strip().split(";")
        if(parts[1]==jatek_neve):
            fogadasok[parts[3]+parts[4]]+=1
    file.close()
    
    
    file2=open("eredmenyek.txt","r",encoding="utf8")
    lines2=file2.readlines()
    talalt=False
    for id,line2 in enumerate(lines2):
        parts2=line2.strip().split(";")
        if(talalt):
            if parts2[0]+parts2[1] in fogadasok.keys():
                k=fogadasok[parts2[0]+parts2[1]]
                szorzo= round(1 + (5/(2 ** k - 1)),2)
            else:
                k=0
                szorzo=0
            if(k==0):
                szorzo=0
            
            rewrite_a_line("eredmenyek.txt",id,f"{parts2[0]};{parts2[1]};{parts2[2]};{szorzo}\n")
        if(jatek_neve == parts2[0]):
            if not len(parts2) > 1:
                talalt=True
    file2.close()
def ranglista():
    jatekosok={
        "pontszam_sorrendben":[],
        "nev_sorrendben":[],
        "igazi_helyezes":[],
        "ideiglenes_nev":[],
        "ideiglenes_nev_es_pontszam":[]
    }
    file=open("fogadasok.txt","r",encoding="utf8")
    lines=file.readlines()
    for line in lines:
        parts=line.strip().split(";")
        if(not parts[0] in jatekosok["ideiglenes_nev"]):
            point=round(dinamikusPontSzamolás(parts[0]))
            jatekosok["pontszam_sorrendben"].append(point)
            jatekosok["ideiglenes_nev"].append(parts[0])
            jatekosok["ideiglenes_nev_es_pontszam"].append({
                "nev":parts[0],
                "pont":point
            })
    file.close()
    jatekosok["pontszam_sorrendben"].sort()
    jatekosok["pontszam_sorrendben"].reverse()
    
    for pont in jatekosok["pontszam_sorrendben"]:
        for jatekos in jatekosok["ideiglenes_nev_es_pontszam"]:
            if(not jatekos["nev"] in jatekosok["nev_sorrendben"]):
                if(jatekos["pont"]==pont):
                    jatekosok["nev_sorrendben"].append(jatekos["nev"])
                    break
    
    streak=0
    for id,jatekos in enumerate(jatekosok["nev_sorrendben"]):
        if id == 0:
            jatekosok["igazi_helyezes"].append(1)
        else:
            if jatekosok["pontszam_sorrendben"][id] == jatekosok["pontszam_sorrendben"][id-1]:
                jatekosok["igazi_helyezes"].append(jatekosok["igazi_helyezes"][id-1])
                streak+=1
            else:
                jatekosok["igazi_helyezes"].append(jatekosok["igazi_helyezes"][id-1]+1+streak)
                streak=0
    for id,jatekos in enumerate(jatekosok["nev_sorrendben"]):
        print(f"{jatekosok['igazi_helyezes'][id]}. helyen: {jatekos}, {jatekosok['pontszam_sorrendben'][id]} ponttal")
    pass
def jatek_statisztika():
    file=open("jatekok.txt","r",encoding="utf8")
    lines = file.readlines()
    for line in lines:
        parts=line.strip().split(";")
        if len(parts) > 1:
            fogadasok_szama=0
            feltett_tetek_osszpontszama=0
            nyeremenyek_osszpontszama=0
            megnezett_alany_esemeny=[]
            jatek_nev=parts[1]
            file2=open("fogadasok.txt","r",encoding="utf8")
            lines2=file2.readlines()
            for line2 in lines2:
                parts2=line2.strip().split(";")
                if(parts2[1] == jatek_nev):
                    fogadasok_szama+=1
                    feltett_tetek_osszpontszama+=int(parts2[2])
                    if(not f"{parts2[3]}{parts2[4]}" in megnezett_alany_esemeny):
                        nyeremenyek_osszpontszama+=haVanoszpontszamEgyJatekhoz(jatek_nev,parts2[3],parts2[4])
                        megnezett_alany_esemeny.append(f"{parts2[3]}{parts2[4]}")
            print(f"{jatek_nev}-ban/-ben")
            print(f"    {fogadasok_szama}db fogadása van")
            print(f"    {feltett_tetek_osszpontszama} összpontszáma van a feltett téteknek a játékhoz")
            print(f"    {nyeremenyek_osszpontszama} összpontszáma van a nyereményeknek a játékhoz")
            
            file2.close()
        else:
            continue
    file.close()
    pass
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
        if len(parts) > 1:
            if(parts[1] == jatek_nev_megadott):
                neve=parts[1]
                szervezo=parts[0]
                talalt=True
                alanyok_szama=int(parts[2])
                esemenyek_szama=int(parts[3])
        else:
            if(talalt):
                if(len(alanyok)<alanyok_szama):
                    alanyok.append(parts[0])
                elif(len(esemenyek)<esemenyek_szama):
                    esemenyek.append(parts[0])
                if(len(esemenyek)==esemenyek_szama):
                    talalt=False
                    file2=open("fogadasok.txt","r",encoding="utf8")
                    lines2=file2.readlines()
                    for alany in alanyok:
                        for esemeny in esemenyek:
                            fogadasok_szama=0
                            feltett_tetek_osszpontszama=0
                            nyeremenyek_osszpontszama=haVanoszpontszamEgyJatekhoz(jatek_nev_megadott,alany,esemeny)
                            for line2 in lines2:
                                parts2=line2.strip().split(";")
                                if(parts2[1] == jatek_nev_megadott and parts2[3] == alany and parts2[4] == esemeny):
                                    fogadasok_szama+=1
                                    feltett_tetek_osszpontszama+=int(parts2[2])
                            print(f"    {alany}+{esemeny}-hez/höz adatok:")
                            print(f"        fogadások száma:{fogadasok_szama}")
                            print(f"        feltett tétek összpontszáma:{feltett_tetek_osszpontszama}")
                            print(f"        nyeremények összpontszáma:{nyeremenyek_osszpontszama}")
                    file2.close()
    file.close()
    pass
def egyedi_jatek_nev(jatek):
    file=open("jatekok.txt","r",encoding="utf8")
    lines=file.readlines()
    for line in lines:
        parts = line.strip().split(";")
        if len(parts) > 1:
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
        if user_input.isnumeric():
            return int(user_input)
        else:
            continue
def le_van_e_zarva_osszes_jatekot_vissza_adja():
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
        if len(parts) > 1:
            if(eredmeny_jatekhoz(parts[1]) == {}):
                neve=parts[1]
                szervezo=parts[0]
                talalt=True
                alanyok_szama=int(parts[2])
                esemenyek_szama=int(parts[3])
        else:
            if(talalt):
                if(len(alanyok)<alanyok_szama):
                    alanyok.append(parts[0])
                elif(len(esemenyek)<esemenyek_szama):
                    esemenyek.append(parts[0])
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
    file.close()
    return elerheto_jatekok
def eredmeny_jatekhoz(jatek_neve):
    file=open("eredmenyek.txt","r",encoding="utf8")
    lines = file.readlines()
    talalt=False
    valaha_talalt=False
    eredmeny={}
    
    
    for line in lines:
        parts=line.strip().split(";")
        if(talalt):
            alany={
                parts[0]:
                {parts[1]:{"eredmeny":parts[2],
                                    "szorzo":float(parts[3])
                                    }}
            }
            if(parts[0] in eredmeny.keys()):
                belso_alany={**eredmeny[parts[0]], **alany[parts[0]]}
                
                eredmeny = {**eredmeny, **{
                    parts[0]:belso_alany
                }}
            else:
                eredmeny = {**eredmeny, **alany}
        if(jatek_neve == parts[0]):
            if not len(parts) > 1:
                talalt=True
                valaha_talalt=True
        
    file.close()
    if(not valaha_talalt):
        eredmeny = {}
    return eredmeny
def rewrite_a_line(file_name,nth,line):
    file=open(file_name,"r",encoding="utf8")
    original_lines=file.readlines()
    original_lines[nth]=line
    file.close()
    nothing=""
    file=open(file_name,"w",encoding="utf8")
    file.write(nothing.join(original_lines))
    file.close()
def dinamikusPontSzamolás(fogado_fel):
    default_point=100
    file=open("fogadasok.txt","r",encoding="utf8")
    lines=file.readlines()
    for line in lines:
        parts=line.strip().split(";")
        if(parts[0]==fogado_fel):
            default_point-=int(parts[2])
            print("Hamis")
            eredmeny_ha_van = eredmeny_jatekhoz(parts[1])
            if(eredmeny_ha_van!={}):
                if(eredmeny_ha_van[parts[3]][parts[4]]["eredmeny"] == parts[5]):   
                    default_point+=round(int(parts[2])*eredmeny_ha_van[parts[3]][parts[4]]["szorzo"],2)
    file.close()
    return default_point
def haVanoszpontszamEgyJatekhoz(jatek_nev,alany,esemeny):
    osszpontszam=0
    havaneredmeny=eredmeny_jatekhoz(jatek_nev)
    if(havaneredmeny!={}):
        file2=open("fogadasok.txt","r",encoding="utf8")
        lines2=file2.readlines()
        for line2 in lines2:
            parts2=line2.strip().split(";")
            if(parts2[1] == jatek_nev and parts2[3] == alany and parts2[4] == esemeny and parts2[5] == havaneredmeny[alany][esemeny]["eredmeny"]):
                osszpontszam+=havaneredmeny[alany][esemeny]["szorzo"]*int(parts2[2])
        file2.close()
    return osszpontszam

