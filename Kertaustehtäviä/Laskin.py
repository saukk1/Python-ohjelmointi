print("\n-------TERVETULOA KÄYTTÄMÄÄN LASKINTA-------")

while True:
    print("\nValitse mitä toimintoa haluat käyttää:\nA: Yhteenlasku \nB: Vähennyslasku\nC: Kertolasku\nD: Jakolasku")

    valinta = input("Valintasi (A - D, Q lopettaa): ").upper()
    if valinta == "Q":
        print("Ohjelma päättyy.")
        break
    a= float(input("Anna eka luku: "))
    b= float(input("Anna toka luku: "))
    if valinta == "A":
        print("Lukujen summa on:", a+b)
    elif valinta == "B":
        print("Lukujen erotus on:", a-b)
    elif valinta == "C":
        print("Lukujen tulo on:", a*b)
    elif valinta == "D":
        print("Lukujen jakojäännös on:", a/b)
    else:
        print("Virheellinen valinta.")

