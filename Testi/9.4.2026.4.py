numerot =  {"Viivi": "050-1234567",
           "Ahmed": "040-1112223",
           "Pekka": "050-7654321"}

numerot["Volga"] = "044.1234567"

for n in numerot:
    print(f"Henkilön {n} puhelinnumero on {numerot[n]}. ")