sukupuoli= input("Hauska tavata ystäväiseni! Kertoisitko sukupuolesi N/M: ")
if sukupuoli =="M":
    Mhemo= float(input("Kerro sinun hemoglobiinisi: "))
    if Mhemo <134:
        print("Hemoglobiinisi on alhainen.")
    elif Mhemo >195:
        print("Hemoglobiinisi on korkea.")
    else:
        print("Hemoglobiinisi on viitearvoissa.")

elif sukupuoli =="N" :
    Nhemo = float(input("Kerro sinun hemoglobiinisi: "))
    if Nhemo < 117:
        print("Hemoglobiinisi on alhainen.")
    elif Nhemo > 175:
        print("Hemoglobiinisi on korkea.")
    else:
        print("Hemoglobiinisi on viitearvoissa.")


