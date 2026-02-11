vuosi = int(input("Tällä kertaa voisit kertoa jonkun vuosiluvun ja minä kerron onko se karkausvuosi. "))
if (vuosi % 4 == 0 and vuosi % 100 != 0 or vuosi % 400 == 0):
    print("Vuosi", vuosi, "on karkausvuosi.")
else:
    print("Vuosi", vuosi, "ei ole karkausvuosi." )
