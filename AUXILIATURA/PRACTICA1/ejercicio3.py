
def dev_mes(numero):
    if m >= 1 or m <= 12:
        if m == 1:
            return "Enero"
        elif m == 2:
            return "Febrero"
        elif m == 3:
            return "Marzo"
        elif m == 4:
            return "Abril"
        elif m == 5:
            return "Mayo"
        elif m == 6:
            return "Junio"
        elif m == 7:
            return "Julio"
        elif m == 8:
            return "Agosto"
        elif m == 9:
            return "Septiembre"
        elif m == 10:
            return "Octubre"
        elif m == 11:
            return "Noviembre"
        elif m == 12:
            return "Diciembre"
    return "No valido"

#Main
m = int(input())
print(dev_mes(m))

m = int(input())
print(dev_mes(m))