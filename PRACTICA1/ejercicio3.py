
a = int(input("INgrese 1° numero: "))
b = int(input("INgrese 2° numero: "))
c = int(input("INgrese 3° numero: "))

intermedio = a + b + c - min(a, b, c) - max(a, b, c)

print(f"a) El valor intermedio es: {intermedio}")

print(f"b) orden descendente: {max(a,b,c)}, {intermedio}, {min(a,b,c)}")
