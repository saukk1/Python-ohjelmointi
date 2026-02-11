print("Loistavaa, että olet saapunut risteilyllemme!")
hyttiluokka= input("Jotta et eksy naapurihyttiin, kertoisitko hyttiluokkasi, A/B/C/LUX: ")
if hyttiluokka == "A":
    print("Hyttisi on ikkunallinen autokannen yläapuolella")
elif hyttiluokka == "B":
    print("Hyttisi on ikkunaton autokannen yläpuolella")
elif hyttiluokka == "C":
    print("Hyttisi on ikkunaton autokannen alapuolella" )
elif hyttiluokka == "LUX":
    print("Hyttisi on parvekkeellinen hytti yläkannella.")
else:
    print("Tarkista isot kirjaimet, virheellinen hyttiluokka. Luulen että olet eksynyt leipurihyttiin!")
