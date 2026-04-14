hedelmat = {"Appelsiini": 13,
           "Banaani": 2,
           "Aprikoosi": 0.2
            }
yhteishinta= 0



while True:
    hedelma = input("Minkä hedelmän hinnan haluat tietää, (tyhjä lopettaa): ").capitalize()
    if hedelma == "":
        print("Päättyy")
        break
    if hedelma in hedelmat:
        yhteishinta += hedelmat[hedelma]
    else:
        print("Valitettavasti tuotetta ei löydy")
        lisataanko= input("haluatko lisätä tuotteen ja hinnan (Y/N)").upper()
        if lisataanko == "Y":
            hinta = float(input(f"Anna hinta {hedelma}:lle. "))
            hedelmat[hedelma] = hinta
            print(f"{hedelma} on lisattu hinnalla {hinta}! ")


print(f"Yhteishinta hedelmille on {yhteishinta}. ")
for hedelma in hedelmat:
    print(f"Hedelmä {hedelma}, hinta {hedelmat[hedelma]}. ")
