kasky = (input("Kerro lukuja, tyhjä lopettaa! "))
luku= int(kasky)
pienin = luku
suurin = luku

while True:
    kasky = (input("Kerro lukuja, tyhjä lopettaa! "))
    if kasky == "":
            break
    luku = int(kasky)
    if luku < pienin:
        pienin = luku
    if luku > suurin:
        suurin = luku

    print(f"Pienin luku oli: {pienin}.")
    print(f"Suurin luku oli: {suurin}.")