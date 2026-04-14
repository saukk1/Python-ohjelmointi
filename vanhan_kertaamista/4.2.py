tuuma = 2.54
while True:
    maara= float(input("Anna tuuma, negatiivinen lopettaa: "))
    if maara <0:
        break
    print(f"{maara} on {tuuma*maara}cm" )