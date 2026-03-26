def tulosta_kertotaulu():
    syote= int(input("Annna numero: "))
    numero= int(syote)

    if 1<= numero <= 10:
        print(f"\nNumeron {numero} kertotaulu on: ")

        for k in range(1,11):
            tulo= k * numero
            (f"{k:2} * {numero} = {tulo}")
            print(tulo)

tulosta_kertotaulu()



