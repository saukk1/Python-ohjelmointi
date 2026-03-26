lista= []

while True:
    syote = int(input("Anna luku ja listaan sen: "))
    if syote == 0:
        break
    lista.append(syote)



    print(f"Tässä on lista {lista}. ")
    lista.sort()
    print(f"Tässä on uusi lista {lista}. ")
