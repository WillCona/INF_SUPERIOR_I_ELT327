def combinar_diccionarios(dic1, dic2):
    combinado = {}

    for clave in dic1:
        combinado[clave] = dic1[clave]

    for clave in dic2:
        combinado[clave] = dic2[clave]

    claves = list(combinado.keys())

    n = len(claves)
    for i in range(n):
        for j in range(0, n - i - 1):
            if str(claves[j]) > str(claves[j + 1]): 
                claves[j], claves[j + 1] = claves[j + 1], claves[j]

    diccionario_ordenado = {}
    for clave in claves:
        diccionario_ordenado[clave] = combinado[clave]

    return diccionario_ordenado

#MAIN
dic1 = {3: "tres", "a": "letra A", 10: "diez", "z": "letra Z"}
dic2 = {"b": "letra B", 1: "uno", "c": "letra C", 5: "cinco", "@": "arroba"}

print("diccionario_1")
for i in dic1.items():
    print(f"{i[0]}: {i[1]}")

print()
print("diccionario 2")
for i in dic1.items():
    print(f"{i[0]}: {i[1]}")

resultado = combinar_diccionarios(dic1, dic2)
print()
print("diccionario union ordenado")
for i in resultado.items():
    print(f"{i[0]}: {i[1]}")
