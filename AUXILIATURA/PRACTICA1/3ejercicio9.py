def contar_vocales(diccionario):
    vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    frecuencia = {
        "a": 0, "e": 0, "i": 0, "o": 0, "u": 0,
        "A": 0, "E": 0, "I": 0, "O": 0, "U": 0
    }
    for clave in diccionario:
        palabra = diccionario[clave]
        for letra in palabra:
            if letra in vocales:
                frecuencia[letra] += 1
    resultado = {}
    for vocal in frecuencia:
        if frecuencia[vocal] > 0:
            resultado[vocal] = frecuencia[vocal]

    return resultado


diccionario = {"uno": "hola", "dos": "mundo", "tres": "python"}
print("el diccionario:")
for i in diccionario.items():
    print(f"{i[0]} -> {i[1]}")

resultado = contar_vocales(diccionario)
print()
print("Contador de vocales: ")
for i in resultado.items():
    print(f"{i[0]} -> {i[1]}")
