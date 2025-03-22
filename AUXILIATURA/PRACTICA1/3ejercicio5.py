# Listas de números (pueden tener tamaños diferentes)
lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [6, 7, 8, 9]

print("lista1:",lista1)
print("lista2:", lista2)


if len(lista2) > len(lista1):
    lista1, lista2 = lista2, lista1

for i in range(len(lista2)):
    lista1[i] += lista2[i]

print("suma de los vectores: ", lista1)
print("multiplos de 3: ")
for i in lista1:
    if i % 3 == 0:
        print(i)