
numeros = []
n = int(input("ingresar numero n: "))

for _ in range(n):
    numeros.append(int(input()))

print(numeros)


for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        numeros[i] = "Par"
    else:
        numeros[i] = "Impar"

print(numeros)