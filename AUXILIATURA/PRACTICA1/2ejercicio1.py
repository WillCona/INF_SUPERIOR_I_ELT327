

n = int(input("ingrese N: "))

pares, impares = 0, 0

for i in range(1, n+1):
    if i % 2 == 0:
        pares += i
    else:
        impares += i

print("pares:", pares)
print("impares:", impares)