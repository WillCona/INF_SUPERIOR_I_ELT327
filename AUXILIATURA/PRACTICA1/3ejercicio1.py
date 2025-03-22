
x = input("Ingrese la cadena: ")
cadena = ""

for i in range(len(x)):
    if x[i] == " ":
        cadena += " "
    elif x[i].lower() not in "aeiouáéíóúàèìòùäëïöü":
        cadena = cadena + x[i] + x[i]

print(cadena)