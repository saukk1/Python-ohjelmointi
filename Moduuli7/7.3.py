lentoasemat = {}
while True:
    toiminto = input("Valitse \n A: Jos haluat lisätä lentoaseman. \n B: Jos haluat hakea lentoasemaa \n C: Jos haluat lopettaa. ").upper()
    if toiminto == "C":
        break
    if toiminto == "A":
        icao = input("Syötä lentoaseman icao: ")
        nimi = input("Syötä lentoaseman nimi: ")
        lentoasemat[icao] = nimi
    if toiminto == "B":
        icao = input(f"Anna ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print(f"Lentoaseman nimi: {lentoasemat[icao]}")
        else:
            print(f"Lentoasemaa ei löytynyt.")

    else:
        print("Virheellinen syöte.")
