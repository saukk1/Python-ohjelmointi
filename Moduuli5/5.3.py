luku = int(input("Sano joku luku ja kerron onko se alkuluku: "))
alkuluku= True

for jakaja in range(2,luku):
    if luku % jakaja == 0:
        alkuluku = False
        break

if alkuluku:
    print(f"Loistavaa!! Luku {luku} on alkuluku.")
else:
    print(f"Oivoi, luku {luku} ei ole alkuluku.")
