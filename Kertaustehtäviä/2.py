tuntipalkka= float(input("Mikä on tuntipalkkasi? "))
print(f"Tuntipalkkasi on: {tuntipalkka} ")
tunnit = float(input("Mikä on tehtyjen tuntien määrä? "))
print(f"Tehtyjen tuntiesi määrä on: {tunnit} ")
viikonpäivä = input("Mikä on viikonpäivä? ")
print(f"Viikonpäivä on: {viikonpäivä} ")


if viikonpäivä == "Sunnuntai" :
    spalkka= tuntipalkka * 2 * tunnit
    print(f"Päiväpalkkasi on: {spalkka} ")
else:
    päiväpalkka = tunnit * tuntipalkka
    print(f"Päiväpalkkasi on {päiväpalkka}: ")
