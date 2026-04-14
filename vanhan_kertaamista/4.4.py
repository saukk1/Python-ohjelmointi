import random
luku = random.randint(1,10)
arvaus = int(input("Arvaa luku: "))

while True:
    if arvaus == luku:
        print("Oikein")
        break
    if arvaus <= luku:
        print("Liian pieni.")
        arvaus = int(input("Syötä uusi luku: "))
    if arvaus >= luku:
        print("Liian suuri.")
        arvaus = int(input("Syötä uusi luku: "))