arvaus= 0
arvausmaara = 5
käyttäjätunnus = "kt"
salasana = "ss"

while arvaus < arvausmaara:
    käyttäjätunnus = input("Syötä käyttäjätunnus: ")
    salasana = input("Syötä salasana: ")
    if käyttäjätunnus == "kt" and salasana == "ss":
        print("Oikein, tervetuloa.")
        break
    else:
        arvaus += 1
        print("Väärin.")

if arvaus == arvausmaara:
    print("Pääsy evätty!")

