
palabras = []
n = int(input("cantidad de palabras: "))
c =0

for _ in range(n):
    palabras.append(input())


for i in palabras:
    for j in range(len(i)):
        if i[j].lower() in "aeiouáéíóúàèìòùäëïöü":
            c += 1

print(f"total vocales: {c}")