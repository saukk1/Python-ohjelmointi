kuukaudet = ("talvi" , "talvi",
                "kevät", "kevät" , "kevät",
                "kesä" , "kesä" , "kesä",
                "syksy" , "syksy" , "syksy", "talvi")

kuukausi = int(input("Anna kuukauden numero (1-12), kerron mihin vuodenaikaa se kuuluu: "))
print(kuukaudet[kuukausi-1])
