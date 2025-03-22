
nombres = ["Ana", "Luis", "Carlos", "Maria", "Pedro"]
edades = [23, 30, 18, 25, 22]

print("nombres", nombres)
print("edades: ", edades)

for i in range(len(edades)):
    for j in range(0, len(edades) - i - 1):
        if edades[j] > edades[j + 1]:
            edades[j], edades[j + 1] = edades[j + 1], edades[j]
            nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]

#main
print()
print("ordenando")
print("nombres", nombres)
print("edades: ", edades)
tercer_nombre = nombres[2]
# Mostrar el resultado
print(f"El tercer nombre con la menor edad es: {tercer_nombre}")
