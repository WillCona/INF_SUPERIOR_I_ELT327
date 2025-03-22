
diccionario = {}

palabras = input("ingrese la cadena: ").split(" ")

for i in palabras:
    if i in diccionario:
        diccionario[i] = diccionario[i] + 1
    else:
         diccionario[i] = 1

print(diccionario)
