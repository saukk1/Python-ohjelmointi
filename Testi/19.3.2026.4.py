def inventaario(tavarat):
    print("Sinulla on seuraavat tavarat repussa: ")
    for t in tavarat:
        print("- "+ t)
    tavarat.clear()
    return

#Pääohjelma
reppu= ["Taskulamppu", "Otsalamppu", "Pöytälamppu"]
inventaario(reppu)

reppu.append("Eväsleipä")
inventaario(reppu)