
cadena = input("ingrese cadena: ")
char = ""
while True:
    char = input("Ingrese un carácter: ")
    if len(char) == 1 and char.isprintable():
        break
    print("Entrada inválida. Debe ingresar un solo carácter.")
c = 0
for i in range(len(cadena)):
    if cadena[i] == char:
        c += 1

print(f"el caracter {char} aparece {c} veces")
