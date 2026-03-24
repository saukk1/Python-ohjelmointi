kaupungit = []
for lista in range(5):
    nimi= input(f"Anna {lista +1}. kaupunki: ")
    kaupungit.append(nimi)

print("Syöttämäsi kaupungit: ")
for kaupunki in kaupungit :
        print(kaupunki)