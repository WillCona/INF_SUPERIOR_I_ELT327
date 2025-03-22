
a = int(input("ingrese la base: "))
b = int(input("ingrese la potencia: "))

sum = 1
for _ in range (b):
    sum *= a

print(f"El resultado es: {sum}")