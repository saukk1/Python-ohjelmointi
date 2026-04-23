opiskelijat = {"Fanni" : ["Fanni", 1, "Viestintä"],
"Marko" : ["Marko", 2, "Ruotsi"],
"Anna" : ["Anna", 3, "Tiedolla johtaminen"]}

print(f"Fannin vuosiluokka on {opiskelijat["Fanni"][1]}  ja Markon lempiaine on",  opiskelijat["Marko"][2])
opiskelijat["Fanni"][2]= "Suunnistus ja majan rakennus kurssi"
opiskelijat["Valto"] = ["Valto", 1, "Liikunta" ]

del opiskelijat["Anna"]
print(opiskelijat)

