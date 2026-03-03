while True:
    tuuma = float(input(f"Kerro tuuma (negatiivinen lopettaa) "))
    if tuuma <0:
        print("Tuumat ei voi olla negatiivisia.")
        break

    cm = tuuma * 2.54
    print(f"{tuuma} tuumaa on {cm} cm ")

       

