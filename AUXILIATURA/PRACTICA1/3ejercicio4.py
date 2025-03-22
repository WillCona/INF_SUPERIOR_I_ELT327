
palabras = []
n = int(input("Numero de palabras: "))
for _ in range(n):
    palabras.append(input())

print(palabras)
c = 0
for i in palabras:
    palabra = ""
    for j in range(len(i)):
        if i[j] == " ":
            palabra += " "
        elif i[j] == "a":
            palabra += "1"
        elif i[j] == "e":
            palabra += "2"
        elif i[j] == "i":
            palabra += "3"
        elif i[j] == "o":
            palabra += "4"
        elif i[j] == "u":
            palabra += "5"
        else:
            palabra += i[j]
    
    palabras[c] = palabra
    c += 1

print(palabras)

