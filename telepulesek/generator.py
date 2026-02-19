import os

# 1. A teljes település és kerület lista (59 db)
varosok = [
    "Budapest I. kerület", "Budapest II. kerület", "Budapest III. kerület", "Budapest IV. kerület", 
    "Budapest V. kerület", "Budapest VI. kerület", "Budapest VII. kerület", "Budapest VIII. kerület", 
    "Budapest IX. kerület", "Budapest X. kerület", "Budapest XI. kerület", "Budapest XII. kerület", 
    "Budapest XIII. kerület", "Budapest XIV. kerület", "Budapest XV. kerület", "Budapest XVI. kerület", 
    "Budapest XVII. kerület", "Budapest XVIII. kerület", "Budapest XIX. kerület", "Budapest XX. kerület", 
    "Budapest XXI. kerület", "Budapest XXII. kerület", "Budapest XXIII. kerület",
    "Biatorbágy", "Budakalász", "Budakeszi", "Budaörs", "Diósd", "Dunaharaszti", "Dunakeszi", 
    "Dunavarsány", "Érd", "Fót", "Gödöllő", "Gyál", "Gyömrő", "Halásztelek", "Herceghalom", 
    "Kistarcsa", "Maglód", "Mende", "Mogyoród", "Nagykovácsi", "Nagytarcsa", "Páty", "Pécel", 
    "Pilisvörösvár", "Pomáz", "Solymár", "Százhalombatta", "Szentendre", "Szigethalom", 
    "Szigetszentmiklós", "Taksony", "Tárnok", "Törökbálint", "Üllő", "Üröm", "Vecsés"
]

# 2. Beolvassuk a sablon HTML-t
try:
    with open("template.html", "r", encoding="utf-8") as file:
        template = file.read()
except FileNotFoundError:
    print("Hiba: Nem találom a template.html fájlt! Kérlek rakd ugyanabba a mappába.")
    exit()

# Létrehozunk egy mappát a generált oldalaknak
if not os.path.exists("telepulesek"):
    os.makedirs("telepulesek")

# 3. Ékezeteltávolító függvény az URL-hez
def slugify(text):
    cserek = {"á":"a", "é":"e", "í":"i", "ó":"o", "ö":"o", "ő":"o", "ú":"u", "ü":"u", "ű":"u", " ":"-", ".":""}
    text = text.lower()
    for mit, mire in cserek.items():
        text = text.replace(mit, mire)
    return text

# 4. Végigmegyünk a városokon, legeneráljuk és elmentjük
for varos in varosok:
    uj_html = template.replace("{{VAROS}}", varos)
    fajlnev = f"favagas-{slugify(varos)}.html"
    
    with open(f"telepulesek/{fajlnev}", "w", encoding="utf-8") as file:
        file.write(uj_html)
        
    print(f"Kész: {fajlnev} ({varos})")

print(f"\nSiker! {len(varosok)} db aloldal legenerálva a 'telepulesek' mappába.")
