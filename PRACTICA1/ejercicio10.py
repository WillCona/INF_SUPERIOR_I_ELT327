n = int(input("Ingrese la cantidaD DE NUMEROS: "))

vector = []

for _ in range(n):
    valor = int(input())
    if valor < 0:
        vector.append(valor)

vector.sort()

contador = 0

for i in vector:
    if (i - vector[len(vector)-1]) == 0:
        contador += 1
if len(vector) != 0:
    print(f"el mayor negativo es {vector[len(vector)-1]}, se repite {contador} veces.")
else:
    print("No hay negativos")

