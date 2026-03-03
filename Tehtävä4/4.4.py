import random
luku = random.randint(1,10)
arvaus= int(input("Syötä jokin luku: "))
while True:
    if arvaus == luku:
        print("Oikein")
        break

    if arvaus < luku:
        print("Luku on liian pieni.")
        arvaus = int(input("Syötä uusi luku: "))

    if arvaus > luku:
        print("Luku on liian suuri.")
        arvaus = int(input("Syötä uusi luku: "))
