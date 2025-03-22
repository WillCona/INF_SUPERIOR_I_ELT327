def intercambiar_claves_valores(diccionario):
    nuevo_diccionario = {}

    for clave, valor in diccionario.items():
        nuevo_diccionario[valor] = clave  

    return nuevo_diccionario  

diccionario_original = {
    "nombre": "Carlos",
    "edad": 25,
    "ciudad": "La Paz"
}


diccionario_nuevo = intercambiar_claves_valores(diccionario_original)

# Mostrar los resultados
print("Diccionario original:")
for clave, valor in diccionario_original.items():
    print(f"{clave}: {valor}")
print()
print("\nDiccionario intercambiado:")
for clave, valor in diccionario_nuevo.items():
    print(f"{clave}: {valor}")
