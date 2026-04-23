lentoasemat = {
    "EFHK" : "Helsinki-Vantaa",
    "EFHF" : "Malmin lentoasema",
    "JHKY" : "Dubai"
}

while True:
    print("Valitse toiminto: A = SYÖTÄ, B = HAE, Q = LOPETA")
    valinta = input("Mitä haluat tehdä? ").upper()
    if valinta == "Q":
        print("Ohjelma päättyy...")
        break
    elif valinta == "A":
        icao = input("Anna lentoaseman ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Uusi lentoaseman nimi tallennettu. ")
    elif valinta == "B":
        icao = input("Anna lentoaseman icao-koodi: ").upper()
        if icao in lentoasemat:
            print("Lentoaseman nimi: ", lentoasemat[icao])
        else:
            print("Koodilla ei löytynyt lentoasemaa. ")
    else:
        print("Virheellinen valinta.")

