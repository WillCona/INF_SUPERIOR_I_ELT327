

n = int(input("ingrese n: "))

for i in range(1, n + 1):
    # Crear I>zquierda (de 1 hasta i)
    ascendente = ""
    for j in range(1, i + 1):
        ascendente += str(j)
        
    # Crear derecha(de i-1 hasta 1)
    descendente = ""
    for j in range(i - 1, 0, -1):
        descendente += str(j)
    # Espácios Izq
    espacios = " " * (n - i)
    # Imprimir
    print(espacios + ascendente + descendente)
print(" " * (n - 1) + str(n))
print(" " * (n - 1) + str(n))
print(" " * (n - 1) + str(n))
