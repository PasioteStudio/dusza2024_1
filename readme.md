# Bevezetés:
A program a Dusza Árpád Országos Programozói Emlékverseny 2023/2024 miatt készülhetett el. A feladat egy fogadásos játék volt, ahol fogadni, játékot létrehozni, lezárni és a ranglistát, játék statisztikáját és fogadási statisztikáját lehet megtekinteni.
# Felhasználói dokumentáció
 1. Python telepítése kötelező a program futtatásához.
 2. FONTOS: Mindig lépjünk be a program mappájába(dusza2024_1), onnan indítsuk el
 3.  Hogy futtassuk el kell indítanunk a main.py-t (`py main.py`)
  -  A programot játékok készítésére:
 ![image](https://github.com/atemzy/dusza2024_1/assets/43964339/f04dfd08-e77d-453c-9195-a2016d67ba9b)
  - És annak lezárására
  - Fogadás leadására:
 ![image](https://github.com/atemzy/dusza2024_1/assets/43964339/5fbd4421-c8c4-40e7-8e26-25e1ec2ee146)
# Fejlesztői dokumentáció:
## A kezelo.py-ban található:
> Minden logikai függvény, például az egyes bejelentkezések, regisztrációk jóváírása. Az összes játék létrehozásának, lezárásának, fogadás leadásának a hitelesítése. De az összes ahhoz kapcsolható metódus is, mint a dinamikus szorzó, az egyes statisztikák eredményei, stb.
## A gui.py-ban van:
> Minden megjelenítés, hogy hogy nézzen ki az alkalmazás, a gombok, minden stílus leírás.
## Használt technológiák:
**hashlib:**
*Lehetővé teszi egy szöveg titkosítását.*
Szükséges volt a felhasználó regisztrációjánál és bejelentkezésénél, hogy összehasonlítva tudja, hogy jó jelszót adott-e meg.
A jelszavakat titkosítva mentjük le.
**PyQt5:**
*Lehetővé teszi az átlátható grafikus felület használatát.*
Szükséges volt a felhasználóbarát felület létrehozásának céljából.
a program beüzemelésének rövid leírását a zsűri számára,#TODO