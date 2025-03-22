
n = int(input("Ingrese la cantidad de numeros: "))
suma, contador = 0, 0

for _ in range(n):
    valor = int(input())
    if (valor > 0) and (valor % 5 == 0):
        suma += valor
        contador += 1

if contador != 0:
    print(f"El promedio es {suma/contador}")
else:
    print("inexistente")