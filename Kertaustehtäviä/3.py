import math
while True:
    luku = float(input("Kerro joku kokonaisluku: "))
    if luku < 0:
        print("Virheellinne luku.")
    elif luku > 0:
        print(f"Luvun neliöjuuri on: {math.sqrt(luku)}")

    else:
         luku == 0
         break


