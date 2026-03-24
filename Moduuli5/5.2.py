lista= []

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    if syote == "":
        break
    luku = int(syote)
    lista.append(luku)


lista.sort(reverse=True)
print("Kiitos luvuista, viisi suurinta on:")
for luku in lista [:5]:
    print(luku)
