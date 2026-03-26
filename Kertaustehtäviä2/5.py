def suurin_arvo(luku1, luku2, luku3):
    return max(luku1, luku2, luku3)

eka= int(input("Anna ensimmäinen luku: "))
toka= int(input("Anna toka luku: "))
kolmas = int(input("Anna kolmas luku: "))

vastaus = suurin_arvo(eka, toka, kolmas)

print(f"\nAntamistasi luvuista suurin on {vastaus}.")

