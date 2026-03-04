name = input("Mikä on nimesi? ")

if name == "Matti":
    print("Tämä ei ole tarkoitettu Mateille. SEURAAVA!")

else:
    annosmaara = float(input("Montako keittoannosta? "))
    kokonaishinta = 5.9 * annosmaara
    print(f"Kokonaishinta on {kokonaishinta}. Seuraava, kiitos! ")

