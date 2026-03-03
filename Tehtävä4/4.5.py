maksimi = 5
käyttäjätunnus= "pythonmike"
salasana= "testomake"
kokeilut = 0


while kokeilut < maksimi:
    pythonmike = input("Anna käyttäjätunnus: ")
    testomake = input("Anna salasana: ")
    if pythonmike == käyttäjätunnus and testomake == salasana:
        print("Tervetuloa!")
        break
    else:
        kokeilut = kokeilut + 1

        if kokeilut < maksimi:
            print("Väärin")

if kokeilut == maksimi:
    print("Liian monta arvausta, pääsy evätty.")

