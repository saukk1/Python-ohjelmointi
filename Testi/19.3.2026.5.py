def tervehdi(nimi):
    print(f"Tervehdys {nimi}!")
    return

def tervehdi_monesti(nimi, kerrat):
    while kerrat > 0:
        tervehdi(nimi)
        kerrat -=1
    return


#Pääohjelma
tervehdi_monesti("Saulus", 3)