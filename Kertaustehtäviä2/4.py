def kuusi(koko):
    print("Tämä on kuusi!")

    for k in range(1, koko +1):
        väli = " " * (koko-k)

        tähdet= "*" * (2* k-1)

        print(väli + tähdet)

    koko_väli = " " * (koko -1)
    print(koko_väli + "*")

kuusi(5)