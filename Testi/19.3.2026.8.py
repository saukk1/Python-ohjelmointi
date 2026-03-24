def keskiarvo(_luku1, _luku2, _luku3):
    _tulos = (_luku1 +_luku2+_luku3)/3
    return _tulos

#Pääohjelma
luku1= int(input("Kerro 1. luku: "))
luku2= int(input("Kerro 2. luku: "))
luku3= int(input("Kerro 3. luku: "))

tulos = keskiarvo(luku1, luku2, luku3)
print("Keskiarvo on:",tulos)