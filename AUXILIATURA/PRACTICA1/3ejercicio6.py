# Definir el diccionario
diccionario = {
    "apple": 10,
    "banana": 20,
    "orange": 15,
    "uva": 30,
    "mango": 25,
    "elefante": 40,
    "iguana": 50,
    "oso": 60
}

for v in diccionario.items():
    print(f"{v[0]}: {v[1]}")
vocales = ['a', 'e', 'i', 'o', 'u']
claves_a_eliminar = []
for clave in diccionario:
    if clave[0].lower() in vocales:
        claves_a_eliminar.append(clave)
for clave in claves_a_eliminar:
    del diccionario[clave]
print()
print("diccionario resultante: ")
print(diccionario)