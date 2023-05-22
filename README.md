## Programozás 1, 2. ZH (gyakorlás)

A feladat egy olyan program elkészítése, amely színdarabok szövegkönyveiről készít statisztikákat.

A program a [main.py](main.py) futtatásával legyen indítható.

Parancssori argumentumként opcionálisan megadható egy könyvtár elérési útja, ahol a színdarab szövegei találhatók.
Ha ez megadásra került, akkor induláskor kerüljön beolvasásra.
Ha a könyvtár nem található, vagy nem lett megadva argumentum, írjon ki egy hibaüzenetet (`Error: Directory not found.`), és kérjen be egy új elérési utat a felhasználótól.
Ezt addig ismételje, míg egy létező könyvtárt nem kap.

A beolvasáshoz használja a [play.py](play.py)-ban található `load_play` függvényt, ami a könyvtárban lévő `.txt` fájlokra hívja meg a [scene.py](scene.py)-ban található `load_scene` függvényt.

Minden jelenet (scene) szövegkönyve egy külön `jelenet_neve.txt` fájlban van tárolva. A jelenetben a karakterek megszólalásai (speeches) vannak.
**Minden megszólalás első sora a megszólaló karakter nevét tartalmazza csupa nagybetűvel.** Az ezt követő sorokban van a megszólalás szövege, amit egy üres sor zár le.
Ezután lehetnek szögletes zárójelbe írt rendezői utasítások, a következő megszólalást ismét a karakter nagybetűs nevét tartalmazó sor előzi meg.

A `load_scene` olvassa be a jelenet szövegkönyvét, és adja vissza a megszólaló karakterek listáját. Minden karakter neve annyiszor szerepeljen a listában, ahányszor megszólal a jelenetben.

A főmenü 1. menüpontjában lehessen új színdarabot beolvasni. Itt hiba esetén térjen vissza a főmenübe, és maradjon változatlan a korábban beolvasott színdarab.

A 2. és 3. menüpontokhoz készüljenek segédfüggvények a megfelelő modulokban, és az alábbi módon működjenek:

A 2. menüpont kiválasztásakor kérje be egy karakter nevét (kis- és nagybetűket NE vegye figyelembe), majd listázza ki azon jelenetek nevét, amelyekben a karakter legalább egyszer megszólal.
Ha a karakter nem található a színdarabban, írja ki az `Error: No character with this name.` hibaüzenetet, és térjen vissza a főmenübe.

A 3. menüpont kiválasztásakor jelenítsen meg egy kimutatást, melyben minden szereplő karakterhez írja ki az összes megszólalásainak számát.

Példa kimenet a hamlet-demo-ra:

```
FRANCISCO: 8
BARNARDO/MARCELLUS: 1
HORATIO: 64
KING: 7
HAMLET: 72
POLONIUS: 9
BARNARDO: 19
QUEEN: 3
OPHELIA: 10
HORATIO/MARCELLUS: 2
CORNELIUS/VOLTEMAND: 1
GHOST: 13
MARCELLUS: 30
LAERTES: 8
ALL: 4
```
