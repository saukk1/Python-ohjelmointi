def muutos(gallonat):
    litrat =gallonat *3.785
    return round(litrat, 2)


while True:
    maara=float(input("Montako gallonaa bensiiniä?: "))
    if maara<0:
        break
    print(f"Tämä määrä on {muutos(maara)} litraa bensiiniä.")