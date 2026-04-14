import random

def heita():
    eka = random.randint(1,6)
    toka = random.randint(1, 6)
    return (eka, toka)

noppa1, noppa2 = heita()
print(f"Heitit nopalla 1: {noppa1} ja nopalla 2: {noppa2}")