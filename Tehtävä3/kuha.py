pituus= float(input(f"Mikä on kuhasi mitta senttimetreinä?"))
if pituus <37:
    print("Kuhasi on alamittainen, päästä se välittömästi takaisin järveen!")
    puuttuu= 37-pituus
    print("Kuhasi pitää kasvaa vielä", puuttuu, "senttiä, eli halkosi verran.")
if pituus >=37:
    print("Onnea, voit pitää kuhasi!")