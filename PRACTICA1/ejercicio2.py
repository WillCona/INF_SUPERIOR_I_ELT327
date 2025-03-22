
menor = 10**100
n = int(input("Ingrese la cantidad de numeros: "))

for _ in range(n):
    valor = int(input())
    if valor < menor:
        menor = valor

print(f"El menor es {menor}")
