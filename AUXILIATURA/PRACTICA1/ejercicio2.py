def fecha_valida(dia, mes, año):
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mes < 1 or mes > 12:
        return "Fecha Incorrecta"
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        dias_mes[1] = 29 
    if dia < 1 or dia > dias_mes[mes - 1]:
        return "Fecha Incorrecta"

    return "Fecha Correcta"

# MAIN
a, b, c = map(int, input().split())

print(fecha_valida(a, b, c))

a, b, c = map(int, input().split())

print(fecha_valida(a, b, c))

a, b, c = map(int, input().split())

print(fecha_valida(a, b, c))
