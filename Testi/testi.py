name = "Saulus"
lisa = 10
age= int(input("Kuinka vanha olet?"))
print(f"Olet {age + lisa} vuotta vanha.")

numero1 =100
numero2 ="100"
print(numero1+numero1)
print(numero2+numero2)
print(numero1, numero2)

luku1 = float(input("Anna eka luku"))
luku2 = float(input("Anna toka luku"))

print(luku1+luku2)
print(luku1-luku2)
print(luku1/luku2)
print(luku1*luku2)
print(luku1//luku2)
print(luku1**luku2)
print(luku1%luku2)
print(luku1>luku2)
print(luku1<luku2)

pituus = int(input( "Anna pituutesi:"))
paino = float(input("Anna painosi:"))



bmi = paino / (pituus/100) **2
print("BMI:si on", bmi)

import math
print(math.pi)
print(math.e)
print(math.log)
print(math.sin)
print(math.tan)
print(math.cos)


leiviskä_naula= 20
naula_luoti= 32
luoti_gramma= 13.3

naula_luoteina= naula * naula_luoti
leiviskä_luoteina=leiviskä * leiviskä_naula * naula_luoti
yhteensä_luoti= luoti + naula_luoteina + leiviskä_luoteina
