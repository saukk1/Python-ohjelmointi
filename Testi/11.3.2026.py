nimet = ["Viivi","Ahmed", "Pekka", "Olga", "Mary"]
print(nimet)
print(len(nimet))

nimet.append("Matti")
nimet.remove("Pekka")
nimet.insert(3, "Tiina")
nimet2= ["Allu", "Ninni"]
nimet.extend(nimet2)

print(nimet)
print(nimet.index("Allu"))
