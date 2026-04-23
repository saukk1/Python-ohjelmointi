kirjasto = {"Muistelmat liitukaudelta." : ["Oliver sr.", 1997, "Tietokirjallisuus"],
"Leipomisen perusteet" : ["Miko", 2020, "Tietokirjallisuus"],
"Koripallo ja haaveet" : ["Sandels", 2023, "Fantasia"]}

print(kirjasto, ["Muistelmat liitukaudelta"][0], kirjasto["Leipomisen perusteet"][2])
kirjasto["Leipomisen perusteet"][2]= "Fantasia"
kirjasto["Onni ja pyörä"] = ["Valto", 2025, "Tietokirjallusuus"]
del kirjasto["Koripallo ja haaveet"]

print(kirjasto)