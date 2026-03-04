import math
while True:

    lasku= input(f"+,-,* tai /, 'loppu' lopettaa. ")
    if lasku == "loppu":
        print("Lopetetaan..")
        break
    ekaluku= int(input("Anna ensimmäinen luku: "))
    tokaluku = int(input("Anna toinen luku: "))

    if lasku == "+":
        print("tulos", ekaluku + tokaluku)

    elif lasku == "-":
        print("tulos",ekaluku - tokaluku)
    elif lasku == "*":
        print("tulos",ekaluku * tokaluku)
    elif lasku == "/":
        print("tulos",ekaluku / tokaluku)
    else:
        print("Tuntematon toiminto. ")



