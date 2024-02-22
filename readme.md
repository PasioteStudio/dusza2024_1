# Bevezetés:
A program a Dusza Árpád Országos Programozói Emlékverseny 2023/2024 miatt készülhetett el. A feladat egy fogadásos játék volt, ahol fogadni, játékot létrehozni, lezárni és a ranglistát, játék statisztikáját és fogadási statisztikáját lehet megtekinteni.
# Felhasználói dokumentáció
 1. Python telepítése kötelező a program futtatásához.
 2. FONTOS: Mindig lépjünk be a program mappájába(dusza), onnan indítsuk el
 3.  Hogy futtassuk el kell indítanunk a gui.py-t (`py gui.py`)
  -  A programot játékok készítésére:
 ![image](https://github.com/atemzy/dusza2024_1/assets/43964339/f04dfd08-e77d-453c-9195-a2016d67ba9b)
  - És annak lezárására:
 ![Képernyőkép 2024-02-21 181554](https://github.com/atemzy/dusza2024_1/assets/43964339/14312892-f38e-449c-9082-87c856958354)
  - Fogadás leadására:
 ![Képernyőkép 2024-02-21 181541](https://github.com/atemzy/dusza2024_1/assets/43964339/d0038e23-d0d7-456a-b23e-90abc0c55291)
# Fejlesztői dokumentáció:
## A kezelo.py-ban található:
> Minden logikai függvény, például az egyes bejelentkezések, regisztrációk jóváírása. Az összes játék létrehozásának, lezárásának, fogadás leadásának a hitelesítése. De az összes ahhoz kapcsolható metódus is, mint a dinamikus szorzó, az egyes statisztikák eredményei, jelszó titkosítása, elrejtése, összehasonlítása, stb.
## A gui.py-ban van:
> Minden megjelenítés, hogy hogyan épüljön fel az alkalmazás, a gombok kinézete, funkcionalitása, a megjelenítés elrendezése, stb.
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
a program beüzemelésének rövid leírását a zsűri számára,
## A program beüzemlésének rövid leírása:
Speciális rendszerkövetelmények nincsenek, Windows-on, MacOS-en, Linux-on is futtatható, de **Python** telepítése szükséges. A program elindításához be kell lépjünk a program mappájába (dusza) és a a `py gui.py` parancs begépelésével elindul.