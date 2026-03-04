tarina = " "

while True:

    sana= input("Anna sanoja ja teen sinulle tarinan: ")
    if sana == "Loppu" or sana == "loppu":
        break
    tarina = tarina + " " + sana

print(f"Tässä on tarinasi: {tarina}")


