def vaihda():
    kaupunki= "Vantaa" #Tämä on paikallinen muuttuja
    print("Funktion lopuksi: " + kaupunki)
    return

#Pääohjelma
kaupunki = "Helsinki"   #Tämä on globaali muuttuja

print("Pääohjelmassa aluksi kaupunki on", kaupunki)
vaihda()
print("Pääohjelmassa lopuksi kaupunki on", kaupunki)