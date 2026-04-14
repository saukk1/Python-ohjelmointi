luku = (input("Anna luku: "))
maara = int(luku)
pienin = maara
suurin = maara
while True:
    luku = (input("Anna luku: "))
    if luku == "":
        break
    maara= int(luku)
    if maara < pienin:
       pienin = maara
    if maara > suurin:
        suurin = maara
print(pienin)
print(suurin)

