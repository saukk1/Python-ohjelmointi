leiviskä=float(input("Anna leiviskät."))
naula=float(input("Anna naulat."))
luoti=float(input("Anna luodit."))


leiviskä_luoti= leiviskä * 20 * 32
naula_luoti= naula * 32
yhteensä_luoti= luoti + naula_luoti + leiviskä_luoti


yhteensä_gramma= yhteensä_luoti * 13.3
kilogramma= int(yhteensä_gramma/ 1000)

gramma= yhteensä_gramma - (kilogramma*1000)
print("Massa nykymittojen mukaan:")
print(f"{kilogramma} kilogrammaa ja {gramma:.2f} grammaa")

