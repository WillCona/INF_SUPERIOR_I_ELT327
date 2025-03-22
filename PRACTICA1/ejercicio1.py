
dia = int(input("INgrese dia : "))
mes = int(input("INgrese mes : "))
año = int(input("Ingrese año YYYY: "))


if dia < 30:
    print(f"L fecha siguiente es {dia + 1}/{mes}/{año}")
else:
    dia = 1
    if mes < 12:
        print(f"L fecha siguiente es {dia}/{mes + 1}/{año}")
    else:
        mes = 1
        print(f"La fecha siguiente es {dia}/{mes + 1}/{año + 1}")