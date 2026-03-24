def karsinta(lista):
    parilliset=[]
    for luku in lista:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset
alkuperainen_lista=[]
while True:
    syote=(input("Syötä luku, tyhjä lopettaa: "))

    if syote=="":
        break
    luku= int(syote)

    alkuperainen_lista.append(luku)

print("Alkuperäinen lista:", alkuperainen_lista)
print("Karsittu lista:", karsinta(alkuperainen_lista))