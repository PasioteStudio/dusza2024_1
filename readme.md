# Bevezetés:
A program a Dusza Árpád Országos Programozói Emlékverseny 2023/2024 miatt készülhetett el. A feladat egy fogadásos játék volt, ahol fogadni, játékot létrehozni, lezárni és a ranglistát, játék statisztikáját és fogadási statisztikáját lehet megtekinteni.
# Felhasználói dokumentáció
 1. Python telepítése és PyQt5 külső python könyvtár kötelező a program futtatásához.
 2. FONTOS: Mindig lépjünk be a program mappájába(dusza), onnan indítsuk el
 3. Hogy futtassuk el kell indítanunk a gui.py-t (`py gui.py`)
  -  A program játékok készítésére:
 ![image](https://github.com/atemzy/dusza2024_1/assets/43964339/f04dfd08-e77d-453c-9195-a2016d67ba9b)
  - És annak lezárására:
 ![Képernyőkép 2024-02-21 181554](https://github.com/atemzy/dusza2024_1/assets/43964339/14312892-f38e-449c-9082-87c856958354)
  - Fogadás leadására:
 ![Képernyőkép 2024-02-21 181541](https://github.com/atemzy/dusza2024_1/assets/43964339/d0038e23-d0d7-456a-b23e-90abc0c55291)
  - Ranglista megtekintésére:
 ![Képernyőkép 2024-02-22 093952](https://github.com/atemzy/dusza2024_1/assets/43964339/ce64cf5d-833d-4f31-95c8-a425d898279a)
  - Játék statisztika megtekintésére:
 ![Képernyőkép 2024-02-22 094111](https://github.com/atemzy/dusza2024_1/assets/43964339/e6828472-3eca-4b9b-8206-a6e6b474c26b)
  - Fogadási statisztika megtekintésére:
 ![Képernyőkép 2024-02-22 094133](https://github.com/atemzy/dusza2024_1/assets/43964339/dd6e3bbf-a4a9-4654-b238-695cbb5f5a92)
  használható.
# Fejlesztői dokumentáció:
## A fájlstruktúra kinézete:
```
├── forrasok
│   ├── kepek
│   │   ├── token.png
│   │   └── icon.jpg
│   └── stilusok
│       └── gui.css
├── ui
│   ├── koszontes.py
│   ├── felhasznalo.py
│   ├── fogado.py
│   ├── lekerdezes.py
│   └── szervezo.py
├── kezelo.py
├── gui.py
├── fogadasok.txt
├── felhasznalok.txt
├── jatekok.txt
├── readme.md
└── eredmenyek.txt
```
## A kezelo.py-ban található:
- Minden logikai függvény, például az egyes bejelentkezések, regisztrációk jóváírása. Az összes játék létrehozásának, lezárásának, fogadás leadásának a hitelesítése. De az összes ahhoz kapcsolható metódus is, mint az egyes statisztikák eredményei, jelszó titkosítása, elrejtése, összehasonlítása **hashlib** külső python könyvtárral, stb.
- Dinamikus szorzó számítása, aminek a képlete: 1+5/(2<sup>k</sup>-1)+o/k/5, ahol a "k" az összes fogadás az adott alany + eseményre, az "o" pedig az összes fogadás az adott játék bármelyik alany + eseményére.
## A gui.py-ban van:
> Minden egyes oldal meghívása, hogy hogy épül fel az alkalmazás, a megjelenítés elrendezésének alaphelyzetbe állítása. Még a mindig megjelenített profil tulajdonságai is.
## A felhasznalo.py-ban van:
> A bejelentkezés, regisztráció, bejelentkezett oldal, és a profil beállítások oldal megjelenítése. 
## A fogado.py-ban van:
> A fogadás leadása, fogadó kezdő oldalához szükséges megjelenítés. 
## A szervezo.py-ban van:
> A játék létrehozása, lezárása, szervező kezdő oldalához szükséges megjelenítés. 
## A koszontes.py-ban van:
> A program kezdőlapjának, azaz az első oldalának a megjelenítése.
## A lekerdezes.py-ban van:
> A lekérdezés kezdő oldala, a ranglista, játék statisztika, fogadási statisztika oldalának megjelenítése.
## A gui.css-ben van:
> Minden stílus leírás, hogy hogyan nézzen ki.
## Használt technológiák:
### **hashlib:**
*Lehetővé teszi egy szöveg titkosítását.*
Szükséges volt a felhasználó regisztrációjánál és bejelentkezésénél, hogy összehasonlítva tudja, hogy jó jelszót adott-e meg.
A jelszavakat titkosítva mentjük le.
### **PyQt5:**
*Lehetővé teszi az átlátható grafikus felület használatát.*
Szükséges volt a felhasználóbarát felület létrehozásának céljából.
## A program beüzemlésének rövid leírása:
Speciális rendszerkövetelmények nincsenek, Windows-on, MacOS-en, Linux-on is futtatható, de **Python** és a PyQt5 külső python könyvtár telepítése és a szükséges. A program elindításához indítsa el (dupla kattintással) a **start.bat** fájlt, ha Windows gépe van, a **start.sh** fájlt, ha MacOS vagy Linux gépe van. Ezek a fájlok segítenek letelepíteni a szükséges könyvtárakat-.