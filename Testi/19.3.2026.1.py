#1: Importataan kirjastot
import random
import math
#2: itse määritellyt funktiot

#3: Pääohjelma

def tervehdi(tervehdys, kerrat):
    for k in range(kerrat):
        print(tervehdys)
    return
#pääohjelma
print("Ohjelma alkaa.")
tervehdi("Moikka!",3)
print("Ohjelma loppuu.")
tervehdi("Hei!",5)
print("Vielä kerran.")
tervehdi("Hyvää yötä!",2)

def tervehdi2():
    print("Moikka!")
    return
tervehdi2()

name = "Saulus"
tervehdi(name,2)