
lista = []

while True:
    n = int(input("Ingrese num: "))
    
    if n == 0:
        break

    lista.append(n)

n = len(lista)
for i in range(n):
    for j in range(0, n - i - 1):
        if lista[j] > lista[j + 1]:  
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
print("ordenada:",lista)
